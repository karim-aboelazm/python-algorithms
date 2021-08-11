data = []
for i in range(1,100):
    data.append(i)

target = 22


# linear search 
def linear_search(data,target):
    for j in range(len(data)):
        if data[j]==target:
            return True
    return False

x = linear_search(data,target)
print(x)