A = [6,9,1,8,2,4,7,3,5]

# insertion sort algo
def insertion_sort(a):
    for i in range(1 , len(a)):
        temp = a[i]
        empty = i
        while (empty > 0 and a[empty -1] > temp):
            a[empty] = a[empty -1]
            empty = empty - 1
        a[empty] = temp
    return a

print(insertion_sort(A))