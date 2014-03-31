names = {}
prices = {}
exposure = {}



def AddName():
    stock_symbol = input('Enter Company Symbol: ')
    company_name = input('Enter Company Name: ')
    names[stock_symbol] =  company_name
    return stock_symbol



 
def AddPrices(stock_symbol):
    buy_price = float(input('Enter the Buy price: '))
    current_price = float(input('Enter the Current Price: '))
    

    prices[stock_symbol] = (buy_price, current_price)


def AddExposure(stock_symbol):
    risk = float(input('Enter the Risk: '))
    shares = float(input('Enter the number of Shares: '))

    exposure[stock_symbol] = (risk, shares)

def AddStock():
    stock_symbol = AddName()
    AddPrices(stock_symbol)
    AddExposure(stock_symbol)

def GetSale(stock_symbol):
    
    ESV = ((prices[stock_symbol][0]-prices[stock_symbol][1]) - exposure[stock_symbol][0]*prices[stock_symbol][0])*exposure[stock_symbol][1]

    return stock_symbol, ESV


def Main():
    print('1. Add Stock')
    print('2. Recommend Sale')
    print('3. Exit')
    menuChoice = 0

    while menuChoice != 3:
        menuChoice = int(input('What Would You Like To Do? '))
        if menuChoice == 1:
            menuChoice = 0
            AddStock()
        elif menuChoice == 2:
            menuChoice = 0
            GetSale()
        elif menuChoice != 3:
            Main()
