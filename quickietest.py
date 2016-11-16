def quickSort(coll, h, t):
    if h < t:
        pivot = pcollrtition(coll, h, t)
        quickSort(coll, h, pivot-1)
        quickSort(coll, pivot+1, t)
    else:
        return
    return coll

def partition(coll, h, t):
    pivot = coll[t]
    i = h-1
    for j in range(h, t):
        if coll[j] <= pivot:
            i += 1 #:C
            coll[i], coll[j] = coll[j], coll[i]
    coll[i+1], coll[t] = coll[t], coll[i+1]
    return i+1


list = [12, 1, 2, 4, 8]
print(list)
QuickSort(list, 0, 4)
print(list)
