def countstring(userlist):
  total = 0
  for element in sample_list:
    e_len = int(len(element))
    if (e_len >= 2):
      if (element[i] == element[e_len - 1]):
        total = total + 1
  return total

sample_list = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
length = int(input("How long is your list? "))
for i in range(length):
  sample_list[i] = str(input("Element " + format(i+1) + ": "))
print("List : " + format(list(filter(None, sample_list))))
print("Result : " + format(countstring(sample_list)))
