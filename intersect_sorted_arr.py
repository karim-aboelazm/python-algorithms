A = [2,3,3,5,7,11]
B = [3,3,7,15,31]

def intersect_sorted_arr(A,B):
    i,j = 0,0
    inter = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if A[i] != A[i - 1 ]:
                inter.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return set(inter)

print(intersect_sorted_arr(A,B)) 