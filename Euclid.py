def gcf(a, b):
    '''Euclid's method of finding the greatest common factor
    Runtime tentatively O(b).
    Without loss of generality we can say that a>b>=0 due to the fact that gcf(b, a) will more or less immediately call gcb(a, b') such that b' is <= b. Because b<a, b modulus a will be less than b. Thus each iteration will operate on a much smaller tuple of numbers, since the steps are (after the initial use) on smaller numbers by at the very least 1, the upper bounding of the function is significantly less than b.
    '''
    if b == 0:
        return a
    else:
        return gcf(b, a%b)
