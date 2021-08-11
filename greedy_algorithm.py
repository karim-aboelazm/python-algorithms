numbers = [3,4,2,9,8,4,5]
def greedy_algo(x):
    x = sorted(x)
    y = []
    for i in range(len(x)//2):
        y.append((x[i] , x[~i]))  
    return y 

for i in greedy_algo(numbers):
    print(i)
