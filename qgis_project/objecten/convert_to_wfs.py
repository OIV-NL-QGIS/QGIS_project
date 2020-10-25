import re
import os
import xml.etree.ElementTree as ET

tree = ET.parse('./OIV_Objecten.qgs')
root = tree.getroot()

with open('geoserver.conf', 'r') as f:
    x = f.read().splitlines()

geoserverURL = "'{}'".format(x[0])
#geoserverURL = geoserverURL.replace('http://', 'http://{}:{}@'.format(x[2], x[3]))
geoserverBron = x[1]
dimensionDbPath = './db/dimension_tables.db'

dropKeyList = ['service', 'sslmode', 'key', 'type', 'checkPrimaryKeyUnicity', '(geom)']
wfsSettingsDict = {'user': x[2], 'password': x[3], 'pagingEnabled': "'false'", 'restrictToRequestBBOX' : '', 'srsname' : '', 'typename' : '', 'url' : '',\
                   'version': "'1.0.0'", 'table': '""', 'sql': ''}
wfsNoGeoLayers = ['aanwezig', 'bedrijfshulpverlening', 'beheersmaatregelen', 'contactpersoon', 'gebruiksfunctie', 'gevaarlijkestof',\
                  'gevaarlijkestof_schade_cirkel', 'historie', 'scenario', 'veilighv_org']

postgresLayers = {}
sqliteLayers = {}

for layer in root.iter('layer-tree-layer'):
    if layer.attrib["providerKey"] == 'postgres':
        sourceList = []
        uriWfs = wfsSettingsDict
        lst = re.split(' |=',layer.attrib["source"].strip())
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst) - 1, 2)}
        tableName = res_dct["table"].split('.')[1].replace('"','') 
        if "type" in res_dct.keys() or tableName in wfsNoGeoLayers:
            for key in dropKeyList:
                res_dct.pop(key, None)            
            uriWfs['url'] = "%s" % geoserverURL
            typeName = geoserverBron + ':' + tableName
            uriWfs['typename'] = "'%s'" % typeName
            layer.attrib["providerKey"] = 'WFS'        
            if 'srid' in res_dct.keys():
                srsName = 'EPSG:' + res_dct["srid"]
                uriWfs['restrictToRequestBBOX'] = '1'
            else:
                srsName = 'EPSG:28992'
                uriWfs['restrictToRequestBBOX'] = '0'
            uriWfs['srsname'] = "'%s'" % srsName
            uriWfs.update(wfsSettingsDict)
            for key in uriWfs:
                sourceList.append(key + '=' + uriWfs[key])
            layer.attrib["source"] = ' '.join(sourceList)
            postgresLayers.update({layer.attrib["name"] : layer.attrib["source"]})
        else:
            for key in dropKeyList:
                res_dct.pop(key, None)              
            layer.attrib["providerKey"] = 'spatialite'
            sourceList.append("dbname='{}'".format(dimensionDbPath))
            sourceList.append('table="{}"'.format(tableName))
            if tableName == 'veiligheidsregio_huidig':
                sourceList.append('(geom)')
            sourceList.append('sql=')
            layer.attrib["source"] = ' '.join(sourceList)
            sqliteLayers.update({layer.attrib["name"] : layer.attrib["source"]})

for layer in root.iter('maplayer'):
    if layer.find('layername').text in postgresLayers.keys():
        layer.find('datasource').text = postgresLayers[layer.find('layername').text]
        layer.find('provider').text = 'WFS'
    if layer.find('layername').text in sqliteLayers.keys():
        layer.find('datasource').text = sqliteLayers[layer.find('layername').text]
        layer.find('provider').text = 'spatialite'

for elem in root.iter('Variables'):
    for var in elem.findall('variableNames'):
        count = 0
        for val in var.findall('value'):
            if val.text == 'connection':
                index = count
            count += 1
    for var in elem.findall('variableValues'):
        var[index].text = 'WFS'

tree.write('./OIV_Objecten.qgs')
#os.remove('./geoserver.conf')
