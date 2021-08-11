A = [6,9,1,8,2,4,7,3,5]

#  selection sort algo

def selection_sort(a):
    for i in range(0 , len(a)-1):
        init = i
        for j in range(i+1,len(a)):
            if a[j] < a[init]:
                init = j
        a[i],a[init] = a[init],a[i]
    return a

print(selection_sort(A))