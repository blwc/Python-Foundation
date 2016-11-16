"""

"""
INC_ALPHA = ('M',  'D', 'C', 'L', 'X', 'V', 'I')
INC_NUM =   (1000, 500, 100, 50,  10,  5,   1)
ROMAN = ''
NUMBER = -1

def check_latest_numeral (num, curr):
    """

    """
    global ROMAN
    while num - INC_NUM[curr] >= 0:
        ROMAN += INC_ALPHA[curr]
        num -= INC_NUM[curr]
    if curr % 2: #odd index
        if num - (INC_NUM[curr] - INC_NUM[curr + 1] ) >= 0 :
            ROMAN += INC_ALPHA[curr + 1]
            ROMAN += INC_ALPHA[curr]
            num -= ( INC_NUM[curr] - INC_NUM[curr + 1] )
    else: #even index
        if num - (INC_NUM[curr] - INC_NUM[curr + 2] ) >= 0 :
            ROMAN += INC_ALPHA[curr + 2]
            ROMAN += INC_ALPHA[curr]
            num -= ( INC_NUM[curr] - INC_NUM[curr + 2] )
    return num

def romanize () :
    """

    """
    global NUMBER
    for curr in range(7):
        NUMBER = check_latest_numeral(NUMBER, curr)
        if NUMBER == 0:
            break
    #this for loop as a while
    # i = 0
    #while i <7
        #do something
        #i +=1

if __name__ == '__main__':
    try:
        NUMBER = int(input('Enter a positive integer: '))
    except:
        print("Please enter a positive integer.")
    if NUMBER < 1 :
        print('Sorry, please try a positive integer.')
    elif NUMBER > 100000:
        print('Now, lets not be too hasty, try a smaller number.')
    else:
        romanize()
        print('The roman numeral of your number is: ' + ROMAN)
