import tkinter as tk
from basic_bot import BasicBot

def place_order():
    symbol = symbol_entry.get()
    side = side_var.get()
    order_type = order_type_var.get()
    quantity = float(quantity_entry.get())
    price = price_entry.get()
    stop_price = stop_price_entry.get()

    bot = BasicBot(api_key_entry.get(), api_secret_entry.get())
    bot.place_order(symbol, side, order_type, quantity,
                    float(price) if price else None,
                    float(stop_price) if stop_price else None)

root = tk.Tk()
root.title("Binance Futures Trading Bot")

fields = ["API Key", "API Secret", "Symbol", "Quantity", "Price", "Stop Price"]
entries = {}

for field in fields:
    tk.Label(root, text=field).pack()
    entry = tk.Entry(root)
    entry.pack()
    entries[field] = entry

api_key_entry = entries["API Key"]
api_secret_entry = entries["API Secret"]
symbol_entry = entries["Symbol"]
quantity_entry = entries["Quantity"]
price_entry = entries["Price"]
stop_price_entry = entries["Stop Price"]

side_var = tk.StringVar(value="BUY")
tk.Label(root, text="Side").pack()
tk.OptionMenu(root, side_var, "BUY", "SELL").pack()

order_type_var = tk.StringVar(value="MARKET")
tk.Label(root, text="Order Type").pack()
tk.OptionMenu(root, order_type_var, "MARKET", "LIMIT", "STOP_MARKET", "STOP_LIMIT").pack()

tk.Button(root, text="Place Order", command=place_order).pack()

root.mainloop()