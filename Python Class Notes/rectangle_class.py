#Write Python class called Rectangle constructed by length and width and methods which will compute the area and perimeter of a rectangle.
#Write a class named square, a subclass of Rectangle which does the same

class Rectangle:
  def __init__(self, length, width):
    self.__length = length
    self.__width = width
  
  def set_length(self, length):
    self.__length = length

  def set_width(self, width):
    self.__width = width
  
  def get_length(self):
    return self.__length
  
  def get_width(self):
    return self.__width
  
  def __str__(self):
    return ("Length: " + str(self.get_length()) + "\nWidth: " + str(self.get_width()))

  def area(self):
    return (self.get_length() * self.get_width())

  def perimeter(self):
    return ((2 * self.get_length()) + (2 * self.get_width()))
  
class Square(Rectangle):
  def __init__(self, length, width):
    Rectangle.__init__(self)
  
  def area(self): #polymorphism; same name but diff operation cuz diff object
    return self.get_length()**2

def main():
  length = int(input("Enter a length: "))
  width = int(input("Enter a width: "))
  shape1 = Rectangle(length, width)
  print(shape1)

main()
