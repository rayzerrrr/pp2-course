# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

x = 'bhjwf'

print(x[0])

#there are a lot of functions connected to the strings properties. For instance:

print(len(x)) #show the length of string
print("h" in x) #boolean type of answer , check if there are a substring in string