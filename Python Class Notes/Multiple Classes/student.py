#person is the parent class, student is the child class
from person import Person

class Student(Person):
  #pass <-  this will just put everythign in Person into Student

  #every class should have an init function, so instead of pass, you can write:
  def __init__(self,name,age,gradyear):
    #must access parent's init function
    super().__init__(name,age)
    self.__gradyear = gradyear

  def __str__(self):
    return("Name: " + self.getName() + "\nAge: " + str(self.getAge()) + "\nGrad year: " + str(self.__gradyear))

