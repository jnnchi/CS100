class Employee:

  def __init__(self, name, emp_number):
    self.__name = name
    self.__emp_number = emp_number

  def set_name(self, name):
    self.__name = name
  
  def set_emp_number(self, emp_number):
    self.__emp_number = emp_number
  
  def get_name(self):
    return self.__name
  
  def get_emp_number(self):
    return self.__emp_number

  def __str__(self): #polymorphism cuz three different str functs
    return("\nEmployee Name: " + self.get_name() + "\nEmployee Number: " + str(self.get_emp_number()))

class ProductionWorker(Employee):

  def __init__(self, name, emp_number, shift_num, pay):
    Employee.__init__(self, name, emp_number)
    self.__shift_num = shift_num
    self.__pay = pay
  
  def set_shift_num(self, shift_num):
    self.__shift_num = shift_num
  
  def set_pay(self, pay):
    self.__pay = pay

  def get_shift_num(self):
    if self.__shift_num == 1:
      return "Day Shift"
    elif self.__shift_num == 2:
      return "Night Shift"

  def get_pay(self):
    return self.__pay

  def __str__(self):
    return("\nEmployee Name: " + self.get_name() + "\nEmployee Number: " + str(self.get_emp_number()) + "\nShift: " + self.get_shift_num() + "\nHourly Pay: " + str(self.get_pay()) + "\n")

class ShiftSupervisor(ProductionWorker):

  def __init__(self, name, emp_number, shift_num, pay, salary, bonus):
    ProductionWorker.__init__(self, name, emp_number, shift_num, pay)
    self.__salary = salary
    self.__bonus = bonus
  
  def set_salary(self, salary):
    self.__salary = salary
  
  def set_bonus(self, bonus):
    self.__bonus = bonus

  def get_salary(self):
    return self.__salary
  
  def get_bonus(self):
    return self.__bonus
  
  def __str__(self):
    return("\nEmployee Name: " + self.get_name() + "\nEmployee Number: " + str(self.get_emp_number()) + "\nShift: " + self.get_shift_num() + "\nHourly Pay: " + str(self.get_pay()) + "\nAnnual Salary: " + str(self.get_salary()) + "\nAnnual Production Bonus: " + str(self.get_bonus()))

def main():
  worker_name = str(input("What is your name? "))
  worker_num = int(input("What is your employee number? "))
  worker_shift = int(input("Which shift do you work? Type 1 for Day Shift and 2 for Night Shift. "))
  worker_pay = float(input("What is your hourly pay rate? "))

  worker = ProductionWorker(worker_name, worker_num, worker_shift, worker_pay)
  print("\nEmployee Name: " + worker.get_name() + "\nEmployee Number: " + str(worker.get_emp_number()) + "\nShift: " + worker.get_shift_num() + "\nHourly Pay: " + str(worker.get_pay()) + "\n")
  
  super_name = str(input("What is your name? "))
  super_num = int(input("What is your employee number? "))
  super_shift = int(input("Which shift do you work? Type 1 for Day Shift and 2 for Night Shift. "))
  super_pay = float(input("What is your hourly pay rate? "))
  super_salary = float(input("What is your annual salary? "))
  super_bonus = float(input("What is your annual production bonus? "))

  supervisor = ShiftSupervisor(super_name, super_num, super_shift, super_pay, super_salary, super_bonus)
  print(supervisor)

main()
