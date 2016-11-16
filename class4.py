def for_loop():
    for i in range(5):
        for letter in 'abcde':
            print(i, letter)

def leap_year(y):
    #check input type is an int
    if y % 400 == 0:
        print(str(y) + 'is a leap year!')
    elif y % 100 == 0:
        print('Sorry, ' + str(y) + ' is not a leap year.')
    elif y % 4 == 0:
        print(str(y) + 'is a leap year!')
    else:
        print('Sorry, ' + str(y) + ' is not a leap year.')

"""
*args
arbitrary number of arguements
"""
def greet(*names):
    for name in names:
        print('hello', name)
"""
**kwargs key word arguements
need more info...
"""
def myrange(**things):
    for key, val in things.items():
        print(key, 'is', val)

#isinsistance('hello', str)

def bool_leap_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

def leap_beens():
#   for i in range(2016, 1996, -1):
    for i in range(2016-20, 2016):
        if bool_leap_year(i):
            print(str(i))

def two_things():
    return 1, 2
