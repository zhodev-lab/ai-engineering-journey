# Functions & Control Flow | `if`, `for`, `while`, `return` | `02_functions.py` |
a = 33
b = 100
if b> a:
    print("b greater a ")
elif a==b:
    print(" b is equal a ")
else:
    print("a greater b")


c = 50
if a> b and c> a:
    print("Both condition")

if a > b or c > a:
    print("or condition")



if not a > b: 
    print(" not keywords for the reverse the conditional statement")


if b > a:
    pass 



#  loops 
my_list = [1,2,3]
for lst in my_list:
    print(lst)


i = 0
while i<5:
    i+= 1
    if i == 3:
        continue
    

# functions 
def function_name(self, input_values):
    return input_values


# If you do not know how many arguments 
# that will be passed into your function, 
# add a * before the parameter name in the function definition.
def my_function(*kids):
    print("the child is:" + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# output is linus

# If you do not know how many keyword arguments 
# that will be passed into your function, add two asterisk: 
# ** before the parameter name in the function definition.
def my_function(arg1, *args, **kwargs):
    print("arg1:", arg1)
    print("args:", args)
    print("kwargs:", kwargs)

my_function(1, 2, 3, a=4, b=5)
# 输出:
# arg1: 1
# args: (2, 3)
# kwargs: {'a': 4, 'b': 5}

list1 = [1, 2, 3]
dict1 = {"a": 4, "b": 5}

my_function(0, *list1, **dict1)
# 输出:
# arg1: 0
# args: (1, 2, 3)
# kwargs: {'a': 4, 'b': 5}

import random
type_of_drinks = ['Soda', 'coffee', 'Water', 'tea']
print(random.choice(type_of_drinks))

print(random.randint(1, 10))