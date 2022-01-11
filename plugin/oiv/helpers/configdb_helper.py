import os
import sqlite3

def read_settings(query, allResult):
    conn = None
    try:
        db_path = os.path.join(os.path.dirname(__file__), '..\\config_files\\configDB.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        if allResult:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
        cursor.close()
        return result
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if conn:
            conn.close()

def get_foreign_key_bl(layerName):
    query = "SELECT foreign_key FROM 'config_bouwlaag' WHERE child_layer = '{}'".format(layerName)
    return read_settings(query, False)[0]

def get_identifier_bl(layerName):
    query = "SELECT identifier FROM config_bouwlaag WHERE child_layer = '{}'".format(layerName)
    return read_settings(query, False)[0]

def get_parentlayer_bl(layerName):
    query = "SELECT parent_layer FROM config_bouwlaag WHERE child_layer = '{}'".format(layerName)
    return read_settings(query, False)[0]

def get_allkeys_bl(layerName):
    query = "SELECT foreign_key, identifier, input_label, rotatie FROM config_bouwlaag WHERE child_layer = '{}'".format(layerName)
    return read_settings(query, False)

def get_chidlayers_bl():
    query = "SELECT child_layer FROM config_bouwlaag;"
    return read_settings(query, True)

def get_foreign_key_ob(layerName):
    query = "SELECT foreign_key FROM 'config_object' WHERE child_layer = '{}'".format(layerName)
    return read_settings(query, False)[0]

def get_identifier_ob(layerName):
    query = "SELECT identifier FROM config_object WHERE child_layer = '{}'".format(layerName)
    return read_settings(query, False)[0]

def get_parentlayer_ob(layerName):
    query = "SELECT parent_layer FROM config_object WHERE child_layer = '{}'".format(layerName)
    return read_settings(query, False)[0]

def get_allkeys_ob(layerName):
    query = "SELECT foreign_key, input_label, question, label_required FROM config_object WHERE child_layer = '{}'".format(layerName)
    return read_settings(query, False)

def get_chidlayers_ob():
    query = "SELECT child_layer FROM config_object;"
    return read_settings(query, True)

def get_tablename_ob(layerName):
    query = "SELECT tablename FROM config_object WHERE child_layer = '{}';".format(layerName)
    return read_settings(query, False)[0]

def get_tablename_bl(layerName):
    query = "SELECT tablename FROM config_bouwlaag WHERE child_layer = '{}';".format(layerName)
    return read_settings(query, False)[0]

def get_identifier_by_tablename_ob(tableName):
    query = "SELECT identifier FROM config_object WHERE tablename = '{}';".format(tableName)
    return read_settings(query, False)[0]

def get_identifier_by_tablename_bl(tableName):
    query = "SELECT identifier FROM config_bouwlaag WHERE tablename = '{}';".format(tableName)
    return read_settings(query, False)[0]
