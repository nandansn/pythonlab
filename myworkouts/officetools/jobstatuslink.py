host=str(input("Host:"))
jobid=str(input("Job Id:"))
port=str(input("port:"))

link='http://host.us.oracle.com:port/dicloud/runtime/v1/jobs/jobid?expand=jobActions'

link=link.replace('host',host).replace('port',port).replace('jobid',jobid)

print(link)