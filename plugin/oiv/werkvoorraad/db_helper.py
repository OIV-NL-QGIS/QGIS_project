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
    query = 'SELECT bouwlaag FROM mobiel_sync.bouwlagen_binnen_object WHERE object_id = {};'.format(int(objectId))
    cursor.execute(query)
    bouwlaagTuple = cursor.fetchall()
    if bouwlaagTuple:
        bouwlagen = [tup["bouwlaag"] for tup in bouwlaagTuple]
    close_db_connection(cursor, conn)
    return bouwlagen

def check_object_mods(objectId):
    answer = False
    conn, cursor = setup_postgisdb_connection()
    query = "SELECT object_id FROM mobiel_sync.object_binnen_bouwlaag WHERE pand_id = '{}';".format(objectId)
    cursor.execute(query)
    objectTuple = cursor.fetchall()
    if objectTuple:
        answer = True
    close_db_connection(cursor, conn)
    return answer

def verwerk_werkvoorraad(werkvoorraadTable, werkvoorraad_id, accepted, conflict_actie=None):
    conn, cursor = setup_postgisdb_connection()
    try:
        query = """
            CALL mobiel_sync.verwerk_werkvoorraad(%s, %s, %s, %s);
        """
        cursor.execute(query, (werkvoorraadTable, werkvoorraad_id, accepted, conflict_actie))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        close_db_connection(cursor, conn)
