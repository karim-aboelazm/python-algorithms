txt1 = 'racocar'
txt2 = 'this is not'

#  palindrome
def is_palindrome(text):
    text = text.replace(' ','').lower()
    ht = dict()
    
    for i in text:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    odd_count = 0

    for k,v in ht.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(is_palindrome(txt1))
print(is_palindrome(txt2))
