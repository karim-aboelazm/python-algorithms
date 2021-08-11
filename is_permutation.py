txt1_is = 'god'
txt2_is = 'dog'
txt1_not = 'not'
txt2_not = 'top'

# permutation algorithm
def is_permutation(a,b):
    a = ''.join(sorted(a)).lower()
    b = ''.join(sorted(b)).lower()

    if len(a) != len(b):
        return False
        
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

print(is_permutation(txt1_is,txt2_is))
print(is_permutation(txt1_not,txt2_not))
    