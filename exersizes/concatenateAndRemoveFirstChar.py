"""
Read two strings from the user and print their concatenation, without the first character of each. The strings will be at least length 1
E.g.: 'Hello', 'There' → 'ellohere'
"""
if __name__ == '__main__':
    try:
        string1 = str(input('Enter your first String: '))
        string2 = str(input('Enter your second String: '))
        print(string1[1:] + string2[1:])
    except:
        print('Looks like something went wrong...')
