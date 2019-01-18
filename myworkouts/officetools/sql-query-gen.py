import xlrd

location = "C:\\Users\\nrangasa.ORADEV\\official\\projects\\mapping\\mapping\\data_model_template.xls"

wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0) 

def createTableQuery():
    sheet = wb.sheet_by_index(0) 
    print("""CREATE TABLE INDIVIDUALS (
    """)
    for i in range(1,sheet.nrows -1):
        print("\t\t{} {},".format(sheet.cell_value(i, 0),sheet.cell_value(i, 1)))

    print("\t\t{} {}".format(sheet.cell_value(sheet.nrows-1, 0),sheet.cell_value(sheet.nrows-1, 1)))
    print(""");""")

def insertValuesQuery():
    sheet = wb.sheet_by_index(1) 
    print("""INSERT INTO INDIVIDUALS (""")
    colNames=""
    for i in range(0,sheet.ncols -1):
        colNames = colNames + "{},".format(sheet.cell_value(1, i))
    colNames = colNames+"{}".format(sheet.cell_value(1, sheet.ncols -1))+")"
    colValues=" values ("
    for i in range(0,sheet.ncols -1):
        
        if str(sheet.cell_value(0, i)).startswith('NUMBER') or str(sheet.cell_value(0, i)).startswith('Number'):
            colValues = colValues + "{},".format(str(sheet.cell_value(2, i)))
        else:
            colValues = colValues + "'{}',".format(str(sheet.cell_value(2, i)))
    if str(sheet.cell_value(0, sheet.ncols -1)).startswith('Number'):
        colValues =colValues+"{}".format(str(sheet.cell_value(2, sheet.ncols -1)))+")"
    else:
        colValues =colValues+"'{}'".format(str(sheet.cell_value(2, sheet.ncols -1)))+")"
    print(colNames+colValues)

insertValuesQuery()


