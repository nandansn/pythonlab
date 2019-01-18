def rentCalc(rent=0,years=0,increment=0):
    totalRent=0
    fromYearOne=1
    prevYearRent = 0
    for i in range(fromYearOne,years):
        if (i == 1):
                prevYearRent = prevYearRent + (12 * rent)
                print('Rent for the year {} is {}:',i,prevYearRent)
                totalRent = prevYearRent
        else:
            prevYearRent = prevYearRent + (prevYearRent * (increment /100))
            print('Rent for the year {} is {}:',i,prevYearRent)
            totalRent = totalRent + prevYearRent
    print('Total rent for {} years is {}',years,totalRent)

rent = int(input('Enter rent:'))
years = int(input('Enter years:'))
increment = int(input('Enter increment:'))

rentCalc(rent,years,increment)


        
        



