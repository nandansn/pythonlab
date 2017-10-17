import jenkins

server = jenkins.Jenkins('http://10.168.128.140:8080/', username='epam', password='epam')

print (server.get_views()[0]['url'])


#get the nodes
print (server.get_nodes())

for node in server.get_nodes():
    print('Name:'+str(node['name'])+'==> Status:'+str(node['offline']))


#print slave nodes
print('list of slave nodes offline')
for node in server.get_nodes():

    if node['name'] != 'master':
        if str(node['offline']) == 'True':
            print(node['name'])


#get jobs
print(server.get_running_builds())

print(server.get_whoami())

print(server.get_job_info('MI_Acquiring/BVT/01. Customer Portal - Acquiring STAGE-SA Env')['lastCompletedBuild'])

print(server.get_build_info('MI_Acquiring/BVT/01. Customer Portal - Acquiring STAGE-SA Env',39))


#get jobs search at diff levels
print(server.get_all_jobs())
