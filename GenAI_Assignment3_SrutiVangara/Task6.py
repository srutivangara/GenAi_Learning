def process_prices(prices):
    discounted_prices = list(map(lambda p:p-(p*0.10),prices))
    filtered_prices = list(filter(lambda d:d>300,discounted_prices))
    print("Discounted prices",discounted_prices)
    print("Filtered prices",filtered_prices)
process_prices([100,500,900,50,750])