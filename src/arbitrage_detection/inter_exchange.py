from utils.logger import setup_logger

logger = setup_logger()

def detect_inter_exchange_arbitrage(prices, fees):
    logger.info("Detecting inter-exchange arbitrage opportunities")
    min_exchange = min(prices, key=prices.get)
    max_exchange = max(prices, key=prices.get)
    min_price = prices[min_exchange]
    max_price = prices[max_exchange]
    
    # Calculate total fees
    total_fees = (min_price * fees[min_exchange] / 100) + (max_price * fees[max_exchange] / 100)
    logger.info(f"Total fees: {total_fees}")
    
    # Calculate profit
    profit = max_price - min_price - total_fees
    logger.info(f"Profit: {profit}")
    
    if profit > 0:
        logger.info(f"Arbitrage opportunity detected: Buy on {min_exchange}, Sell on {max_exchange}, Profit: {profit}")
    else:
        logger.info("No arbitrage opportunity found")
    
    return {
        "buy_exchange": min_exchange,
        "sell_exchange": max_exchange,
        "buy_price": min_price,
        "sell_price": max_price,
        "profit": profit
    }