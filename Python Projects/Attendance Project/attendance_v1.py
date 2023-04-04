import pickle
attendance_sheet = {}
week_sheet = {}
action = 0

try:
  file = open("week.pickle", "rb")
  week_sheet = pickle.load(file)
  file.close()
except IOError:
  file = open("week.pickle", "wb")
  week_sheet = pickle.dump(week_sheet,file)
  file.close()

def get_names(num_of_new):
  for i in range(num_of_new):
      name = str(input("Student name #" + format(i+1) + ": "))
      here = int(input("Is the student: 1. present, 2. absent, or 3. tardy? Type 1 for present, 2 for absent, and 3 for tardy. Type 0 for none. "))
      if here == 1:
        attendance_sheet[name] = "present"
      elif here == 2:
        attendance_sheet[name] = "absent"
      elif here == 3:
        attendance_sheet[name] = "tardy"
      else:
        attendance_sheet[name] = ""
  return attendance_sheet

def get_action():
  action = int(input("\nWhat would you like to do now?\n 1. enter more student names\n 2. remove student names\n 3. take attendance\n 4. see your attendance sheet\nType the number (1, 2, 3, 4). Type 0 for none.\n"))
  return action;

day = int(input("Hi! Welcome to your digital attendance sheet, let's get started!\nWhich day are you on? (Please type 1, 2, 3, 4, 5, 6, or 7).\n"))

num_names = int(input("How many students do you have? Type 0 if you don't want to input them just yet. \n"))
get_names(num_names)
print("This is today's attendance sheet so far: " + format(attendance_sheet))

action = get_action()

while ((day <= 7) and (action > 0) and (action < 4)):
  while action == 1:
    new_names = int(input("How many new names would you like to input? "))
    get_names(new_names)
    print("This is the attendance sheet with your changes:\n" + format(attendance_sheet)) 
    action = get_action()
  while action == 2:
    delete_name = str(input("What is the name of the student you would like to delete? Type \"n\" if you want to see the names present. "))
    if delete_name in attendance_sheet:
      del attendance_sheet[delete_name]
      print("This is the attendance sheet with your changes:\n" + format(attendance_sheet))
    elif delete_name[0].lower() == 'n':
      print("These are your current students: ")
      for key in attendance_sheet.keys():
        print(key)
      delete_name = str(input("What is the name of the student you would like to delete? "))
      del attendance_sheet[delete_name]
      print("This is the attendance sheet with your changes:\n" + format(attendance_sheet))
    else:
      print("This student name does not exist.")
    action = get_action()
  while action == 3:
    for key in attendance_sheet.keys():
      attend = int(input("Is " + format(key) + ": 1. present, 2. absent, or 3. tardy? Type 1 for present, 2 for absent, and 3 for tardy. Type 0 if you've already input their attendance status. "))
      if attend == 1:
        attendance_sheet[key] = "present"
      elif attend == 2:
        attendance_sheet[key] = "absent"
      elif attend == 3:
        attendance_sheet[key] = "tardy"
    print("This is the attendance sheet with your changes:\n" + format(attendance_sheet))
    action = get_action()
  while action == 4:
    print("This is your attendance sheet so far:\n" + format(attendance_sheet))
    action = get_action()
if (action == 0) and (day != 7):
  week_sheet["Day " + str(day)] = attendance_sheet
  print("This is the week's attendance sheet so far:\n" + format(week_sheet))
  print("Thank you for using this program, see you next time!")
elif (action == 0) and (day == 7):
  week_sheet["Day " + str(day)] = attendance_sheet
  print("Congratulations, you've finished taking attendance! This is your finished attendance sheet for the week:\n" + format(week_sheet))

file = open("week.pickle", "wb")
week_sheet = pickle.dump(week_sheet,file)
file.close()
