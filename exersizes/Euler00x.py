def sum_3s5s(x):
    sum = 0
    for i in range(1, x+1):
        if not i%3:
            sum += i
        elif not i%5:
            sum += i
    return sum

def fib():
    """
    returns an array of fibonacci numbers up to 4000000
    """
    old = 0
    new = 1
    sum = 0
    arr = [0,]
    while sum < 4000000:
        arr.append(new)
        sum = old + new
        old = new
        new = sum
    return arr

def sum_even(a):
    sum = 0
    for i in a:
        if not i%2:
            sum += i
    return sum

def eratosthenes_sieve(limit):
    import math
    A = [True for i in range(2, limit)]
    for i in range(2, int(math.sqrt(limit)) + 1 ):
        if A[i] == True:
            j = 0
            while ((i*i + j*i) < int(math.sqrt(limit)) ):
                A[i*i + j*i ] = False
                j += 1
    return A[:int(math.sqrt(limit))]

def not_prime_factors(x):
    factors = []
    for i in range(2, x):
        if not x%i:
            factors.append(i)
            print(i)
    return factors

def max_prime_factors(x):
    f = not_prime_factors(x)
    for i in f[::-1]:
        if not_prime_factors(i) == []:
            return print("answer is: " + str(i))
    return None
