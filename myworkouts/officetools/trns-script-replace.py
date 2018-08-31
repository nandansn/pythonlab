import sys, os
print(os.path.dirname(os.path.abspath(sys.argv[0])))

f = open(os.path.dirname(os.path.abspath(sys.argv[0]))+'/script.txt','r')
message = str(f.read())
message = message.replace('\"','\\"')
message= message.replace('\n','')
message = "String transformScriptPayload = \"" + message + "\";"
print(message)
f.close()