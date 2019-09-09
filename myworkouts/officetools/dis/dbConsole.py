import dbOperations as dbOps
import dbutils as dbu
from dbConsoleDisplay import Display


connection = True

while (connection):
    print('''
    1. Create table
    2. Drop table
    3. Truncate table
    4. Drop columns
    5. Describe table
    6. Alter table
    7. Query Records
    0. Exit
    ''')


    option = int(input('Enter option:'))    

    
    if option == 1 :
        existingTableName, columnNames, tableName = Display.create()
        dbOps.createTable(existingTableName, columnNames, tableName)
    elif option == 2:
        tableName = str(input('Table name:'))  
        dbOps.dropTable(tableName)
    elif option == 3:
        tableName = str(input('Table name:'))  
        dbOps.truncateTable(tableName)
    elif option == 4:
        tableName = str(input('Table name:'))  
        columnNames = str(input('Enter column names seperated by comma:'))  
        dbOps.dropTableColumns(tableName,columnNames)
    elif option == 5:
        tableName = str(input('Table name:'))  
        dbOps.describeTable(tableName)
    elif option == 6:
        print('''
                1. Drop columns
                2. Add columns
                3. Modify columns
         ''')
         
        alterOption = int(input('Enter alter option:'))
        tableName = str(input('Table name:'))  
        if alterOption == 1:
            columnNames = str(input('Enter column names, seperated by comma:'))
            dbOps.dropTableColumns(tableName,columnNames)      
        if alterOption == 2:
            columnNameType = str(input('Enter column name and type[like: Name varchar2(100), Age number], seperated by comma:'))
            dbOps.addTableColumns(tableName,columnNameType)
        if alterOption == 3:
            columnNameType = str(input('Enter column name and type[like: Name varchar2(100), Age number], seperated by comma:'))
            dbOps.modifyTableColumns(tableName,columnNameType)

    elif option == 7:
        print('''
                1. Standard
                2. Custom
        ''')
        queryOption = int(input('Enter query option:'))
        tableName = str(input('Table name:'))
        if queryOption == 1 :
            columnNames = str(input('Enter column names seperated by comma:'))
            condition = str (input('Enter simple where condition:'))
            # call standard query 
            # display the result
        if queryOption == 2:
            customQuery = str(input('Enter custom query:'))
            # call custom query 
            # display the result
    elif option == 0:
        connection = False
        dbu.closeConnection()
        pass



