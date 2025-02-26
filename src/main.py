from data_collection.data_fetcher import fetch_prices

def main():
    symbol = "BTC/USD"
    exchanges = ["binance", "kraken", "coinbase"]
    prices = fetch_prices(symbol, exchanges)
    print("Fetched Prices:")
    for exchange, price in prices.items():
        print(f"{exchange}: {price}")

if __name__ == "__main__":
    main()