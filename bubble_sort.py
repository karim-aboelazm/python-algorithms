A = [6,9,1,8,2,4,7,3,5]

# bubble sort algo
def bubble_sort(a):
    for i in range(1 , len(a) - 1):
        temp = 0
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]
                temp = 1
        if temp == 0:
            break
    return a

print(bubble_sort(A))