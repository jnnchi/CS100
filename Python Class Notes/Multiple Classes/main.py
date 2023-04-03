from person import Person
#should not be able to access a class's attributes directly; that's why we have methods, so you can do things without directly saying "self.name," etc
p1 = Person("Nora Alvarado", 21)
print(p1.speak())
print(p1.getAge())
print("Hello my name is " + p1.getName())
print("My age is " + str(p1.getAge()))
p1.setName("Nora Demosthenes")
print(p1.getName())

from student import Student

s1 = Student("Joe", 15, 2024)
print(s1)