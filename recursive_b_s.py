data = []
for i in range(1,100):
    data.append(i)
target = 22

# recursive binary search
def binary_search_recu(data,target,low,high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recu(data, target, low, mid-1)
        else:
            return binary_search_recu(data, target, mid + 1, high)

z = binary_search_recu(data,target,0 ,len(data)-1)
print(z)