def quickSort(coll, h, t):
    #print("qs coll type: ", type(coll))
    if h < t:
        pivot = partition(coll, h, t)
        quickSort(coll, h, pivot-1)
        #print('the first partition is :', coll[h:pivot-1])
        quickSort(coll, pivot+1, t)
    else:
        return
    return coll

def partition(coll, h, t):
    print("the array being worked is:  ", coll[h:t])
    pivot = coll[t]
    i = h-1
    #print("partition coll type: ", type(coll))
    for j in range(h, t):
        #print("partition for coll type: ", type(coll))
        if coll[j] <= pivot:
            #print("partition for if coll type: ", type(coll))
            i += 1 #:C
            #print(type(coll))
            coll[i], coll[j] = coll[j], coll[i]
    coll[i+1], coll[t] = coll[t], coll[i+1]
    print("pivot is: ", coll[i+1])
    print("the array being worked is now:  ", coll[h:t])
    print("the left side is:", coll[h:i])
    print("the right side is:", coll[i+2:t])
    print("++++++++++++++++++++++++++++")
    #print(coll)
    return i+1


#list = [12, 1, 2, 4, 8]
#print(list)
#QuickSort(list, 0, 4)
#print(list)

if __name__ == '__main__':
    #try:
    arr = []
    # print(type(arr))
    arr = [int(x) for x in input('Please enter numbers seperated by spaces: ').split()]
    #arr = input('Please enter numbers seperated by spaces: ')
    #print("input type: ", type(arr))
    # print(type(arr.__len__()))
    quickSort(arr, 0, arr.__len__()-1)
    print("The sorted list is: ", arr)
    #except:
    #    print("Something went horribly wrong.")
