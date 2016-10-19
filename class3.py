### Introduction to flow control
# my_age = 0
# my_name = 'Bridie'
# if my_name != 'Bridie':
#     print('You are not Bridie')
#     if my_age % 10 == 0:
#         print("But it's a big year for you eh?")
#     elif my_age % 5 == 0:
#         print("You're halfway through a decade!")
#     else:
#         print(str(my_age) + " isn't a big deal.")

###
#Guess the number. If guess is too high, reply too high, etc
#import imports a module
#random source code is at: https://hg.python.org/cpython/file/2.7/Lib/random.py
#random implements a pseudo-random number generator
# import random
# #initialize the variable guess
# guess = -1
# #create the number to be guessed
# number = random.randrange(0, 100)
# print('Guess a number between 0 and 100.')
# guess = int(input())
# while guess != number:
#     if guess > number:
#         print('Too high!')
#         #print('The number is: ' + str(number) + '. Your guess was: ' + str(guess))
#     else:
#         print('Too low!')
#         #print('The number is' + str(number) + '. Your guess was: ' + str(guess))
#     print('Guess another number')
#     guess = int(input())
# print('You got it!')

##  a if <condition> else b

### leap year
# print("Provide a year to see if it's a leap year.")
# #check input type is an int
# year = int(input())
# if year % 400 == 0:
#     print('It\'s a leap year!')
# elif year % 100 == 0:
#     print('Sorry, not a leap year.')
# elif year % 4 == 0:
#     print('It\'s a leap year!')
# else:
#     print('Sorry, not a leap year.')
