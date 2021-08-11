name_1 = 'karim'
name_2 = 'karim'
name_3 = 'KARim'
name_4 = 'karim'
name_5 = 'karim'

# find upper letter 
def find_upper_litter(name):
    for i in range(len(name)):
        if name[i].isupper():
            return name[i]
    return 'no upper letters found !'

x = find_upper_litter(name_1)
x1 = find_upper_litter(name_2)
x2 = find_upper_litter(name_3)
x3 = find_upper_litter(name_4)
x4 = find_upper_litter(name_5)
print(x)
print(x1)
print(x2)
print(x3)
print(x4)