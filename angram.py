stm1 = 'fairy tales'
stm2 = 'rail safety'

stm1 = stm1.replace(' ','').lower()
stm2 = stm2.replace(' ','').lower()

# two statments ara angram

def is_angram(s1,s2):
    ht = dict() # hash table

    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    
    for i in ht:
        if ht[i] !=0:
            return False
    return True


print(is_angram(stm1,stm2))