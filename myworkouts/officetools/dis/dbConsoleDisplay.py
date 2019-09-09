class Display:
    
    @staticmethod
    def create():
        print('''
        Create table from existing table or new table?
            1. From existing table.
            2. New table
        ''')
        createOption = int(input('Enter create table option: '))

        if createOption == 1:
            existingTableName = str(input('Enter existing table name:'))
            columnNames = str(input('Enter column names seperated by comma:'))  
            tableName = str(input('Table name:'))  
            return existingTableName, columnNames, tableName