#our object is a person
class Person:
  #THIS IS OUR CONSTRUCTOR:
  #def, two underscores, "initialize" function, two underscores. the default parameter for init is self (doesn't HAVE to be self but it's default so you should use it).
  #add diff attributes of a person after (self,
  #initializes attributes for a person
  def __init__(self, name, age):
    self.name = name
    self.age = age

  #this is a METHOD, an action the person does
  #every method needs the self parameter; methods should always return a value. instead of putting a print statement, use return.
  #accessor (aka getter)
  def speak(self):
    return("Hello, my name is " + self.name)

  #mutator (aka setter); changes value
  def hasBirthday(self):
    self.age = self.age + 1

  #accessor (aka getter); returns value
  def getAge(self):
    return self.age

#create a person now that you have a person object
p1 = Person("John", 20)
#make John speak
print(p1.speak())
print(p1.getAge())
p1.hasBirthday()
print(p1.getAge())

p2 = Person("Seraphina", 18)
print(p2.speak())
