import subprocess
from os import system
from dbtb import *


executionDirPath =''
options = ['1. Prepare','2. Deploy', '3. Exit  ']
hostName =''
buildVersion =''
userName =''
password =''

toolTitle = " DBTB Prepare and Deploy "

system('cls')


print(toolTitle.center(100,'*'))
print('\n')

for option in options:
    print(option.center(100,' '))

print('\n')
optionNumber = input('\tEnter option number:')

if int(optionNumber) in [1,2]:
    hostName,buildVersion,userName,password = get_data()
    
else:
    print('\n')
    print('Choosen option {option} System exiting...'.format(option=optionNumber).center(45))



result = []
errcode=''
#process =subprocess.call('C:\\Users\\nrangasa.ORADEV\\git\\latestpremaster\\dicloud\\Source\\dicloud-test\\dbtb\\target\\appassembler\\bin\\dbtb.bat deploy -h slc14vqd.us.oracle.com -v 18.4.3.0.0-1809270306 -u nrangasa -p Mathi0363',shell=True)
#process =subprocess.call('dir',shell=True)

#print(process)