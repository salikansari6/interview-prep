class User:
  #! Polymorphism
  def log(self):
    print(self)

class Teacher(User):
  #! Polymorphism
  def log(self):
    print("I'm a Teacher")

# Inheritance
class Customer(User):
  # Constructor / Initialiazer
  def __init__(self, name, membershipType):
    self.name = name
    self.membershipType = membershipType
  
  def __str__(self):
    # customers[0] will return value instead of object location
    return self.name + " " + self.membershipType
  
  def __eq__(self, other):
    # if __eq__() not overrided object location are matched by default
    if self.name == other.name and self.membershipType == other.membershipType:
      return True
    return False

  # Non Hashable Object
  __hash__ = None

  # customers will return values instead of Object location
  __repr__ = __str__

  #! Polymorphism
  def log(self):
    print("I'm a Customer")

  # Encapsulation
  @property # getter method in many different langugages
  def name(self):
    return self._name

  @name.setter # setter method
  def name(self, name):
    self._name = name

  @name.deleter
  def name(self):
    del self._name
  
  # Methods
  def updateMembership(self, newMembership):
    # API Call, Update DB, Charge Customers etc
    self.membershipType = newMembership

  def readCustomer():
    print("Read Customers from DB")

  def printAllCustomers(customers):
    for customer in customers:
      print(customer)

  

# ===================================================================================================================================

print("----- OOP -----")
customers = [Customer("Rizwan", "Premium"), Customer("Rehan", "Gold"), Customer("Rizwan", "Premium")]
print(customers[0].name)
print()


print("----- __str__() and Methods -----")
customers[1].updateMembership("Premium")
print(customers[1])
print()

print("----- No self Method -----")
Customer.printAllCustomers(customers)
print()

print("----- __eq__ -----")
print(customers[0] == customers[2])
print()

print("----- __repr__ -----")
print(customers)
print()

print("----- INHERITANCE -----")
customers[0].log()
print()


print("----- POLYMORPHISM -----")
users = [Customer("Rizwan", "Premium"), Customer("Rehan", "Gold"), Teacher()]

for user in users: 
  user.log()
print()
