from binance.client import Client
from binance.enums import *
import logging

# Setup Logging
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=str(price)
                )
            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_STOP_MARKET,
                    stopPrice=str(stop_price),
                    quantity=quantity,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            elif order_type == 'STOP_LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_STOP,
                    stopPrice=str(stop_price),
                    price=str(price),
                    quantity=quantity,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            else:
                raise ValueError("Unsupported order type")

            logging.info(f"Order placed: {order}")
            print("✅ Order placed successfully!", order)

        except Exception as e:
            logging.error(f"Order failed: {e}")
            print("❌ Error placing order:", e)

    def grid_trade(self, symbol, base_price, gap_percent, num_orders, quantity, side):
        try:
            for i in range(num_orders):
                price = base_price * (1 + gap_percent / 100.0 * i) if side == 'SELL' else base_price * (1 - gap_percent / 100.0 * i)
                price = round(price, 2)
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=str(price)
                )
                logging.info(f"Grid order placed: {order}")
                print(f"✅ Grid order placed at {price}")
        except Exception as e:
            logging.error(f"Grid error: {e}")
            print("❌ Grid error:", e)