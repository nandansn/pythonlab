import dbutils as dbutil
import cx_Oracle

def createTable(existingTableName, columnNames, tableName):
    createTableQuery = "create table {0} as select {1} from {2}"
    createTableQuery = createTableQuery.format(tableName,columnNames,existingTableName)
    print(createTableQuery)
    dbutil.executeDDL(createTableQuery)
    print('table created')

def dropTable(tableName):
    dropTableQuery = "drop table {0}"
    dropTableQuery = dropTableQuery.format(tableName)
    print(dropTableQuery)
    dbutil.executeDDL(dropTableQuery)
    print('table dropped from the schema...')

def truncateTable(tableName):
    truncateTableQuery = "truncate table {0}"
    truncateTableQuery = truncateTableQuery.format(tableName)
    print(truncateTableQuery)
    dbutil.executeDDL(truncateTableQuery)
    print('table data deleted...')

def dropTableColumns(tableName, columnNames):
    dropColumnQuery = "alter table {0} DROP ({1})"
    dropColumnQuery = dropColumnQuery.format(tableName,columnNames)
    print(dropColumnQuery)
    dbutil.executeDDL(dropColumnQuery)
    print('columns {0} dropped'.format(columnNames))

def addTableColumns(tableName, columnNameType):
    addColumnQuery = "alter table {0} ADD ({1})"
    addColumnQuery = addColumnQuery.format(tableName,columnNameType)
    print(addColumnQuery)
    dbutil.executeDDL(addColumnQuery)
    print('columns {0} added'.format(columnNameType))

def modifyTableColumns(tableName, columnNameType):
    modifyColumnQuery = "alter table {0} MODIFY ({1})"
    modifyColumnQuery = modifyColumnQuery.format(tableName,columnNameType)
    print(modifyColumnQuery)
    dbutil.executeDDL(modifyColumnQuery)
    print('columns {0} modified.'.format(columnNameType))

def describeTable(tableName):
    describeQuery = "select COLUMN_NAME,DATA_TYPE from user_tab_columns where table_name='{0}'".format(tableName)
    print(describeQuery)
    dbutil.executeDescribe(describeQuery)
    print('table description..')

def standardQuery(tableName, columnNames, whereCondition):
    pass

def customQuery(customQuery):
    pass