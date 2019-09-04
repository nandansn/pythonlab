from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook(filename='july.xlsx') #C:\\Users\\nrangasa.ORADEV\\Downloads\\
sheet_ranges = wb['Sheet 1']
l=[]
item=''
sum=0

itemToFilter = input('Enter item to filter:')
startRange = input('Enter start range:')
endRange = input('Enter end range:')
txnType = input('Txt Type[C/D]:')

     

for i in range(int(startRange),int(endRange),1):
    
    if itemToFilter in sheet_ranges['B'+str(i)].value:
        l.append(sheet_ranges['B'+str(i)].value)
        if txnType is "C":
                try:
                        sum=sum+int(sheet_ranges['F'+str(i)].value)
                except TypeError as typeInvalid:
                        print('No Credit value found. Check the transaction type.')
        elif txnType is "D":
                try:
                        sum=sum+int(sheet_ranges['E'+str(i)].value)
                except TypeError as typeInvalid:
                        print('No Debit value found. Check the transction type.')
        else:
                print('You entered invalid type. Enter C or D')
                exit()
        


for i in l:
    print(i)
    
print('total:{}'.format(sum))