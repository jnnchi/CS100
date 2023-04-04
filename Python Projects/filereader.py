file = open("numberfile.txt", "w")
sum = 0
numlist = []
import random

length = int(input("How many random numbers will the file hold? "))
for i in range(length):
  numlist.append(random.randrange(1,101))
  file.write(str(numlist[i]) + " ")
  sum = sum + numlist[i]
file.close()

file2 = open("numberfile.txt", "r")
print("The random numbers: " + format(file2.read()))
file2.close()
print("The sum of the numbers is: " + format(sum))
numlist.sort()
print("The sorted list is: " + format(numlist))
