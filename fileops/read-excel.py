from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook(filename='Txn2018.xlsx') #C:\\Users\\nrangasa.ORADEV\\Downloads\\
sheet_ranges = wb['OpTransactionHistory']
l=[]
item=''
sum=0

itemToFilter = input('Enter item to filter:')
itemToSearchInColumn = input('Item to search in column:')
startRange = input('Enter start range:')
endRange = input('Enter end range:')
txnType = str(input('Txt Type[C/D]:'))
txnDateColumn = input('Enter txn date column:')
print(txnType.upper())
if txnType == "C":
        creditColumn = str(input('Enter credit column:'))
else:
        debitColumn = str(input('Enter debit column:'))





     

for i in range(int(startRange),int(endRange),1):
    
    
    if itemToFilter in sheet_ranges[itemToSearchInColumn+str(i)].value:
        l.append(str(sheet_ranges[txnDateColumn+str(i)].value) + ":" 
        + str(sheet_ranges[itemToSearchInColumn+str(i)].value) + ":" + str(sheet_ranges[creditColumn+str(i)].value))
        if txnType.upper() == "C":

                try:
                        print(i)        
                        sum=sum+int(sheet_ranges[creditColumn+str(i)].value)
                except TypeError as typeInvalid:
                        print('No Credit value found. Check the transaction type.')
        elif txnType.upper() == "D":
                
                try:
                        sum=sum+int(sheet_ranges[debitColumn+str(i)].value)
                except TypeError as typeInvalid:
                        print('No Debit value found. Check the transction type.')
        else:
                print('You entered invalid type. Enter C or D')
                exit()
        


for i in l:
    print(i)
    
print('total:{}'.format(sum))