#slicing
#Strings can be sliced on the specified range

x = 'Hello, world!'

print(x[2 : 5]) #from 2 index to the 5 not included
print(x[ : 5]) #from start to 5
print(x[2 :]) #from 2 to the end

#modify strings

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = "Hello, World! H"
print(a.replace("H", "J"))

a = "Hello, World!"

b = a.split(",")
print(b)
print(type(b))