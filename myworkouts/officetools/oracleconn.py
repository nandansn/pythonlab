import cx_Oracle

dsn_tns = cx_Oracle.makedsn('slc06ptr.us.oracle.com', '14190', service_name='db2473.us.oracle.com') 
conn = cx_Oracle.Connection(user=r'DICS_repo', password='welcome1', dsn=dsn_tns)

cx_Oracle.connect
 
c = conn.cursor()
c.execute('select * from database.table')

for rows in c:
    print(rows[0])



