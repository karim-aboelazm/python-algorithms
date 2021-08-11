data = []
for i in range(1,100):
    data.append(i)

target = 22



# iterative binary search
def binary_search_iter(data,target):
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

y = binary_search_iter(data, target)
print(y)