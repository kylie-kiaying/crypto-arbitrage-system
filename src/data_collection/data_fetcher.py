from utils.logger import setup_logger
from data_collection.api_client import APIClient

logger = setup_logger()

def fetch_prices(symbol, exchanges):
    logger.info(f"Fetching prices for {symbol} from {exchanges}")
    
    prices = {}
    for exchange in exchanges:
        client = APIClient(exchange)
        price = client.fetch_price(symbol)
        prices[exchange] = price
    logger.info("Prices fetched successfully")
    
    ## Mock prices for testing
    # prices = {
    #     "binance": 85000.0,
    #     "kraken": 85500.0,
    #     "coinbase": 86000.0
    # }
    return prices