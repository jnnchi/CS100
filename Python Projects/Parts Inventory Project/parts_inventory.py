from consolemenu import *
from consolemenu.items import *
import time
import pickle

storage = {}
profit_list = {}
sold_qty = {}

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
            self.get_cost_price()))


class PartsInventory(Part):
    def __init__(self, sku, name, quantity, sales_price, cost_price, inventory, profit_list, sold_qty):
        Part.__init__(self, sku, name, quantity, sales_price, cost_price)
        self.__inventory = inventory
        self.__profit_list = profit_list
        self.__sold_qty = sold_qty

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def get_inventory(self):
        return self.__inventory

    def set_profit_list(self, profit_list):
        self.__profit_list = profit_list

    def get_profit_list(self):
        return self.__profit_list

    def set_sold_qty(self, sold_qty):
        self.__sold_qty = sold_qty

    def get_sold_qty(self):
        return self.__sold_qty

    def __str__(self):
        return ("Your inventory is: " + str(self.get_inventory()))

    def print_inventory(self):
        for key in self.__inventory.keys():
            print("\nITEM:")
            print(self.__inventory[key])

    def sum_profit(self):
        return sum(self.__profit_list.values())

    def add_parts(self):
        print("This is your current inventory: ")
        self.print_inventory()
        num = int(input("How many parts would you like to add? "))
        for i in range(num):
            part_sku = int(input("\nWhat is the SKU of this part? "))
            part_name = str(input("What is the name of this part? ")).upper()
            part_quantity = int(input("What is the quantity of this part? "))
            part_sales_price = float(input("What is the sales price of this part? "))
            part_cost_price = float(input("What is the cost price of this part? "))

            self.__inventory[part_sku] = Part(part_sku, part_name, part_quantity, part_sales_price, part_cost_price)

        print("This is your updated inventory: ")
        self.print_inventory()
        time.sleep(5)

    def remove_parts(self):
        print("Here is your current inventory:")
        self.print_inventory()
        remove_sku = int(input("What is the SKU of the part you need to delete? "))
        del self.__inventory[remove_sku]
        print("Here is your updated inventory:")
        self.print_inventory()
        time.sleep(5)

    def change_qty(self):
        print("Here is your current inventory:")
        self.print_inventory()
        change_sku = int(input("What is the SKU of the part you want to increase the quantity of? "))
        new_quantity = int(input("What is the new quantity of the item? "))
        self.__inventory[change_sku].set_quantity(new_quantity)
        print("Here is your updated inventory:")
        self.print_inventory()
        time.sleep(5)

    def report_inventory(self):
        print("Here is your inventory report: ")
        print("You currently have " + str(len(self.__inventory)) + " items in your inventory.")
        self.print_inventory()
        time.sleep(10)

    def report_revenue(self):
        for key in self.__profit_list.keys():
            print("From selling " + str(self.__sold_qty[key]) + " UNITS of the ITEM: " + self.__inventory[
                key].get_name() + ", you gained the PROFIT of: $" + str(self.__profit_list[key]))
        print("The total revenue you have currently gained: $" + str(self.sum_profit()))
        time.sleep(10)

    def sell_parts(self):
        print("These are the items currently for sale:")
        self.print_inventory()

        total_price = 0
        num_to_buy = int(input(
            "\nHow many (different kinds of) items would your customer like to buy? For example, if they want to buy ten hats and a scarf, type 2. "))
        item_list = []
        qty_list = []
        for i in range(num_to_buy):
            item_to_buy = int(
                input("\nWhich item would your customer now like to buy? Please type the SKU (numbers only). "))
            qty_to_buy = int(input("How many of this item would your customer like to buy? "))

            # updates the quantity in the inventory
            reduced_qty = self.__inventory[item_to_buy].get_quantity() - qty_to_buy
            self.__inventory[item_to_buy].set_quantity(reduced_qty)

            # sales price
            item_price = self.__inventory[item_to_buy].get_sales_price() * qty_to_buy
            # profit to print in revenue report
            profit = item_price - (self.__inventory[item_to_buy].get_cost_price() * qty_to_buy)
            try:
                self.__profit_list[item_to_buy] = self.__profit_list[item_to_buy] + profit
            except KeyError:
                self.__profit_list[item_to_buy] = profit

            # qty to print in revenue report
            try:
                self.__sold_qty[item_to_buy] = self.__sold_qty[item_to_buy] + qty_to_buy
            except KeyError:
                self.__sold_qty[item_to_buy] = qty_to_buy

            # tells the user what they just bought
            print("This item costs $" + str(
                self.__inventory[item_to_buy].get_sales_price()) + " per unit" + "\nYou bought " + str(
                qty_to_buy) + " units, so the total price for this item will be $" + str(item_price))
            # summing the prices for the receipt
            total_price = total_price + item_price

            # keep track of ONLY the sku and use the sku to access the rest
            item_list.append(item_to_buy)
            qty_list.append(qty_to_buy)

        print("\nHere is your updated inventory:")
        self.print_inventory()
        time.sleep(3)

        print("\nUSER RECEIPT:---------------\n")
        for i in range(len(item_list)):
            item = item_list[i]
            print("PURCHASED ITEM:")
            print("You bought " + str(qty_list[i]) + " units of " + self.__inventory[item].get_name())
            print("Each unit cost: $" + str(self.__inventory[item].get_sales_price()))
            print("\n")
        print("Your price before tax is: $" + str(total_price))
        tax_price = total_price * 0.06
        print("Your final price is $" + str(total_price + tax_price))
        print("\nThank you for shopping with us!")
        time.sleep(10)

    def make_file(self):
        inv_file = open("inventory.txt", "wb")
        pickle.dump(self.__inventory, inv_file)
        inv_file.close()

        prof_file = open("prof_file.txt", "wb")
        pickle.dump(self.__profit_list, prof_file)
        prof_file.close()

        qty_file = open("qty_file.txt", "wb")
        pickle.dump(self.__sold_qty, qty_file)
        qty_file.close()

    def save_inv(self):
        inv_file = open("inventory.txt", "rb")
        self.__inventory = pickle.load(inv_file)
        inv_file.close()

        prof_file = open("prof_file.txt", "rb")
        self.__profit_list = pickle.load(prof_file)
        prof_file.close()

        qty_file = open("qty_file.txt", "rb")
        self.__sold_qty = pickle.load(qty_file)
        qty_file.close()

    def pickle(self):
        try:
            self.save_inv()
        except FileNotFoundError:
            self.make_file()

def menu():
    inventory1 = PartsInventory(123, "hat", 12, 14.99, 10.00, storage, profit_list, sold_qty)
    inventory1.pickle()
    menu = ConsoleMenu("What would you like to do now?")

    add_parts = FunctionItem("Add parts to your inventory", inventory1.add_parts)
    remove_parts = FunctionItem("Remove parts from your inventory", inventory1.remove_parts)
    change_qty = FunctionItem("Change the quantity of a certain part", inventory1.change_qty)
    report_inventory = FunctionItem("See a report of your inventory", inventory1.report_inventory)
    report_revenue = FunctionItem("See a report of your profits/losses", inventory1.report_revenue)
    sell_parts = FunctionItem("Sell parts to a customer.", inventory1.sell_parts)

    menu.append_item(add_parts)
    menu.append_item(remove_parts)
    menu.append_item(change_qty)
    menu.append_item(report_inventory)
    menu.append_item(report_revenue)
    menu.append_item(sell_parts)
    menu.show()

    inventory1.make_file()


menu()
