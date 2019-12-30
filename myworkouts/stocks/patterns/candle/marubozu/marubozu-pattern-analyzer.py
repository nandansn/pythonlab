from colorama import init,deinit,Fore
from termcolor import colored
import configparser

init()

print(Fore.WHITE,'''
    Types of Marubozu:
        1. Bullish Marubozu
        2. Bearish Marubozu
''')


typeOfPatternYouSee = str(input('Type of marubozu pattern you see:'))

if typeOfPatternYouSee == '1':
    print(Fore.WHITE, '''
        Types Of Bullish Marubozu:
            1. White Marubozu
            2. Open White Marubozu
            3. Close White Marubozu
    ''')
    print(Fore.MAGENTA, '\t\tRule: Stock Open Price  = Stock Low Price And Stock High Price = Stock Close Price', Fore.WHITE )

    
    typeOfBullishMarubozuYouSee = str(input('\t\nType bullish marubozu you see:'))

    

    if (typeOfBullishMarubozuYouSee == '1'):
        openPrice = eval(input('\tOpen Price:'))
        lowPrice = eval(input('\tLow Price:'))
        closePrice = eval(input('\tClose Price:'))
        highPrice = eval(input('\tHigh Price:'))
        
        if openPrice == lowPrice and closePrice == highPrice:
            print(Fore.GREEN,'\n\t\t Info:This is White marubozu. Confirmed')
            fileHandle = open('white-marubozu-rules.txt', 'r')
            print('\n')
            for line in fileHandle:
                print(Fore.LIGHTMAGENTA_EX,'\t',line) # prints the first fields value
            fileHandle.close()

        else:
            print(Fore.YELLOW,'\t\tWarning: This is not white marubozu, cross check')
