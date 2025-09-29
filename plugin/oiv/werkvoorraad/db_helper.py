import psycopg2
from configparser import ConfigParser
from psycopg2.extras import RealDictCursor
import qgis.core as QC
import oiv.helpers.constants as PC
import oiv.helpers.configdb_helper as CH
import oiv.helpers.messages as MSG
import oiv.helpers.utils_core as UC

layerFields = {
    "Werkvoorraad object - punt": [["object_id", "int"], ["rotatie", "int"], ["symbol_name", "type"], ["label", "string"], 
                                   ["opmerking", "string"], ["formaat_object", "string"], ["label_positie", "string"]],
    "Werkvoorraad object - label": [["object_id", "int"], ["rotatie", "int"], ["symbol_name", "type"], ["omschrijving", "string"],
                                    ["opmerking", "string"], ["formaat_object", "string"]],
    "Werkvoorraad object - lijn": [["object_id", "int"], ["symbol_name", "type"], ["opmerking", "string"]],
    "Werkvoorraad object - vlak": [["object_id", "int"], ["symbol_name", "type"], ["opmerking", "string"]],
    "Werkvoorraad bouwlaag - punt": [["bouwlaag_id", "int"], ["rotatie", "int"], ["symbol_name", "type"], ["label", "string"], 
                                     ["opmerking", "string"], ["formaat_bouwlaag", "string"], ["label_positie", "string"]],
    "Werkvoorraad bouwlaag - label": [["bouwlaag_id", "int"], ["rotatie", "int"], ["symbol_name", "type"], ["omschrijving", "string"], 
                                      ["opmerking", "string"], ["formaat_bouwlaag", "string"]],
    "Werkvoorraad bouwlaag - lijn": [["bouwlaag_id", "int"], ["symbol_name", "type"], ["opmerking", "string"]],
    "Werkvoorraad bouwlaag - vlak": [["bouwlaag_id", "int"], ["symbol_name", "type"], ["opmerking", "string"]]
}

def setup_postgisdb_connection():
    """setup the postgis database connection"""
    conn = None
    cursor = None
    try:
        config = ConfigParser()
        #filePath = QC.QgsProject.instance().readPath("./")
        filePath = "C:/programdata/oiv"
        fileName = filePath + '/pg_service.conf'
        config.read_file(open(fileName))
        dbName = config.get('oiv', 'dbname')
        user = config.get('oiv', 'user')
        passw = config.get('oiv', 'password')
        host = config.get('oiv', 'host')
        port = config.get('oiv', 'port')
        connString = "dbname={} user={} password={} host={} port={}".format(dbName, user, passw, host, port)
        conn = psycopg2.connect(connString)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
    except:  # pylint: disable=bare-except
        print("Failed to connect to the oiv database")
    return conn, cursor

def close_db_connection(cursor, conn):
    """when ready, close the database connection"""
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def get_bouwlagen(objectId):
    bouwlagen = []
    conn, cursor = setup_postgisdb_connection()
    query = 'SELECT bouwlaag FROM mobiel.bouwlagen_binnen_object WHERE object_id = {};'.format(int(objectId))
    cursor.execute(query)
    bouwlaagTuple = cursor.fetchall()
    if bouwlaagTuple:
        bouwlagen = [tup["bouwlaag"] for tup in bouwlaagTuple]
    close_db_connection(cursor, conn)
    return bouwlagen

def check_object_mods(objectId):
    answer = False
    conn, cursor = setup_postgisdb_connection()
    query = "SELECT object_id FROM mobiel.object_binnen_bouwlaag WHERE pand_id = '{}';".format(objectId)
    cursor.execute(query)
    objectTuple = cursor.fetchall()
    if objectTuple:
        answer = True
    close_db_connection(cursor, conn)
    return answer

def execute_queries(executableFeatures, bouwlaagOfObject, accept):
    conn, cursor = setup_postgisdb_connection()
    for arr in executableFeatures:
        feat = arr[0]
        ilayer = arr[1]
        layerName = ilayer.name()
        layerType = UC.check_layer_type(ilayer)
        operatie = feat['operatie']
        update_accepted(layerName, accept, cursor, conn)
        if accept and operatie == 'INSERT':
            result = insert_feature(feat, cursor, conn, layerName, bouwlaagOfObject, layerType)
        if accept and operatie == 'UPDATE':
            result = update_feature(feat, cursor, conn, layerName, bouwlaagOfObject, layerType)
        if accept and operatie == 'DELETE':
            result = delete_feature(feat, cursor, conn)
        if operatie == 'UPDATE':
            result = delete_hulplijn(feat, cursor, conn)
        result = insert_into_log(feat, cursor, conn, layerName)
        result = clean_werkvoorraad(feat, cursor, conn, layerName)
    close_db_connection(cursor, conn)

def update_accepted(layerName, accept, cursor, conn):
    werkvTableName = PC.WERKVOORRAAD["tablelayertranslate"][layerName]
    query = "UPDATE mobiel.{} SET accepted = {}".format(werkvTableName, accept)
    cursor.execute(query)
    conn.commit()
    return 'succes'

def insert_into_log(feat, cursor, conn, layerName):
    werkvTableName = PC.WERKVOORRAAD["tablelayertranslate"][layerName]
    query = 'INSERT INTO mobiel.log_werkvoorraad (geom, record) \
                SELECT geom, row_to_json(w.*) FROM mobiel.{} w \
                WHERE id = {};'.format(werkvTableName, feat["id"])
    cursor.execute(query)
    conn.commit()
    return 'succes'

def delete_hulplijn(feat, cursor, conn):
    query = "DELETE FROM mobiel.werkvoorraad_hulplijnen \
             WHERE bron_id = {} AND brontabel = '{}';".format(feat['bron_id'], feat['brontabel'])
    cursor.execute(query)
    conn.commit()
    return 'succes'

