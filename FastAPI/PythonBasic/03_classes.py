# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person('aaa', 30)
print(p1.name)
print(p1.age)


class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print(self.name)

p2 = Person("another name", 30)
p2.myFunc()


# Inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Child(Person):
   def __init__(self, fname, lname):
      Person.__init__(self, fname, lname)

class Student(Person):
   def __init__(self, fname, lname, year):
      super().__init__(self, fname, lname)
      self.graduation_year = year

student = Student('Mike', 'Joe', 2025)

# abstraction 
# only show necessary details to user 
# dont need to know inside how to complete 

class Enemy:
   type_of_enemy: str
   health_points: int = 10
   attack_damage: str = 1

   def talk(self):
      print(f'I am a {self.type_of_enemy}')
    

# if __ under score is immutable, but we still want to change the value
# Encapsulation come
#  getter and setter 

# keep related fields and methods together 
# makes our code cleaner and easier to read
# provide more flexibility to our code 
# more reuseable to our code 

# self VS super 

# "polymorphism" means "many forms", and in programming it refers to methods/functions/operators
#  with the same name that can be executed on many objects or classes.

my_str = "hello World"
my_tuple = ('a', 'b', 'c')
my_dict = {'a': 1, 'b': 2} 

len(my_str)
len(my_tuple)
len(my_dict)

# Class Polymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()