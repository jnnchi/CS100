dictionary = {}
user_string = str(input("String: "))

for letter in user_string:
  if letter in dictionary:
    dictionary[letter] = dictionary[letter] + 1
  else:
    dictionary[letter] = 1

print(dictionary)
