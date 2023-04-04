items = 0
sum = 0.0

print("What is the price of your item?")
for items in range(5):
  price = float(input("Price of item #" + format(items+1) + ": $"))
  items = items + 1
  sum = sum + price
  
print("The subtotal is $" + format(float(sum)))
print("The sales tax is 6%")
total = sum + sum * 0.06
print("The total is $" + format(total, '.2f'))
