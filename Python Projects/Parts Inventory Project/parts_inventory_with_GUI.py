from tkinter import *

root = Tk()
root.geometry("1000x1000")

storage = {}

class Part:
    def __init__(self, sku, name, quantity, sales_price, cost_price):
        self.__sku = sku
        self.__name = name
        self.__quantity = quantity
        self.__sales_price = sales_price
        self.__cost_price = cost_price

    # mutators
    def set_sku(self, sku):
        self.__sku = sku

    def set_name(self, name):
        self.__name = name

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_sales_price(self, sales_price):
        self.__sales_price = sales_price

    def set_cost_price(self, cost_price):
        self.__cost_price = cost_price

    # accessors
    def get_sku(self):
        return self.__sku

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_sales_price(self):
        return self.__sales_price

    def get_cost_price(self):
        return self.__cost_price

    # methods
    def __str__(self):
        return ("SKU: " + str(self.get_sku()) + "\nName: " + self.get_name() + "\nQuantity: " + str(
            self.get_quantity()) + "\nSales Price: $" + str(self.get_sales_price()) + "\nCost Price: $" + str(
            self.get_cost_price()) + "\n")

part1 = Part(123, "HAT", 100, 14.99, 10.00)
part2 = Part(144, "SCARF", 50, 20.99, 17.00)
part3 = Part(222, "JACKET", 200, 40.50, 21.99)
part4 = Part(167, "PANTS", 99, 15.50, 4.99)
part5 = Part(241, "GLOVE", 108, 5.00, 2.50)
part_list = [part1, part2, part3, part4, part5]

class PartsInventory(Part):
    def __init__(self, sku, name, quantity, sales_price, cost_price, inventory):
        Part.__init__(self, sku, name, quantity, sales_price, cost_price)
        self.__inventory = inventory

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def get_inventory(self):
        return self.__inventory

    def __str__(self):
        return ("Your inventory is: " + str(self.get_inventory()))

    def load_inventory(self):
      for i in range(len(part_list)):
        part_sku = part_list[i].get_sku()
        self.__inventory[part_sku] = part_list[i]
      
    def print_inventory(self):
      forSale = Label(root, text = "These are the products \ncurrently for sale:\n").grid(row = 0, column = 1)
      item1 = Label(root, text = "%s" % self.__inventory[123]).grid(row = 1, column = 1)
      item2 = Label(root, text = "%s" % self.__inventory[144]).grid(row = 2, column = 1)
      item3 = Label(root, text = "%s" % self.__inventory[222]).grid(row = 3, column = 1)
      item4 = Label(root, text = "%s" % self.__inventory[167]).grid(row = 4, column = 1)
      item5 = Label(root, text = "%s" % self.__inventory[241]).grid(row = 5, column = 1)

    def sell_parts(self):
      self.print_inventory()
      item_to_buy = StringVar()
      num_of_items = StringVar()

      def get_receipt():
        sku = int(item_to_buy.get())
        reduced_qty = self.__inventory[sku].get_quantity() - int(num_of_items.get())
        self.__inventory[sku].set_quantity(reduced_qty)
        item_price = round(self.__inventory[sku].get_sales_price() * int(num_of_items.get()), 2)
        tax_price = round(item_price * 0.07, 2)
        receiptLabel = Label(root, text = "\nUSER RECEIPT:\nYou bought " + str(num_of_items.get()) + " units of " + self.__inventory[sku].get_name() + "\nEach unit cost: $" + str(self.__inventory[sku].get_sales_price()) + "\nYour price before tax is: $" + str(item_price) + "\nYour final price is $" + str(round(item_price + tax_price, 2))).grid(row = 3, column = 2)
        byeLabel = Label(root, text = "\nThank you for buying this item!\nPress \"Buy Items\" again to buy more, \nor press \"View Items\" again to see changes \nto your inventory!\nPress \"Exit\" to exit.").grid(row = 3, column = 3)

      purchase = Label(root, text = "Please type the SKU of\n the part you would like to buy.").grid(row = 0, column = 2)
      num = Label(root, text = "Please type the quantity\n you would like to buy.").grid(row = 1, column = 2)

      buy_entry = Entry(root, textvariable = item_to_buy).grid(row = 0, column = 3)
      num_entry = Entry(root, textvariable = num_of_items).grid(row = 1, column = 3)

      receiptButton = Button(root, text = "BUY!", command = get_receipt).grid(row = 2, column = 3)

inventory1 = PartsInventory(000, "create", 1, 2, 3, storage)
inventory1.load_inventory()

viewButton = Button(root, text = "View Items", command = inventory1.print_inventory).grid(row = 0, column = 0)
sellButton = Button(root, text = "Buy Items", command = inventory1.sell_parts).grid(row = 1, column = 0)
clearButton = Button(root, text = "Exit", command = root.destroy).grid(row = 2, column = 0)
