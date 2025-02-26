from .api_client import APIClient

def fetch_prices(symbol, exchanges):
    """
    Fetch prices for a given symbol from multiple exchanges.
    """
    prices = {}
    for exchange in exchanges:
        client = APIClient(exchange)
        price = client.fetch_price(symbol)
        prices[exchange] = price
    return prices