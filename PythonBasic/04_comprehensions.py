# global
def myFunc():
    global x
    x = 300

myFunc()
print(x)

# nonlocal
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

try:
  print(x)
except:
  print("An exception occurred")


