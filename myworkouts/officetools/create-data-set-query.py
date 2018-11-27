import openpyxl

wb = openpyxl.load_workbook('C:\\Users\\nrangasa.ORADEV\\Downloads\\BenefitsCostSharing.csv\\Sample_Data_Set.xlsx')

wbSheet = wb.active

createTableQuery = ''' create table sample_source ( '''

for rowOfCellObjects in wbSheet['A1':'AF1']:
    for cellObj in rowOfCellObjects:
        createTableQuery = createTableQuery + cellObj.value + ' varchar2(30),'

createTableQuery = createTableQuery + ');'

print(createTableQuery)

