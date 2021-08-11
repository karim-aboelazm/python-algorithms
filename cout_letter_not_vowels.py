str_1 = 'Welcome'
str_2 = 'Python'

vowels = 'aeiou'

# iterative count letters not vowels
def iterative_count_consonants(string):
    count = 0
    for i in range(len(string)):
        if string[i].lower() not in vowels and string[i].isalpha():
            count += 1
    return count

# recursive count letters not vowels
def recursive_count_consonants(string):
    if string == '':
        return 0
    if string[0].lower() not in vowels and string[0].isalpha():
        return 1 + recursive_count_consonants(string[1:])
    else:
        return recursive_count_consonants(string[1:])


print(iterative_count_consonants(str_1))
print(iterative_count_consonants(str_2))

print(recursive_count_consonants(str_1))
print(recursive_count_consonants(str_2))
