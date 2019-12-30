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
            
    @staticmethod
    def alter():
        print('''
                1. Drop columns
                2. Add columns
                3. Modify columns
         ''')
         
        alterOption = int(input('Enter alter option:'))
        tableName = str(input('Table name:'))  
        return tableName, alterOption

    @staticmethod
    def query():
        print('''
                1. Standard
                2. Custom
        ''')
        queryOption = int(input('Enter query option:'))
        tableName = str(input('Table name:'))

        return tableName, queryOption

    @staticmethod
    def menu():
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
        return option
        