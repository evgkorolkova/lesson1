def format_price(price):
   price = int(price)
   price_text = "Цена:"
   price_currency = "руб."
   price_rub = "{} {} {}".format(price_text, price, price_currency)
   return price_rub
price_rub = format_price(56.24)
print(price_rub)

