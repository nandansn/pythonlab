print(""" ######################## Job Status Link ##################### 
            Enter Host Name, Port and Job Id
            
""")

host=str(input("\tHost:"))
port=str(input("\tport:"))
jobid=str(input("\tJob Id:"))

link='http://host.us.oracle.com:port/dicloud/runtime/v1/jobs/jobid?expand=jobActions'

link=link.replace('host',host).replace('port',port).replace('jobid',jobid)

print("\tJob Status Link:",link)

print ("""\n ################################################################""")