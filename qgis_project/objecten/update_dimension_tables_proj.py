"""Import dimension tables from the WFS en updat sqlite db"""
import os
import sqlite3
import json
import time
import requests
import psycopg2
from configparser import ConfigParser
from qgis.core import QgsProject, QgsGeometry, QgsVectorLayer
from psycopg2.extras import RealDictCursor


def get_geoserver_conf(confPath):
    """get geoserver connection parametres"""
    geoserverURL = None
    geoserverBron = None
    auth = None
    filePath = os.path.join(os.path.dirname(__file__), confPath)
    try:
        with open(filePath, 'r') as f:
            x = f.read().splitlines()
        geoserverURL = "{}".format(x[0])
        auth = (x[2], x[3])
        geoserverBron = x[1]
    except:  # pylint: disable=bare-except
        print('Configfile not found or not complete!')
    return geoserverURL, geoserverBron, auth


def setup_sqlitedb_connection(dbrelPath, isProject):
    """setup the sqlite database connection"""
    conn = None
    cursor = None
    allTables = None
    try:
        if isProject:
            db_path = dbrelPath
        else:
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


def execute_update_by_wfs(geoserverURL, geoserverBron, cursor, allTables, auth, conn):
    """update all the tables, insert extra rows and delete not existing"""
    for table in allTables:
        layerName = table[0]
        params = {'request': 'GetFeature', 'outputFormat': 'json', 'typename': '{}:{}'.format(geoserverBron, layerName)}
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
                                    conn.commit()
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
                            conn.commit()
                    else:
                        print("Let op {} is niet ingelezen!".format(layerName))
                for remainingId in ids:
                    query = "DELETE FROM {} WHERE id = {}".format(layerName, remainingId)
                    cursor.execute(query)
            except sqlite3.Error as e:
                print("The {} table is corrupt!".format(layerName), e)
    return 'ok'


def setup_postgisdb_connection(service):
    """setup the postgis database connection"""
    conn = None
    cursor = None
    try:
        config = ConfigParser()
        fileName = os.path.join(os.path.dirname(__file__), 'pg_service.conf')
        with open(fileName, 'rb') as f:
            config.read_file(f)
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


def execute_update_by_db(cursorOIV, cursor, allTables, conn):
    """update all the tables, insert extra rows and delete not existing"""
    for table in allTables:
        tableCheck = True
        layerName = table[0]
        query = "SELECT table_schema FROM information_schema.tables WHERE table_name = '{}'".format(layerName)
        cursorOIV.execute(query)
        checkSchema = cursorOIV.fetchone()
        if checkSchema:
            schema = checkSchema["table_schema"]
            if schema in ['algemeen', 'bluswater', 'objecten']:
                query = "SELECT * FROM {}.{}".format(schema, layerName)
                cursorOIV.execute(query)
                allRecords = cursorOIV.fetchall()
            else:
                tableCheck = False
        else:
            tableCheck = False
        if tableCheck:
            try:
                query = 'SELECT id FROM {}'.format(layerName)
                idsTuple = cursor.execute(query).fetchall()
                ids = [tup[0] for tup in idsTuple]
                for record in allRecords:
                    if "id" in record.keys():
                        if record["id"] in ids:
                            for key in record.keys():
                                if key != 'id':
                                    query = "UPDATE {} SET {} = '{}' WHERE id = {}"\
                                        .format(layerName, key, record[key], record["id"])
                                    cursor.execute(query)
                                    conn.commit()
                            ids.remove(record["id"])
                        else:
                            columns = []
                            values = []
                            for key in record.keys():
                                columns.append(key)
                                if isinstance(type(record[key]), int):
                                    values.append(record[key])
                                else:
                                    values.append("'{}'".format(record[key]))
                            columnNames = ', '.join(columns)
                            valuesProp = ', '.join(map(str, values))
                            query = "INSERT INTO {} ({}) VALUES ({})".format(layerName, columnNames, valuesProp)
                            cursor.execute(query)
                            conn.commit()
                    else:
                        print("Let op {} is niet ingelezen!".format(layerName))
                for remainingId in ids:
                    query = "DELETE FROM {} WHERE id = {}".format(layerName, remainingId)
                    cursor.execute(query)
            except:  # pylint: disable=bare-except
                print("The {} table is corrupt!".format(layerName))
    return 'ok'


def getlayer_byname(layername):
    layer = None
    layers = QgsProject.instance().mapLayersByName(layername)
    layer = layers[0]
    return (layer)


def run_update_dimension_tables(confFile, dbFile, isProjectDb, connectType):
    """execute all the update work"""
    print('Start: ', time.ctime())
    result = None
    connOIV = None
    cursorOIV = None
    conn, cursor, allTables = setup_sqlitedb_connection(dbFile, isProjectDb)
    if connectType == 'WFS':
        geoserverURL, geoserverBron, auth = get_geoserver_conf(confFile)
        result = execute_update_by_wfs(geoserverURL, geoserverBron, cursor, allTables, auth, conn)
        close_db_connection(cursor, conn)
    else:
        connOIV, cursorOIV = setup_postgisdb_connection("service='oiv'")
        if cursorOIV:
            result = execute_update_by_db(cursorOIV, cursor, allTables, conn)
            close_db_connection(cursorOIV, connOIV)
    if result == 'ok':
        print('Dimension tables are correct updatet!')
    print('Stop : ', time.ctime())
