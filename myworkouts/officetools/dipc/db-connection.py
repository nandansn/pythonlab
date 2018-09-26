#references : parsing the property file: https://wiki.python.org/moin/ConfigParserExamples
#ref: get the directory path, https://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python
#ref: oracle connection https://stackoverflow.com/questions/3521692/how-can-i-access-oracle-from-python
#ref: my sql connection https://stackoverflow.com/questions/12072961/how-to-connect-to-mysql-database-from-python-using-connection-string


import configparser
import os
import cx_Oracle
config = configparser.RawConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__))+'\\test.properties')

print(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())
dbHost=config.get('SOURCE_DB_CONFIG','source.db.host')
dbHostPort=config.get('SOURCE_DB_CONFIG','source.db.port')
dbUserName=config.get('SOURCE_DB_CONFIG','source.db.username')
dbUserPwd=config.get('SOURCE_DB_CONFIG','source.db.password')
dbServiceId=config.get('SOURCE_DB_CONFIG','source.db.sid')

print(dbHost,dbHostPort,dbUserName,dbUserPwd,dbServiceId)
connectionString = dbHost + ':' + dbHostPort + '/' + dbServiceId

connectionString = 'DICS_stage/'+dbUserPwd+'@' + dbHost +':'+dbHostPort+'/db3030.us.oracle.com'

P
print(connectionString)
connection  = cx_Oracle.connect(u''+connectionString)

print(id(connection))

sqlQueryCursor = connection.cursor()

sqlQueryCursor.execute('select * from SAMPLE_31082018020102')

res = sqlQueryCursor.fetchall()

for data in res:
    print (data)

connection.close()

