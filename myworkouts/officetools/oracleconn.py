import cx_Oracle

dsn_tns = cx_Oracle.makedsn('slc12mqz.us.oracle.com', '18920', service_name='db9997.us.oracle.com') 
conn = cx_Oracle.Connection(user=r'DP_ORA_TGT_RST', password='welcome1', dsn=dsn_tns)

cx_Oracle.connect
 
c = conn.cursor()
c.execute('SELECT  column_name FROM USER_TAB_COLUMNS WHERE table_name = \'USER_OCS_TGT\' ' )
columnNames=''
for rows in c:
    print(rows[0])
    columnNames = columnNames +   rows[0] + ',' 

print(columnNames)

c.execute('SELECT  *  FROM USER_OCS_TGT' )
for r in c.fetchall():
    print(r)


conn.close()



