#in python functions prioritize their inner value of variable if it exists  and it wont change their value globally
#but if you want you can use global to change it

x = "awesome"

def myfunc1():
  x = "good"
  print("Python is " + x)


myfunc1()

print("Python is " + x)


def myfunc2():
  global x
  x = 'bad'
  print("Python is " + x)

myfunc2()

