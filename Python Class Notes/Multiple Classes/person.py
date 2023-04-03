#can't run a class; only run the main. try not to write class and main in the same file
class Person:
  #these attributes should be private––put two underscores after self.
  def __init__(self, name, age):
    self.__name = name #self.__ makes it private
    self.__age = age

  #method
  def speak(self):
    return("Hello, my name is " + self.__name)

  #mutators (aka setter); changes value
  def setAge(self, age):
    self.__age = age
  
  def setName(self,name):
    self.__name = name #variable names are arbitrary; don't need to name it the same as the attribute

  #accessors (aka getter); returns value
  def getAge(self):
    return self.__age

  def getName(self):
    return self.__name

  #prints values of attributes; always returns a string
  def __str__(self):
    return("Name: " + self.__name + "\nAge: " + self.__age)