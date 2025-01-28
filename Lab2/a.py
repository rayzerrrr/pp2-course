#Boolean

# a = True
# b = False

# if a :
#     print("hello")

# if b : 
#     print("World")


#if we specify any non-zero/empty value in boolean data type we will get "True" , in other cases "False"

# a = ''
# b = 'abc'

# print(bool(a))
# print(bool(b))

#in general this data type is used in if/else structure

# a  = 10
# b = 5

# if a / b == 3: 
#     print("Correct")
# else:
#     print('Incorrect')


#Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type:

# x = 1
# print(isinstance(x , int))

# Python divides the operators in the following groups:

# Arithmetic operators 

# x = 2
# y = 3
# print(x + y , x - y , x * y , x / y)

# Assignment operators

# x = 10 
# x += 5  #which means x = x + 5
# x -= 5  #same
# print(x)

# Comparison operators
# a = 5
# b = 5

# if a == b: 
#     print('equal')
# elif a > b: 
#     print('a>')
# else:
#      print('b>')
# Logical operators
# and 	Returns True if both statements are true	
# x = 3
# if x < 5 and  x > 1:
#  print("in interval")
# or	Returns True if one of the statements is true	
# x = 3
# if x < 5 or x > 4:
#  print("at least in one interval")
# not	Reverse the result, returns False if the result is true	
# x = 3
# if not(x < 1 and x < 2):
#  print("Not in interval")
# Identity operators
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y
# x = 5
# y = 5
# z = 'abc'

# if x is y and y is not z:
#     print("correct")
# Membership operators
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
# x = 'a'
# y = 'abc'
# z = 'd'

# if x in y:
#     print("a is in abc")
# if z not in y:
#     print("z not in y")
# Bitwise operators
#operators that works with the bits of binary numbers by comparing them. For instance, and | or | xor

# 5 = 0000000000000101
# 7 = 0000000000000111

# x = 5
# y = 7 
# print (x & y , x | y , x ^ y)

#Operator Precedence
#() - highest precedence , * and / higher than + and -

# print((2 +2) * 2, 2 + 2 * 2)


#Lists 
#Ordered , indexed, changeable data type. It can contain elements that can differ by their data type , and do not exclude duplicates 
#thislist = ["apple", "banana", "cherry"]
#list's elements can be changed by their index , you can change them one by one or change the specific range of elements
#thislist = ["apple", "banana", "cherry"]
#thislist[1] = ["berry"]
#thislist[0:3] = ["a" , "b" , "c"]
#or you can add new elements by insert() function:
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(len(thislist) + 1, "berry") #add to the end of the list
# print(thislist)

#Two lists can be composed by extention of one of the lists by elements from another
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

#there are a lot of functions that exclude elements from the list like remove("specified value") , pop(index) 
# and clear(empty whole list) or del that can do both og the last two f
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
#print(thislist)
#thislist.remove("apple")
#print(thislist)
#thislist.clear()
#print(thislist)

#to work with each elemen tat once we cqan use loops like while and for

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i += 1

#to create a list that will contain elements from the another list with the specified conditions(if you want) we cant write it like this

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

#or in a short form (newlist = [expression for item in iterable if condition == True])
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# The expression is the current item in the iteration, but it is also the outcome,
#  which you can manipulate before it ends up like a list item in the new list:
# Set the values in the new list to upper case:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)

#Lists can be sorted in many ways by built-in function sort() or define it via function

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort() # or thislist.sort(reverse = True) for descending order
# print(thislist)

# def myfunc(n):
#   return abs(n - 50) Sort the list based on how close the number is to 50:

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

#To copy the list you can use built in functions like copy() or list() or
#  equate new list to the range of the previous from beginnig to the end

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)


#Tuple is very similar to lists but their elements cant be changed , but thereare some compilcated ways to do that
# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("mango")
# y[1] = "kiwi"
# x = tuple(y) 
# print(x)

#same ways for removing items

#tuples are easier to combine 

# x = (1 ,2 , 3)
# y = (4 ,) #When creating a tuple with only one item,
# #remember to include a comma after the item, otherwise it will not be identified as a tuple.

# x += y

# print(x)

#we can assign a variable for each value in a tuple
# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

#if the amount of variables is less than the quantity of elements, 
# depending on place of * you can contain the remainig ones in the list of a variable
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

#Everything about loops in lists is same for tuples

#Tuple can be multiplied and contain duplicates of itself

# x = (1 , 2 , 3)
# x *= 3
# print(x)

#Sets set items are unordered, unchangeable, and do not allow duplicate values.



#in set 1 and 0 is considered as True and False accordingly

# You cannot access items in a set by referring to an index or a key.

# But you can loop through the set items using a for loop
# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

#to add new items in set you can use functipn add() or 
# you can use update() to add element from one set to another(but its not necessary to be set)
#thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)

#to remove elements from set you can use remove() and discard() functions
#the only difference is that remove will give an error if item to remove will not be finded  and discard wont do that
# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)

#pop() also works, but since the set is unordered pop will delete random element

# thisset = {3 ,2 , 1}
# thisset.pop()
# print(thisset)

#to combine sets we also can use union() or | , but the second option allows to join sets and no other data types

# set1 = {1 , 2}
# set2 = {3 , 4}
# set3 = {5 , 6}

# set1  = set1.union(set2 , set3)  #or set1 = set1 | set2 | set3

# print(set1)

#Dictionary

# Dictionary items are ordered, changeable, and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

#to access to the value of a key in dict

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"] #or x = thisdict.get("model")
# print(x)

#use functions keys(),values(),items() to create a list of the keys , values and tuples of pairs key-value

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()
# y = thisdict.values()
# z = thisdict.items()

# print(x , y , z)

#to add a new pair 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisdict['color'] = 'yellow'

# print(thisdict)

#to change a value of a key address to its key and set a new value ,
#if the key does not exist and you want to add it then use update function

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

#to remove the last inserted item use popitem() 
#to remove item by it's key use pop(key) or del thisdict[key]
#also you can delete entire dict by del or just empty it by clear()
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model") #or del thisdict["model"]
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

#Loops in dictionary

#you can loop through keys and values separately by

# for x in thisdict:
#   print(x)

# for x in thisdict:
#   print(thisdict[x])

#or

# for x in thisdict.keys():
#   print(x)

# for x in thisdict.values():
#   print(x)


#or cover both by items()

# for x, y in thisdict.items():
#   print(x, y)

#Nested Dictionary

#Example
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

#addressing

#print(myfamily["child2"]["name"])

#Loops for a dictionary in dictionary

# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])

#If - else general form

# if statement: 
#     action
# elif if there another case to check:
#     content
# else: for every other cases
#     content

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

#Short forms

#for 1 statement
# if a > b: print("a is greater than b")
#for 2
#print("A") if a > b else print("B")

#nested if

# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

#Loops (while , for)

#With the while loop we can execute a set of statements as long as a condition is true and stop it with certain conditions.

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

#we can add a content for else if condition in loop became false

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

#A for loop is used for iterating over a sequences

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

#can be stopped by break statement

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

#To loop through a set of code a specified number of times, we can use the range(x,y,z) function
#x - beginning of a sequence , y - end of it , z - increment value(default 1)

# for x in range(2, 30, 3):
#   print(x)

#when loop has finished you can add an else statement that will go after it ,
#  if the loop will stop during its work else statement wont work

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")


# Nested Loops
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)