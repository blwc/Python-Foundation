def gcf(a, b):
    '''Euclid's method of finding the greatest common factor'''
    if b == 0:
        return a
    else:
        return gcf(b, a%b)
