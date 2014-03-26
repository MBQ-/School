# The first dictionary, called Names, maps the
# stock symbol to the company name (example: "GM" maps to "General Motors").

# The second dictionary, called Prices, maps the stock symbol to a
# list of 2 floating point numbers corresponding to the buy price
# (the price the user paid for the stock) and the current market price (the price the user could sell the stock for today).

# The third dictionary,
# called Exposure, maps the stock symbol to a list of 2 floating point numbers,
# corresponding to the number of shares purchased, and the risk associated with
# holding onto the stock (i.e. How likely the stock is to gain value in the future).

Exposure = ()

# AddName - Asks the user for a Stock Symbol and Name pairing
# then adds it to the Names dictionary

def AddName():
    
    # Ask user for Stock Symbol
    stock_symbol = input(" Enter Stock Symbol: ")

    # Ask user for the Company Name
    company_name = input("Enter the Company Name: ")

    # Add this key/value pair to Names dictionary
    Names(stock_symbol) = company_name

    return stock_symbol

# AddPrices - takes a Stock Symbol as an input parameter,
# then asks the user for the Buy price and the Current price
# of the corresponding stock, adding them to the Prices dictionary

def AddPrices(stock_symbol):
    
    # Asks the user for the Buy Price    
    buy_price = float(input("Enter the Buy price: "))

    # Asks the user for the Current Price    
    current_price = float(input("Enter the Current Price: "))

    # Adding them to the Prices dictionary  
    Prices(stock_symbol) = (buy_price, current_price)

# AddExposure - Takes a Stock Symbol as an input parameter,
# then asks the user for the Risk and Shares of the
# corresponding stock, adding them to the Exposure dictionary.

def AddExposure(stock_symbol):

    # Asks the user for the Risk
    risk - float(input("Enter the Risk: ")

    # Asks the user for the Shares
    number_of_shares = float(input("Enter the number of Shares: ")

    #Adding them to the Exposure dictionary
    Exposure(stock_symbol) = (risk,  number_of_shares)

# AddStock - Calls AddName, AddPrices, and AddExposure
# to add a new stock to the portfolio.

def AddStock(stock_symbol):
    AddName()
    AddPrices()
    
    

# GetSale - Finds the maximum expected value of selling a stock.
# The expected sale value of a stock is the current profit minus
# the future value of the stock:


