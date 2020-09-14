"""Import dimension tables from the WFS en updat sqlite db"""
import os
import sqlite3
import time
import requests
from requests.auth import HTTPBasicAuth

def get_geoserver_conf(confPath):
    """get geoserver connection parametres"""
    geoserverURL = None
    geoserverBron = None
    filePath = os.path.join(os.path.dirname(__file__), confPath)
    try:
        with open(filePath, 'r') as f:
            x = f.read().splitlines()
        geoserverURL = "{}".format(x[0])
        userpass = HTTPBasicAuth(x[2], x[3])
        geoserverBron = x[1]
    except: # pylint: disable=bare-except
        print('Configfile not found or not complete!')
    return geoserverURL, geoserverBron, userpass

def setup_db_connection(dbrelPath):
    """setup the sqlite database connection"""
    conn = None
    cursor = None
    allTables = None
    try:
        db_path = os.path.join(os.path.dirname(__file__), dbrelPath)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        cursor.execute(query)
        allTables = cursor.fetchall()
    except sqlite3.Error as error:
        print("Failed to connect to the dimension database", error)
    return conn, cursor, allTables

def close_db_connection(cursor, conn):
    """when ready, close the sqlite database connection"""
    if cursor:
        cursor.close()
    if conn:
        conn.close()

def execute_update(geoserverURL, geoserverBron, cursor, allTables, auth):
    """update all the tables, insert extra rows and delete not existing"""
    for table in allTables:
        layerName = table[0]
        params = {'request' : 'GetFeature', 'outputFormat' : 'json', 'typename': '{}:{}'.format(geoserverBron, layerName)}
        try:
            r = requests.get(geoserverURL, params=params, auth=auth)
        except requests.exceptions.RequestException as e:
            print('The connection with GeoServer could not be established!', e)
            return 'not ok'
        if r.ok:
            try:
                query = 'SELECT id FROM {}'.format(layerName)
                idsTuple = cursor.execute(query).fetchall()
                ids = [tup[0] for tup in idsTuple]
                for feat in r.json()["features"]:
                    if "id" in feat["properties"].keys():
                        if feat["properties"]["id"] in ids:
                            for key in feat["properties"].keys():
                                if key != 'id':
                                    query = "UPDATE {} SET {} = '{}' WHERE id = {}"\
                                        .format(layerName, key, feat["properties"][key], feat["properties"]["id"])
                                    cursor.execute(query)
                            ids.remove(feat["properties"]["id"])
                        else:
                            columns = []
                            values = []
                            for key in feat["properties"].keys():
                                columns.append(key)
                                if isinstance(type(feat["properties"][key]), int):
                                    values.append(feat["properties"][key])
                                else:
                                    values.append("'{}'".format(feat["properties"][key]))
                            columnNames = ', '.join(columns)
                            valuesProp = ', '.join(map(str, values))
                            query = "INSERT INTO {} ({}) VALUES ({})".format(layerName, columnNames, valuesProp)
                            cursor.execute(query)
                    else:
                        print("Let op {} is niet ingelezen!".format(layerName))
                for remainingId in ids:
                    query = "DELETE FROM {} WHERE id = {}".format(layerName, remainingId)
                    cursor.execute(query)
            except sqlite3.Error as e:
                print("The {} table is corrupt!".format(layerName), e)
    return 'ok'

def run_update_dimension_tables():
    """execute all the real work"""
    print ('Start : ', time.ctime())
    result = None
    geoserverURL, geoserverBron, auth = get_geoserver_conf('geoserver.conf')
    conn, cursor, allTables = setup_db_connection('.\\db\\dimension_tables.db')
    if geoserverURL and geoserverBron and allTables:
        result = execute_update(geoserverURL, geoserverBron, cursor, allTables, auth)
    if result == 'ok':
        conn.commit()
        print('Dimension tables are correct updatet!')
    close_db_connection(cursor, conn)
    print('Stop : ', time.ctime())
