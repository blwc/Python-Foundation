###Guess the number. If guess is too high, reply too high, etc
###import imports a module
###random source code is at: https://hg.python.org/cpython/file/2.7/Lib/random.py
###random implements a pseudo-random number generator
def guess_the_number():
    import random
    #initialize the variable guess
    guess = -1
    #create the number to be guessed
    number = random.randrange(0, 100)
    print('Guess a number between 0 and 100.')
    guess = int(input())
    while guess != number:
        if guess > number:
            print('Too high!')
            #print('The number is: ' + str(number) + '. Your guess was: ' + str(guess))
        else:
            print('Too low!')
            #print('The number is' + str(number) + '. Your guess was: ' + str(guess))
            print('Guess another number')
            guess = int(input())
            print('You got it!')

#Collatz conjecture
#     If the number is even, divide it by two.
#     If the number is odd, triple it and add one.
#     This process will always end in the number 1
def collatz(i):
    number = i
    count = 0
    seq = str(i)
    while number != 1:
        if number%2:
            number = (number * 3) + 1
        else:
            number = number / 2
        count +=1
        seq += (', ' + str(int(number)))
    print(seq)
    print('It took ' + str(count) + ' operations to get ' + str(i) + ' to 1.')
    return count

#leap_year to chinese zodiac year???


# FizzBuzz
#
# For the numbers 1 through 100 (we'll learn this part soon)
#
#     If the number is divisible by 3 print 'Fizz'
#     If the number is divisible by 5 print 'Buzz'
#     If the number is divisible by both 3 and 5 print 'FizzBuzz'
#     otherwis, print the number

def FizzBuzz(i, j):
    if j < i:
        i, j = j, i
    for k in range (i, j):
        if not k%3 and not k%5:
            print('FizzBuzz', end=' ')
        elif not k%3:
            print('Fizz', end=' ')
        elif not k%5:
            print('Buzz', end=' ')
        if k%3 and k%5:
            print(str(k), end=' ')

#     Write a loop that sings 99 Bottles of Beer on the wall. Last line is 'No more bottles of beer on the wall'
#     Write another loop that does FizzBuzz for the numbers 1 to 100.
#     Print out the letters of the alphabet along with their index (a is 1, b is 2, c is 3)
#     Write a loop that prompts the user to enter a password twice. If both passwords are the same it prints "Access Granted" otherwise it reprompts them to enter their password again twice.
#
# Bonus:
#
#     Write a program that takes a word (or any input) and calculates the word value according the the alphabet index created above (i.e. cat == 3 + 1 + 20 == 24)
#     What if the word has uppercase letters? Account for those in your next solution.
#     List the amount of steps the Collatz procedure takes (until it reaches 1) for every number from 1 to 10.
