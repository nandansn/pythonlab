import openpyxl
import sys, os
print(os.path.dirname(os.path.abspath(sys.argv[0])))

def printBodyHeader():
    print('''Hi Satheesh,
Please find the weekly report,
    ''')

def printAccomplishments():
    print('''Top 3 accomplishments during the week (provide related Jira Task IDs and Confluence Page links)
    ''')

def printPrioritiesNxtWeek():
    print('''\nPriorities for next week
    ''')

def printTestData():
    print('''\nTest Data (Consolidated data for your module)
    a.Total Tests Automated Till Today :''')

def getTotalNumberOfTasks(sheet):
    totalNumberOfTasks = 0

    for i in range(2,1000):
        if (sheet['C'+str(i)].value == None):
            break
        else:
            #print(sheet['C'+str(i)].value)
            totalNumberOfTasks += 1
    return totalNumberOfTasks

def getCompletedTasks(numberOfTasks,sheet):
    completedTasks = []
    serialNumber = 0
    
    for i in range(2,numberOfTasks+1):
        if (sheet['D'+str(i)].value == 'Done'):
            serialNumber+=1
            taskDetails = str(serialNumber)+'''.Task Name:{0}\n  Task Type:{1}\n  Jira/Confluence Link:{2}\n  Comments:\n\t\t{3}'''.format(sheet['B'+str(i)].value,sheet['C'+str(i)].value,sheet['E'+str(i)].value,str(sheet['F'+str(i)].value).replace('\n','\n\t\t'))
            completedTasks.append(taskDetails)
    
    return completedTasks

def printCompletedTasks(completedTasks):
    for taskDetail in completedTasks:
        print(taskDetail)

def getInProgressOrYetToStartTasks(numberOfTasks,sheet):
    inProgressTasks =[]
    serialNumber = 0
    for i in range(2,numberOfTasks+1):
        if (sheet['D'+str(i)].value == 'In-Progress' or sheet['D'+str(i)].value == 'Yet-To-Start'):
            serialNumber+=1
            taskDetails = str(serialNumber)+'''.Task Name:{0}\n  Task Type:{1}\n  Jira/Confluence Link:{2}\n  Comments:\n\t\t{3}'''.format(sheet['B'+str(i)].value,sheet['C'+str(i)].value,sheet['E'+str(i)].value,str(sheet['F'+str(i)].value).replace('\n','\n\t\t'))
            inProgressTasks.append(taskDetails)
    
    return inProgressTasks

def printInProgressTasksOrYetToStart(progressTasks):
    for taskDetail in progressTasks:
        print(taskDetail)

def getAutomationData(automationSheet):
    uiNumbers = automationSheet['B2'].value
    restNumbers = automationSheet['C2'].value

    autoStatus ={'UI':uiNumbers,'REst':restNumbers}

    return autoStatus

def printAutomationData(automationData):
    print('''\t\t UI:'''+str(automationData.get('UI')))
    print('''\t\t REst:'''+str(automationData.get('REst')))

def getBugData():
    pass


wb = openpyxl.load_workbook('C:\\Users\\nrangasa.ORADEV\\Desktop\\Nanda-Tasks.xlsx')

sheet = wb.get_sheet_by_name('06-10Aug') # add logic to get the current week's status sheet.
automationSheet = wb.get_sheet_by_name('AutomationStatus')
numberOfTasks = getTotalNumberOfTasks(sheet)


printBodyHeader()
printAccomplishments()
printCompletedTasks(getCompletedTasks(numberOfTasks,sheet))
printPrioritiesNxtWeek()
printInProgressTasksOrYetToStart(getInProgressOrYetToStartTasks(numberOfTasks,sheet))
printTestData()
printAutomationData(getAutomationData(automationSheet))


reportFile = open(os.path.dirname(os.path.abspath(sys.argv[0]))+'\\report.txt','w')

reportFile.write('report')

reportFile.close()



