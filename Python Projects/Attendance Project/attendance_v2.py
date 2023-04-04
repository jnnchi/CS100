from consolemenu import *
from consolemenu.items import *
import pickle
import time

daily_sheet = {'Mon':'', 'Tues':'', 'Wed':'', 'Thurs':'', 'Fri':''}
week_sheet = {}

try:
  file = open("attendance.pickle", "rb")
  week_sheet = pickle.load(file)
  file.close()
except IOError:
  file = open("attendance.pickle", "wb")
  week_sheet = pickle.dump(week_sheet,file)
  file.close()

def menu():
  menu = ConsoleMenu("What would you like to do now?")
  enter_names = FunctionItem("Enter new student names", add_names)
  del_names = FunctionItem("Remove student names", delete_names)
  take_attendance = FunctionItem("Take attendance", take_attend)
  view_sheet = FunctionItem("See your attendance sheet", see_sheet)

  menu.append_item(enter_names)
  menu.append_item(del_names)
  menu.append_item(take_attendance)
  menu.append_item(view_sheet)
  menu.show()

def add_names():
  print("Before you add a new student, here is your attendance sheet so far: " + format(week_sheet))
  num_of_new = int(input("How many new student names would you like to input? "))
  for i in range(num_of_new):
    name = str(input("Student name #" + format(i+1) + ": ")).upper()
    week_sheet[name] = daily_sheet
  print("This is the attendance sheet with your changes:\n" + format(week_sheet))
  time.sleep(3)

def delete_names():
  print("Before you delete a student, here are your current students: ")
  for key in week_sheet.keys():
    print(key)
  delete_name = str(input("What is the name of the student you would like to delete? ")).upper()
  if delete_name in week_sheet:
    del week_sheet[delete_name]
    print("This is the attendance sheet with your changes:\n" + format(week_sheet))
  else:
    print("This student name does not exist.")
  time.sleep(3)

def take_attend():
  day = int(input("Which day are you on? (Please type 1, 2, 3, 4, or 5).\n"))
  for key in week_sheet.keys():
    if day == 1:
      d1 = str(input("Is " + format(key) + " (P)resent, (A)bsent, or (T)ardy? Type P, A, or T. ")).upper().strip()
      week_sheet[key]['Mon'] = d1
    elif day == 2:
      d2 = str(input("Is " + format(key) + "(P)resent, (A)bsent, or (T)ardy? Type P, A, or T. ")).upper().strip()
      week_sheet[key]['Tues'] = d2
    elif day == 3:
      d3 = str(input("Is " + format(key) + "(P)resent, (A)bsent, or (T)ardy? Type P, A, or T. ")).upper().strip()
      week_sheet[key]['Wed'] = d3
    elif day == 4:
      d4 = str(input("Is " + format(key) + "(P)resent, (A)bsent, or (T)ardy? Type P, A, or T. ")).upper().strip()
      week_sheet[key]['Thurs'] = d4
    elif day == 5:
      d5 = str(input("Is " + format(key) + "(P)resent, (A)bsent, or (T)ardy? Type P, A, or T. ")).upper().strip()
      week_sheet[key]['Fri'] = d5
  for key in week_sheet.keys():
    print("\n" + format(key) + "\'s Attendance:")
    for days in week_sheet[key]:
      print(format(days) + ": " + week_sheet[key][days])
  time.sleep(5)

def see_sheet():
  print(week_sheet)
  time.sleep(5)

print("Hi, welcome to your digital attendance sheet! Let's get started!")
time.sleep(1)
menu()
file = open("attendance.pickle", "wb")
week_sheet = pickle.dump(week_sheet,file)
file.close()
