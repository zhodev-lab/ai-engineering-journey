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