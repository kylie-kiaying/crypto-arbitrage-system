from data_collection.data_fetcher import fetch_prices
from arbitrage_detection.inter_exchange import detect_inter_exchange_arbitrage

def main():
    symbol = "BTC/USD"
    exchanges = ["binance", "kraken", "coinbase"]
    fees = {
        "binance": 0.1,  # 0.1%
        "kraken": 0.26,  # 0.26%
        "coinbase": 0.5  # 0.5%
    }

    # Fetch prices
    prices = fetch_prices(symbol, exchanges)
    print("Fetched Prices:")
    for exchange, price in prices.items():
        print(f"{exchange}: {price}")

    # Detect arbitrage opportunities
    arbitrage = detect_inter_exchange_arbitrage(prices, fees)
    if arbitrage["profit"] > 0:
        print("\nArbitrage Opportunity Detected:")
        print(f"Buy on {arbitrage['buy_exchange']} at {arbitrage['buy_price']}")
        print(f"Sell on {arbitrage['sell_exchange']} at {arbitrage['sell_price']}")
        print(f"Profit: {arbitrage['profit']}")
    else:
        print("\nNo arbitrage opportunity found.")

if __name__ == "__main__":
    main()