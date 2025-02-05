import math

#1 def grams_to_ounces(grams):
#     return grams * 28.3495231

# x = int(input())

# print(grams_to_ounces(x))


#2 def f_to_c(f):
#     return (5 / 9) * (f - 32)

# x = int(input())

# print(f_to_c(x))

#3 def Solution(numheads, numlegs):
#     for chickens in range(numheads + 1):
#         rabbits = numheads - chickens
#         if 2 * chickens + 4 * rabbits == numlegs:
#             return chickens, rabbits
#     return 0
# x , y = map(int , input().split())

# print(Solution(x , y))

# numbers = list(map(int , input().split()))


#4 def isPrime(n):
#     if n < 2:
#         return False
#     for x in range(2 , int(math.sqrt(n)) + 1):
#         if n % x == 0:
#            return False
#     return True

# primes = list(filter(isPrime , numbers))  

# print(primes)

#5 def string_permutations(s, step=0):
#     if step == len(s) - 1:
#         print("".join(s)) 
#         return
    
#     for i in range(step, len(s)):
#         s = list(s)
#         s[step], s[i] = s[i], s[step]  
#         string_permutations(s, step + 1) 
#         s[step], s[i] = s[i], s[step]  

# string = input()

# string_permutations(string)

#6 def reverse_words(sentence):
#     wordslist = sentence.split()
#     wordslist.sort(reverse = True)
#     return " ".join(wordslist)


# sentence = input()

# print(reverse_words(sentence))

#7

# def has_33(nums):
#     for i in range(0 , len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#     return False

# nums = list(map(int , input().split()))

# print(has_33(nums))

#8

# def spy_game(nums):
#     pattern = [0 , 0 , 7]
#     index = 0

#     for i in nums:
#      if i == pattern[index]:
#         index += 1
#         if index == len(pattern):
#            return True    
#     return False

# nums = list(map(int , input().split()))

# print(spy_game(nums))

#9

# def sphere_volume(radius):
#     return (4/3) * math.pi * radius**3

# r = int(input())

# print(sphere_volume(r))

#10

# def unique_elements(lst):
#     unique_list = []
#     for num in lst:
#         if num not in unique_list:
#             unique_list.append(num)
#     return unique_list

# lst = list(map(int , input().split()))

# print(unique_elements(lst))

#11

# def is_palindrome(word):
#     word = word.replace(" ", "").lower()
#     reversed_word = word[::-1] 
#     return word == reversed_word  

# word = input()
# print(is_palindrome(word))

#12

# def histogram(lst):
#     for num in lst:
#         print('*' * num)

# lst = list(map(int , input().split()))

# histogram(lst)

#13

import random

def guessNum():
    print("Hello! What is your name?")
    name = input()

    num = random.randint(1 , 20)
    print(f"Well,{name}, I am thinking of a number between 1 and 20.")
    attempt = 0

    while True:
        print("\nTake a guess.")

        guess = int(input())
        attempt += 1
        

        if guess > num:
            print("\nYour guess is too high.")
        elif guess < num:
            print("\nYour guess is too low.")
        else:
             print(f"Good job, {name}! You guessed my number in {attempt} attempts.")
             break

guessNum()