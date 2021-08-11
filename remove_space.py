string = 'Was it a cat I Saw'

# check stm is plandrom or not 
def is_plandrom(s):
    i = 0 
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
        stm = ''.join([i for i in s if i.isalpha()]).replace(' ','').lower()
    return True , stm
        

print(is_plandrom(string))