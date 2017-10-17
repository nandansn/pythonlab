import os

# getting current working directory
print (os.getcwd())

# list dir and files

print(os.listdir(os.getcwd()))

# make directory and create files

# os.remove('test-dir')

os.mkdir('test-dir')

# rename dir

os.rename('test-dir','test-dir-rn')

