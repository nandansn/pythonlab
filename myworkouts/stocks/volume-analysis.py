from colorama import init, Fore, deinit

init()

def analyzeVolume():
    volumeFlag = input('Do the volume increase [Y/N] :')
    priceFlag = input('Do the price flag increase [Y/N]:')
    insitutionalBuying = input('Any insitutional buying [Y/N]:')
    insitutionalSelling = input('Any insitutional selling [Y/N]:')
    volumeAboveMA = input('Moving average line above the bars [Y/N]:')



    if volumeFlag == 'Y' and priceFlag == 'Y':
        print(Fore.GREEN,'Price Increase, Volume Increase: Bullish')

        if insitutionalBuying == 'Y':
            if volumeAboveMA == 'Y':
                print(Fore.GREEN,'Volume data indicates entry point now.')
            else:
                print(Fore.YELLOW, 'Check the data thorougly.')
        else:
            print(Fore.YELLOW,'Check for block deal thorougly.')

    elif priceFlag == 'Y' and volumeFlag == 'N':
        print(Fore.GREEN,'Price Increases, Volume Decreases: Caution – weak hands buying')

        if insitutionalBuying == 'N':
            if volumeAboveMA == 'N':
                print(Fore.RED,'''
                So what does an increase in price, associated by decreasing volumes indicate?
				It means the price is increasing because of a small retail participation and not really influential buying.
                Hence you need to be cautious as this could be a possible bull trap
                 
                 This is not the right time enter.
                  ''')
            else:
                print(Fore.RED,'''Seems to be false signal,
                1. Check the data
                2. Check the news
                3. Wait for few sessions.
                
                ''')
        else:
            print(Fore.YELLOW,'''
                1. Check the data properly.
            ''')

    elif volumeFlag == 'Y' and priceFlag == 'N':
        print(Fore.YELLOW,'Price Decreases, Volume Increases: Bearish')

        if volumeAboveMA == 'N' and insitutionalSelling == 'Y':
            print(Fore.YELLOW,'''
            Increase in volumes indicates the presence of smart money. Both events occurring together (decrease in price + increase in volumes)
            should imply that smart money is selling stocks.
            ''')

    elif volumeFlag == 'N' and priceFlag == 'N':
        print(Fore.YELLOW,'''
            Price Decreases, Volume Decreases: Caution – weak hands selling
        ''')
        if insitutionalSelling == 'N':
            if volumeAboveMA == 'N':
                print(Fore.RED,'''
                It means the price is decreasing because of small retail participation, and not really influential (read as smart money) selling.
                 Hence you need to be cautions as this could be a possible bear trap.
                ''')
            else:
                print(Fore.RED,'Check the data properly. Moving average indicates false signals.')
        
        else:
            print(Fore.RED,'Check the volume. Volume data gives wrong signals.')

    

