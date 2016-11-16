x = 'hello'
y = 'world'
def reverse(x):
    i=0
    for i in range(0, len(x)//2):
        x[i], x[-i] = x[-i], x[i]
        i+=1
    return x

def QuickSort(A, h, t):
    if h < t:
        q = Partition(A, h, t)
        QuickSort(A, h, q-1)
        QuickSort(A, q+1, t)
    else:
        return
    return A

def Partition(A, h, t):
    x = A[t]
    i = h-1
    for j in range(h, t):
        if A[j] <= x:
            i += 1 #:C
            A[i], A[j] = A[j], A[i]
    A[i+1], A[t] = A[t], A[i+1]
    return i+1
