food_charge = float(input("Enter the charge for the food: "))
tip = food_charge * 0.15
sales_tax = food_charge * 0.07

print("15% Tip: $" + format(tip))
print("7% Sales Tax: $" + format(sales_tax))
total = food_charge + tip + sales_tax
print("The total is: $" + format(total))
