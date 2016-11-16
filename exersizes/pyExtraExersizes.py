"""
A collection of basic practice problems.
"""

def guess_the_number():
    """
    Guess the number. If guess is too high, reply too high, etc
    import imports a module
    random source code is at: https://hg.python.org/cpython/file/2.7/Lib/random.py
    random implements a pseudo-random number generator
    """
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


def collatz(i):
    """
    Collatz conjecture
        If the number is even, divide it by two.
        If the number is odd, triple it and add one.
        This process will always end in the number 1
    This function will print the sequence of numbers from the input to 1, the
    number of operations and will return the number of operations.
    """
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

def collatz_counts(h, t):
    """
    takes a range of numbers and returns a list of tuples of the integers and
    the collatz operation counts for each
    """
    r = range(h, t+1)
    c = [collatz(i) for i in range(h, t+1)]
    return list(zip(r, c))

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

#     Print out the letters of the alphabet along with their index (a is 1, b is 2, c is 3)

def lower_alpha_to_int(s):
    return ord(s.lower())-96

#     Write a program that takes a word (or any input) and calculates the word value according the the alphabet index created above (i.e. cat == 3 + 1 + 20 == 24)

def string_to_int(s):
    sum = 0
    for j in [ord(i.lower())-96 for i in s]:
        sum += j
    return sum


#     What if the word has uppercase letters? Account for those in your next solution.
