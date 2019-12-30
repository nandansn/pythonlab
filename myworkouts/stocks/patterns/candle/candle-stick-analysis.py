print('''
    1. Single.
    2. Multiple.
''')

mOption = input('Ente the option:')

if mOption == 1:
    pass
else:
    print('''
        1. Bullish Engulfing
        2. Bearish Engulfing
        3. Piercing
        4. Dark Cloud Cover
        5. Doji
    ''')
    multiPatternOption = input('What pattern you see ? Enter the option:')

    if multiPatternOption == 1:
        print('''
            You are seeing Bullish Engulfng pattern.
            Below are the rules:
                1. The prior trend should be a downtrend.
                2. The first day of the pattern (P1) should be a red candle reconfirming the bearishness in the market.
                3. The candle on the 2nd day of pattern (P2) should be a blue candle, long enough to engulf the red candle.

            Refer the file: Mutlipe Candle Stick Pattern - The Engulfing Pattern
        ''')
    
    elif multiPatternOption == 2:

        print('''
            You are seeing Bearish Engulfng pattern.
            Below are the rules:
                1. The prior trend should be a uptrend.
                2. The first day of the pattern (P1) should be a blue candle reconfirming the bullishness in the market.
                3. The candle on the 2nd day of pattern (P2) should be a red candle, long enough to engulf the blue candle.

            Refer the file: Mutlipe Candle Stick Pattern - The Engulfing Pattern
        ''')

    elif multiPatternOption == 3:
        print('''
            You are seeing Piercing pattern.
            Below are the rules:
                The piercing pattern is very similar to the bullish engulfing pattern with a very minor variation. 
		        In a bullish engulfing pattern the P2’s blue candle engulfs P1’s red candle completely. 
		        However in a piercing pattern P2’s blue candle partially engulfs P1’s red candle, however the engulfing should be between 50% and less than 100%. 
		        You can validate this visually or calculate the same. 

		        For example if P1’s range (Open – Close) is 12 , P2’s range should be at least 6 or higher but below 12.

            Refer the file: Mutlipe Candle Stick Pattern - The Engulfing Pattern
        ''')

    elif multiPatternOption == 4:
        print('''
            You are seeing Dark Cloud Cover pattern.
            Rules:
                The dark cloud cover is very similar to the bearish engulfing pattern with a minor variation. 
		        In a bearish engulfing pattern the red candle on P2 engulfs P1’s blue candle completely.
		        However in a dark cloud cover, the red candle on P2 engulfs about 50 to 100% of P1’s blue candle. 
		        The trade set up is exactly the same as the bearish engulfing pattern.
        ''')

    else:
        print('''
            You are seeing Doji pattern.
            Rules:
                1. An obvious uptrend as highlighted
		        2. A bearish engulfing pattern right at the top end of the upward rally
		        3. A doji formation on the day following P2
        ''')
