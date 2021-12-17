import psycopg2
from configparser import ConfigParser
from psycopg2.extras import RealDictCursor
import qgis.core as QC
import oiv.helpers.constants as PC

layerFields = {
    "Werkvoorraad object - punt": [["object_id", "int"], ["rotatie", "string"], ["symbol_name", "type"], ["fotografie_id", "integer"]],
    "Werkvoorraad object - lijn": [["object_id", "int"], ["symbol_name", "type"], ["fotografie_id", "integer"]],
    "Werkvoorraad object - vlak": [["object_id", "int"], ["symbol_name", "type"], ["fotografie_id", "integer"]],
    "Werkvoorraad bouwlaag - punt": [["bouwlaag_id", "int"], ["rotatie", "string"], ["symbol_name", "type"], ["fotografie_id", "integer"]],
    "Werkvoorraad bouwlaag - lijn": [["bouwlaag_id", "int"], ["symbol_name", "type"], ["fotografie_id", "integer"]],
    "Werkvoorraad bouwlaag - vlak": [["bouwlaag_id", "int"], ["symbol_name", "type"], ["fotografie_id", "integer"]]
}
typeIdTable = ["dreiging", "ingang", "points_of_interest", "sleutelkluis", "veiligh_install", "veiligh_ruimtelijk"]

def setup_postgisdb_connection():
    """setup the postgis database connection"""
    conn = None
    cursor = None
    config = ConfigParser()
    filePath = QC.QgsProject.instance().readPath("./")
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
    #except:  # pylint: disable=bare-except
        #print("Failed to connect to the oiv database")
    return conn, cursor

def close_db_connection(cursor, conn):
    """when ready, close the sqlite database connection"""
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

def execute_queries(executableFeatures, ilayer, accept):
    conn, cursor = setup_postgisdb_connection()
    for arr in executableFeatures:
        feat = arr[0]
        ilayer = arr[1]
        layerName = ilayer.name()
        operatie = feat['operatie']
        update_accepted(layerName, accept, cursor, conn)
        if accept and operatie == 'INSERT':
            insert_feature(feat, cursor, layerName)
        if accept and operatie == 'UPDATE':
            update_feature(feat, cursor, layerName)
        if accept and operatie == 'DELETE':
            delete_feature(feat, cursor)
        if operatie == 'UPDATE':
            delete_hulplijn(feat, cursor)
        insert_into_log(feat, cursor, ilayer)
        clean_werkvoorraad(feat, cursor, ilayer)
        conn.commit()
    close_db_connection(cursor, conn)

def update_accepted(layerName, accept, cursor, conn):
    werkvTableName = PC.OBJECT["tablelayertranslate"][layerName]
    query = "UPDATE mobiel.{} SET accepted = {}".format(werkvTableName, accept)
    cursor.execute(query)
    conn.commit()

def insert_into_log(feat, cursor, ilayer):
    query = 'INSERT INTO mobiel.log_werkvoorraad (geom, record) \
                SELECT geom, row_to_json(w.*) FROM mobiel.werkvoorraad_punt w \
                WHERE id = {};'.format(feat["id"])
    cursor.execute(query)

def delete_hulplijn(feat, cursor):
    query = "DELETE FROM mobiel.werkvoorraad_hulplijnen WHERE bron_id = {} AND brontabel = '{}';".format(feat['bron_id'], feat['brontabel'])
    cursor.execute(query)

def clean_werkvoorraad(feat, cursor, ilayer):
    werkvTableName = PC.OBJECT["tablelayertranslate"][ilayer.name()]
    query = "DELETE FROM mobiel.{} WHERE id = {};".format(werkvTableName, feat["id"])
    cursor.execute(query)

def update_feature(feat, cursor, layerName):
    tableName = feat["brontabel"]
    query = 'UPDATE objecten.{} SET '.format(tableName)
    query += "geom = ST_GeomFromText('{}', 28992),".format(feat.geometry().asWkt())
    queryFields = layerFields[layerName]
    for field in queryFields:
        if field[1] == "string":
            query += " {}='{}',".format(field[0], feat[field[0]])
        elif field[1] == "integer":
            query += ' {}={},'.format(field[0], feat[field[0]])
        elif field[1] == "type":
            if tableName in typeIdTable:
                query += " {}_type_id=(SELECT t.id FROM objecten.{}_type t WHERE t.symbol_name = '{}'),".format(tableName, tableName, feat[field[0]])
    query = query[:-1]
    query += ' WHERE id = {};'.format(feat["bron_id"])
    print(query)

def insert_feature(feat, cursor, layerName):
    print('insert')
    get_bouwlagen(feat["object_id"])

def delete_feature(feat, cursor):
    query = "DELETE FROM objecten.{} WHERE id={};".format(feat['brontabel'], feat['bron_id'])
    cursor.execute(query)
