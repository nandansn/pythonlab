import cx_Oracle
import dbParser as db

db_tns = None
db_conn = None
cursor = None

def createConnection():
    global db_conn
    if db_conn == None:
        db_tns = cx_Oracle.makedsn(db.getHost(),db.getPort(),service_name=db.getServiceName())
        db_conn = cx_Oracle.connect(user=db.getUser(),password=db.getPassword(),dsn=db_tns)
    return db_conn.cursor()

def executeDDL(queryToExecute):
    global cursor 
    cursor = createConnection()
    try:
        cursor.execute(queryToExecute)
    except cx_Oracle.DatabaseError as dbError:
        print(dbError)

def executeDescribe(queryToExecute):
    cursor = createConnection()
    try:
        cursor.execute(queryToExecute)
        res = cursor.fetchall()
        
        for record in res:
            print('{0} ---- {1}'.format(record[0],record[1]))
    except cx_Oracle.DatabaseError as dbError:
        print(dbError)
 
def executeSelect(queryToExecute):
    cursor = createConnection()
    try:
        cursor.execute(queryToExecute)
        for column in cursor.description:
                print(column)
        
        res = cursor.fetchmany(3)
        
        for record in res:
            print(record)
    except cx_Oracle.DatabaseError as dbError:
        print(dbError)

def closeConnection():
    global db_conn
    if db_conn != None:
        cursor.close()
        db_conn.close()

