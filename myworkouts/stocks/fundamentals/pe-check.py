from colorama import init,deinit,Fore

def initialize():
    init()

def whatIsPe():
    print(Fore.YELLOW,'''

        What is P/E?
            The P/E of a stock is calculated by dividing the current stock price by the Earning Per share (EPS).
            The P/E ratio measures the willingness of the market participants to pay for the stock, 
            for every rupee of profit that the company generates. 
            For example if the P/E of a certain firm is 15, then it simply means that for every unit of profit the company earns, 
            the market participants are willing to pay 15 times. Higher the P/E, more expensive is the stock.

            Rules:
                1. P/E indicates how expensive or cheap the stock is trading at. Never buy stocks that are trading at high valuations. 
                I personally do not like to buy stocks that are trading beyond 25 or at the most 30 times its earnings, 
                irrespective of the company and the sector it belongs to
                2. The denominator in P/E ratio is the ‘Earnings’, and the earnings can be manipulated
                3. Make sure the company is not changing its accounting policy too often – this is one of the ways the company tries to manipulate its earnings.
                4. Pay attention to the way depreciation is treated. Provision for lesser depreciation can boost earnings
                5. If the company’s earnings are increasing but not its cash flows and sales, then clearly something is not right

                CASE STUDY

                    SJVN was listed at Rs.28 and was P/E of 7 in 2010 and today in 2015 it is Rs.24 at P/E of 6.5. 
                    In last 5 years it has made zero money for investors inspite of it being low P/E

                Moral: LOW P/E is not always cheap and good value.

                    United Breweries is P/E of 100 in 2010 was Rs.400 and is Rs.900 at P/E of 84. In spite of high P/E it has made money.

                Moral: HIGH P/E is not always expensive and bad!

    ''')



initialize()
whatIsPe()