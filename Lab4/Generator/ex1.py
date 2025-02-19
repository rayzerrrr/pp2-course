#1

# def square_generator(N):
#     for i in range(1, N + 1):
#         yield i ** 2


# N = int(input())
# squares = square_generator(N)
# for square in squares:
#     print(square)

#2
# def evens(N):
    
#     for x in range(1, N + 1):
#         if(x % 2 == 0):
#             yield x
    
    
# N = int(input())

# evens = evens(N)

# for even in evens:
#     print(even)

#3
# def div(N):
    
#     for x in range(1, N + 1):
#         if(x % 3 == 0 and x % 4 == 0):
#             yield x
    
    
# N = int(input())

# nums = div(N)

# for x in nums:
#     print(x)

#4
# def squares(a, b):
#     for num in range(a, b + 1):
#         yield num ** 2


# a = int(input())
# b = int(input())

# for square in squares(a, b):
#     print(square)

#5
# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1

# n = int(input())

# for num in countdown(n):
#     print(num)
