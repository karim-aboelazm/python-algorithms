A = [6,9,1,8,2,4,7,3,5]

# merge function
def merge(L,R,A):
    i,j,k = 0,0,0
    while (i < len(L)) and (j < len(R)):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while (i < len(L)):
        A[k] = L[i]
        k += 1
        i += 1
    while (j < len(R)):
        A[k] = R[j]
        k += 1
        j += 1
    
# merge sort arr 
def merge_sort(A):
    if len(A) < 2:
        return
    mid = int(len(A) / 2)
    left = A[:mid]
    right = A[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,A)
    return A


print(merge_sort(A))