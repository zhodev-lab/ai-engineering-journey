# create module
def greeting(name):
    print("hello", name)

#  use module 
import mymodule

mymodule.greeting("Jonathan")

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
# only the person1 dictionary from the module
from mymodule import person1

print (person1["age"])



import datetime 
x = datetime.datetime.now()
x.year
object_x = datetime.datetime(2020, 5, 17)
object_x.year
