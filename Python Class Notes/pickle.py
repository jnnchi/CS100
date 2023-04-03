#pickle module; use when you're writing non-regular types to a file
import pickle
dictionary = {"a":1, "b":2, "c":3, "d":6}

#when you serialize an object it converts to binary; "wb" for write binary
file_to_write = open("output_file.pickle", "wb")

#instead of .write, it's .dump(thing you want to dump, file you want to dump it to) in pickle
pickle.dump(dictionary, file_to_write)
file_to_write.close()

file_to_open = open("output_file.pickle", "rb")

#instead of .read, pickle uses .load(file)
dictionary2 = pickle.load(file_to_open)
print(dictionary2)
print(type(dictionary2))
file_to_open.close()
