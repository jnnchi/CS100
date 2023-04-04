users_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

length = int(input("How many elements are in your tuple? "))
for i in range(length):
  users_list[i] = int(input("Element " + format(i+1) + ": "))

users_tuple = tuple(users_list)
simplified = (tuple(i for i in users_list if i != 0))
print("Original Tuple: \n" + format(simplified))

print("Sum - adding all the numbers of the said tuple: " + format(sum(list(users_tuple))))
