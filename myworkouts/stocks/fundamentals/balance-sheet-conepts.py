from colorama import init,deinit,Fore

init()

def currentAssets():
    print(Fore.YELLOW,'''
        Current assets include cash, cash equivalents, accounts receivable, stock inventory, marketable securities, 
        pre-paid liabilities, and other liquid assets.


        Current Assets = C + CE + I + AR + MS + PE + OLA
        where:
        C = Cash
        CE = Cash Equivalents
        I = Inventory
        AR = Accounts Receivable
        MS = Marketable Securities
        PE = Prepaid Expenses
        OLA = Other Liquid Assets
​	 
    ''')

def currentLiabilities():
    print(Fore.YELLOW,'''
        Current liabilities are a company's short-term financial obligations that are due within one year
        or within a normal operating cycle. An operating cycle is the time it takes a company to purchase 
        inventory and convert it to cash from sales. Current liabilities are the result of a company's operating 
        activities or day-to-day business operations.
    ''')

    