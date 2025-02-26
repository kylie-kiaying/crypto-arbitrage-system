import ccxt

class APIClient:
    def __init__(self, exchange_name):
        """
        Initialize the API client for a specific exchange.
        """
        self.exchange = getattr(ccxt, exchange_name)()

    def fetch_price(self, symbol):
        """
        Fetch the latest price for a given trading pair.
        """
        ticker = self.exchange.fetch_ticker(symbol)
        return ticker['last']