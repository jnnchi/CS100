import random

def add_numbers():
  count = 0
  loop = 0
  for loop in range(5):
    x = random.randrange(1, 100)
    print("Question #" + format(loop + 1) + ": \n" + "The first number is " + format(x))
    y = random.randrange(1, 100)
    print("The second number is " + format(y))
    sum = int(input("What is the sum of the numbers? "))
    if (sum == (x + y)) and (loop < 4):
      print("That is correct! On to the next question!")
      count = count + 1
    elif (sum == (x + y)) and (loop == 4):
      count = count + 1
      print("That is correct!")
    elif (sum != (x+y)) and (loop < 4):
      print("That is incorrect! On to the next question!")
    elif (sum != (x+y)) and (loop == 4):
      print("That is incorrect!")
  print("Your score is: " + format(count) + " out of 5!")

if __name__ == '__main__':
  name = str(input("What is your name? "))
  print("Hi, " + name + ", let's start the game!")
  add_numbers()
  again = str(input("Would you like to play again? "))
  while again[0].lower() == 'y':
    print("Let's start the game!")
    add_numbers()
    again = str(input("Would you like to play again? "))
  if again[0].lower() == 'n':
    print("Thank you for playing!")
