import pickle

ids_major = {12345:"statistics", 22345:"computers",32345:"biology", 42345:"literature", 52345:"psychology"}

#unpickles the file when the file exists, makes file if it doesn't exist
try:
  file = open("majors.pickle", "rb")
  ids_major = pickle.load(file)
  file.close()
except IOError:
  file = open("majors.pickle", "wb")
  ids_major = pickle.dump(ids_major,file)
  file.close()

ids_major = {12345:"statistics", 22345:"computers",32345:"biology", 42345:"literature", 52345:"psychology"}

#shows menu and asks user what to do
action = int(input("What would you like to do first?\n 1. look up an ID number\n 2. add a new ID and major\n 3. change an existing major\n 4. delete an existing ID and major\n Type the number only (1, 2, 3, or 4). Type 0 for none.\n"))

while (action > 0) and (action < 5):
  while action == 1: #look up ID number
    number = int(input("What is the ID of the major you would like to see? "))
    if number in ids_major:
      print("The major is: " + format(ids_major[number]))
    else:
      print("This ID does not exist.")
    action = int(input("\nWhat would you like to do now?\n 1. look up an ID number\n 2. add a new ID and major\n 3. change an existing major\n 4. delete an existing ID and major\n Type 0 for nothing.\n"))
  while action == 2: #make new major and ID
    new_major = str(input("What is the major? "))
    new_id = int(input("What is the new 5-digit ID? "))
    new_value = {new_id:new_major}
    ids_major.update(new_value)
    print("This is the dictionary with your changes:\n" + format(ids_major))
    action = int(input("\nWhat would you like to do now?\n 1. look up an ID number\n 2. add a new ID and major\n 3. change an existing major\n 4. delete an existing ID and major\nType 0 for nothing.\n"))
  while action == 3: #change a major
    key = int(input("What is the ID of the major? "))
    if key in ids_major:
      changed_major = str(input("What is the new major name? "))
      ids_major[key] = changed_major
      print("This is the dictionary with your changes:\n" + format(ids_major))
    else:
      print("This ID does not exist.")
    action = int(input("\nWhat would you like to do now?\n 1. look up an ID number\n 2. add a new ID and major\n 3. change an existing major\n 4. delete an existing ID and major\n Type 0 for nothing.\n"))
  while action == 4: #delete a major and ID
    delete_id = int(input("What is the 5-digit ID of the major you would like to delete? "))
    if delete_id in ids_major:
      del ids_major[delete_id]
      print("This is the dictionary with your changes:\n" + format(ids_major))
    else:
      print("This ID does not exist.")
    action = int(input("\nWhat would you like to do now?\n 1. look up an ID number\n 2. add a new ID and major\n 3. change an existing major\n 4. delete an existing ID and major\n Type 0 for nothing.\n"))
if (action == 0):
  print("Thank you for using this program, goodbye!")

#pickles the file
file = open("majors.pickle", "wb")
ids_major = pickle.dump(ids_major,file)
file.close()
