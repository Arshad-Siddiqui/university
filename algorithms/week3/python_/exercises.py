# Exercise 1

def order_price(kilos):
  subtotal = kilos * 3
  if subtotal > 50:
    subtotal -= 1.50

  return int((subtotal + 4.99) * 100) 