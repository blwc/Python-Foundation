

def reverse(s):
    return s[::-1]

def palindrome(s):
    pal = ''.join([ i for i in str(s).lower() if i.isalpha()])
    return pal == reverse(pal)

if __name__ == '__main__':
    try:
        the_string = str(input('Enter a palindrome: '))
    except:
        print("Looks like soemthing went wrong!")
    palindrome(the_string)
