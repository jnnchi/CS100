file = open("numberfile.txt", "w")
import random
length = int(input("How many random numbers will the file hold? "))
for i in range(length):
  file.write(str(random.randrange(1, 101)) + " ")
file.close()

file2 = open("numberfile.txt", "r")
print(file2.read())
file2.close()
