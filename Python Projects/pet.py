class Pet:
  def __init__(self, name, animal_type, age):
    self.__name = name
    self.__animal_type = animal_type
    self.__age = age
  
  def set_name(self, name):
    self.name = name
  
  def set_animal_type(self, animal_type):
    self.__animal_type = animal_type
  
  def set_age(self, age):
    self.__age = age
  
  def get_name(self):
    return self.__name

  def get_animal_type(self):
    return self.__animal_type

  def get_age(self):
    return self.__age

def main():
  name = str(input("What is your pet's name? "))
  animal = str(input("What kind of animal is your pet? "))
  age = int(input("How old is your pet? "))
  pet = Pet(name, animal, age)
  print("Your pet's name is: " + pet.get_name() + "\nYour pet is a: " + pet.get_animal_type() + "\nYour pet's age is: " + str(pet.get_age()) + " years old.")

main()
