#can't write a dict to a file cuz you can only have a string; must use a module

#can also use a module called ast to cast str back to dict but it's better to use pickle

dictionary = {"a":1, "b":2, "c":3}

file = open("dictfile.txt", "w")
file.write(str(dictionary))
file.close()

file = open("dictfile.txt", "r")
dictionary2 = file.read()
print(dictionary2)
#prints string cuz we converted it
print(type(dictionary2))
file.close()
