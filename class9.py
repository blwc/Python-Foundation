#x = range(10)
#(str(i)+'s') for i in x



# Here's our collatz:
#[i//2 if even(i) else i*3+1 for i in x]

def reverse(s):
    return s[::-1]

def palindrome(s):
    pal = ''.join([ i for i in str(s).lower() if i.isalpha()])
    return pal == reverse(pal)
