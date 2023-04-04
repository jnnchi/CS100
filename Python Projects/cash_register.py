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

class CashRegister:
  def __init__(self, item_list):
    self.__item_list = []

  def purchase_item(self, item):
    self.__item_list.append(item)

  def get_total(self, price):
    total = 0.0
    total = total + price
    return total

  def show_items(self):
    print("The items you have selected for purchase are: ")
    for item in self.__item_list:
      print(item.get_item_type().upper())
    
  def clear(self):
    self.__item_list = []

def main():
  item_list = []
  register = CashRegister(item_list)
  total = 0.0

  action = int(input("Would you like to purchase an item? Type 1 for yes and type 2 for no. "))
  while action == 1:
    name = str(input("\nWhat is the item's name? "))
    units = int(input("How many units of this item will you buy? "))
    price = float(input("What is the price of the item? "))
    print("\n")

    full_price = price * units
    total = total + register.get_total(full_price)

    item = RetailItem(name, units, price)
    register.purchase_item(item)
    action = int(input("Would you like to purchase an item? Type 1 for yes and type 2 for no. "))
  print("\nThank you for shopping with us!")
  register.show_items()
  print("\nYour total price is: " + str(total))
  register.clear()

main()
