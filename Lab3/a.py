import math

# class toUpper:
#     def __init__(self):
#         self.string = ""

#     def getString(self):
#         self.string = input()

#     def printString(self):
#         print(self.string.upper())

# string = toUpper()
# string.getString()
# string.printString()

#2 class Shapes:
#     def area(self):
#         return 0

# class Square(Shapes):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length * self.length

# length = float(input())

# square = Square(length)

# print(square.area())


#3 class Shapes:
#     def area(self):
#         return 0

# class Rectangle(Shapes):
#     def __init__(self, length , width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# length, width = map(int, input().split())

# square = Rectangle(length , width)

# print(square.area())






# class Point:
#     def __init__(self, x, y, x2, y2):
#         self.x = x
#         self.y = y
#         self.x2 = x2
#         self.y2 = y2

#     def show(self):
#         print(f"({self.x}, {self.y})")

#     def dist(self):
#         return math.sqrt((self.x2 - self.x)**2 + (self.y2 - self.y)**2)

#     def move(self):
#         self.x = self.x2
#         self.y = self.y2


# x, y, x2, y2 = map(int, input().split())


# point = Point(x, y, x2, y2)


# point.show()


# print(f"Distance: {point.dist()}")

# point.move()

# point.show()

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, money):
#         self.balance += money
#         print(self.balance)

#     def withdraw(self, money):
#         if money > self.balance:
#             print(self.balance)
#         else:
#             self.balance -= money
#             print(self.balance)

# owner = input()
# balance = int(input())

# account = Account(owner, balance)

# while True:
#     command = input().strip().lower()

#     if command == "exit":
#         break
#     elif command in ["deposit", "withdraw"]:
#             amount = int(input())
#             if amount < 0:
#                 continue

#             if command == "deposit":
#                 account.deposit(amount)
#             elif command == "withdraw":
#                 account.withdraw(amount)
#     else:
#         continue


# numbers = list(map(int , input().split()))


# primes = list(filter(lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)), numbers))

# print(primes) 