def clean_werkvoorraad(feat, cursor, conn, layerName):
    werkvTableName = PC.WERKVOORRAAD["tablelayertranslate"][layerName]
    query = "DELETE FROM mobiel.{} WHERE id = {};".format(werkvTableName, feat["id"])
    cursor.execute(query)
    conn.commit()
    return 'succes'

def update_feature(feat, cursor, conn, layerName, bouwlaagOfObject, layerType):
    tableName = feat["brontabel"]
    query = 'UPDATE objecten.{} SET '.format(tableName)
    query += "geom = ST_GeomFromText('{}', 28992),".format(feat.geometry().asWkt())
    queryFields = layerFields[layerName]
    for field in queryFields:
        attr = field[0]
        attrType = field[1]
        if attrType == "type":
            if bouwlaagOfObject == 'Object':
                identifier = CH.get_identifier_by_tablename_ob(tableName)
            else:
                identifier = CH.get_identifier_by_tablename_bl(tableName)
            if identifier == 'soort':
                if layerType == 'Point':
                    query += " {}=(SELECT naam FROM objecten.{}_type t WHERE symbol_name = '{}'),".format(identifier, tableName, feat[attr])
                else:
                    query += " {}=(SELECT naam FROM objecten.{}_type t WHERE naam = '{}'),".format(identifier, tableName, feat[attr])
        else:
            if feat[attr]:
                if attrType == "string":
                    query += " {}='{}',".format(attr, feat[attr])
                elif attrType == "int":
                    query += ' {}={},'.format(attr, feat[attr])
    query = query[:-1] + ' WHERE id = {};'.format(feat["bron_id"])
    cursor.execute(query)
    conn.commit()
    return 'succes'

def insert_feature(feat, cursor, conn, layerName, bouwlaagOfObject, layerType):
    tableName = feat["brontabel"]
    attrQuery = []
    valueQuery = []
    attrQuery.append("geom")
    valueQuery.append("ST_GeomFromText('{}', 28992)".format(feat.geometry().asWkt()))
    for field in layerFields[layerName]:
        attr = field[0]
        attrType = field[1]
        if attrType == "type":
            if bouwlaagOfObject == 'Object':
                identifier = CH.get_identifier_by_tablename_ob(tableName)
            else:
                identifier = CH.get_identifier_by_tablename_bl(tableName)
            attrQuery.append('{}'.format(identifier))
            if identifier == 'soort':
                if layerType == 'Point':
                    valueQuery.append("(SELECT naam FROM objecten.{}_type t WHERE t.symbol_name = '{}')".format(tableName, feat[attr]))
                else:
                    valueQuery.append("(SELECT naam FROM objecten.{}_type t WHERE t.naam = '{}')".format(tableName, feat[attr]))
        else:
            if feat[attr]:
                attrQuery.append('{}'.format(attr))
                if attrType == "string":
                    valueQuery.append("'{}'".format(feat[attr]))
                elif attrType == "int":
                    valueQuery.append('{}'.format(feat[attr]))
    query = 'INSERT INTO objecten.{} ('.format(tableName) + ', '.join(attrQuery) + ') VALUES (' + ', '.join(valueQuery) + ');'
    cursor.execute(query)
    conn.commit()
    return 'succes'

def delete_feature(feat, cursor, conn):
    if feat['brontabel'] == 'alternatieve':
        query = "DELETE FROM bluswater.{} WHERE id={};".format(feat['brontabel'], feat['bron_id'])
    else:
        query = "DELETE FROM objecten.{} WHERE id={};".format(feat['brontabel'], feat['bron_id'])
    cursor.execute(query)
    conn.commit()
    return 'succes'

def temp_delete_feature(ilayer, ifeature, bouwlaagOfObject, rightLayerNames):
    if ilayer.name() in rightLayerNames:
        ids = []
        ids.append(ifeature.id())
        ilayer.selectByIds(ids)
        ilayer.startEditing()
        reply = MSG.showMsgBox('deleteobject_question')
        if not reply:
            ilayer.selectByIds([])
        elif reply:
            conn, cursor = setup_postgisdb_connection()
            if bouwlaagOfObject == 'Object':
                tableName = CH.get_tablename_ob(ilayer.name())
            else:
                tableName = CH.get_tablename_bl(ilayer.name())
            if tableName == 'alternatieve':
                query = "DELETE FROM bluswater.{} WHERE id={};".format(tableName, ifeature['id'])
            else:
                query = "DELETE FROM objecten.{} WHERE id={};".format(tableName, ifeature['id'])
            cursor.execute(query)
            conn.commit()
            close_db_connection(cursor, conn)
            ilayer.triggerRepaint()
        return "Done"
    else:
        reply = MSG.showMsgBox('noselectedtodelete')
        if reply:
            ilayer.selectByIds([])
            return "Done"
        return "Retry"

def temp_delete_feature_multi(ilayer, bouwlaagOfObject):
    conn, cursor = setup_postgisdb_connection()
    if bouwlaagOfObject == 'Object':
        tableName = CH.get_tablename_ob(ilayer.name())
    else:
        tableName = CH.get_tablename_bl(ilayer.name())
    for feat in ilayer.selectedFeatures():
        if tableName == 'alternatieve':
            query = "DELETE FROM bluswater.{} WHERE id={};".format(tableName, feat['id'])
        else:
            query = "DELETE FROM objecten.{} WHERE id={};".format(tableName, feat['id'])
        cursor.execute(query)
        conn.commit()
    close_db_connection(cursor, conn)
    ilayer.triggerRepaint()
    return "Done"
