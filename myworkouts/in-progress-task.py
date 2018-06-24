tasks=open('C:\\Users\\nrangasa.ORADEV\\git\\myrepo\\pythonlab\\myworkouts\\myRunningTasks.txt','a+')

readUserTask = input('enter task name:')


tasks.write('\n'+readUserTask+'\n')

tasks.close()


