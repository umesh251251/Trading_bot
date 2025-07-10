from basic_bot import BasicBot

def get_user_input():
    print("=== Binance Futures Trading Bot ===")
    api_key = input("Enter your API Key: ").strip()
    api_secret = input("Enter your API Secret: ").strip()
    bot = BasicBot(api_key, api_secret)

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()

    print("\nSelect Order Type:")
    print("1. MARKET")
    print("2. LIMIT")
    print("3. STOP_MARKET")
    print("4. STOP_LIMIT")
    print("5. GRID")
    order_type = input("Choice [1-5]: ").strip()

    if order_type == "5":
        base_price = float(input("Enter base price: "))
        gap_percent = float(input("Enter gap % between grid levels: "))
        num_orders = int(input("Enter number of grid levels: "))
        quantity = float(input("Enter quantity per order: "))
        bot.grid_trade(symbol, base_price, gap_percent, num_orders, quantity, side)
        return

    order_type_map = {
        "1": "MARKET",
        "2": "LIMIT",
        "3": "STOP_MARKET",
        "4": "STOP_LIMIT"
    }
    order_type = order_type_map.get(order_type)

    quantity = float(input("Enter quantity: "))
    price = stop_price = None

    if order_type == "LIMIT":
        price = float(input("Enter LIMIT price: "))
    elif order_type == "STOP_MARKET":
        stop_price = float(input("Enter STOP price: "))
    elif order_type == "STOP_LIMIT":
        stop_price = float(input("Enter STOP (trigger) price: "))
        price = float(input("Enter LIMIT (execution) price: "))

    bot.place_order(symbol, side, order_type, quantity, price, stop_price)

if __name__ == "__main__":
    get_user_input()