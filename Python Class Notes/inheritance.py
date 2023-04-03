class Person:
  #two underscores are a dunder
  def __init__(self, name, address, telephone):
    self.__name = name
    self.__address = address
    self.__telephone = telephone

  def set_name(self, name):
    self.__name = name
  
  def set_address(self, address):
    self.__address = address
  
  def set_telephone(self, telephone):
    self.__telephone = telephone

  def get_name(self):
    return self.__name
  
  def get_address(self):
    return self.__address
  
  def get_telephone(self):
    return self.__telephone

  def __str__(self):
    return ("Name: " + self.__name + "\nAddress: " + str(self.__address) + "\nTelephone: " + str(self.__telephone))
  
#now every customer created will have every Person attribute
class Customer(Person):
  
  def __init__(self, name, address, telephone, customer_num, mailing_list):
    #send over attributes
    Person.__init__(self, name, address, telephone)
    self.__customer_num = customer_num
    self.__mailing_list = mailing_list
  
  def set_customer_num(self, customer_num):
    self.__customer_num = customer_num
  
  def set_mailing_list(self, mailing_list):
    self.__mailing_list = mailing_list
  
  def get_customer_num(self):
    return self.__customer_num
  
  def get_mailing_list(self):
    return self.__mailing_list

  def __str__(self):
    #using getters is better cuz keep attributes PRIVATE
    return ("\nName: " + self.get_name() + "\nPhone: " + str(self.get_telephone()) + "\nAddress: " + str(self.get_address()) + "\nCustomer Number: " + str(self.get_customer_num()) + "\nOn Mailing List: " + self.get_mailing_list())

    #return ("Name: " + self._Person__name + "\nAddress: " + str(self._Person__address) + "\nTelephone: " + str(self._Person__telephone) + "\nCustomer Number: " + str(self.__customer_num) + "\nOn Mailing List: " + choice)
    

def main():
  name = input("Customer Name: ")
  address = input("Customer Address: ")
  phone = input("Customer Telephone Number: ")
  number = input("Customer Number: ")
  mail = input("Will the customer be on the mailing list? Type True or False. ").lower()

  if mail == "true":
    mail = "YES"
  elif mail == "false":
    mail = "NO"

  #create an object of type Customer
  info = Customer(name, address, phone, number, mail)
  #without the str function, you wouldn't be able to print––it would just show you where it's located
  print(info)

main()
