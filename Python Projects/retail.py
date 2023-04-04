class RetailItem:
  def __init__(self, item_type, units, price):
    self.__item_type = item_type
    self.__units = units
    self.__price = price

  def set_item_type(self, item_type):
    self.__item_type = item_type

  def set_units(self, units):
    self.__units = units

  def set_price(self, price):
    self.__price = price

  def get_item_type(self):
    return self.__item_type

  def get_units(self):
    return self.__units

  def get_price(self):
    return self.__price

def main():
  item1 = RetailItem("Jacket", 12, 59.95)
  item2 = RetailItem("Designer Jeans", 40, 34.95)
  item3 = RetailItem("Shirt", 20, 24.95)

  print("ITEM #1:\n  It is a " + item1.get_item_type() + "\n  It has " + format(item1.get_units()) + " units" + "\n  Its price is: " + format(item1.get_price()))

  print("ITEM #2:\n  It is a " + item2.get_item_type() + "\n  It has " + format(item2.get_units()) + " units" + "\n  Its price is: " + format(item2.get_price()))

  print("ITEM #3:\n  It is a " + item3.get_item_type() + "\n  It has " + format(item3.get_units()) + " units" + "\n  Its price is: " + format(item3.get_price()))

main()
