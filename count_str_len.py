string = 'Welcome To My New Course'

# iterative count string length

def iterative_str_len(x):
    count = 0 
    for i in range(len(x)):
        count += 1
    return count

# recursive count string lenght

def recursive_str_len(x):
    if x == '':
        return 0
    else:
        return 1 + recursive_str_len(x[1:])

# print(len(string))
# print(iterative_str_len(string))
# print(recursive_str_len(string))

    