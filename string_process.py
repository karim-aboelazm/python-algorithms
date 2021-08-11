# spreadsheet encode column
def srpeadsheet_encode_column(str_pro):
    num = 0
    count = len(str_pro) - 1
    for s in str_pro:
        num += 26**count * (ord(s) - ord('A')+1)
        count -= 1
    return num

print(srpeadsheet_encode_column('A'))
print(srpeadsheet_encode_column('AA'))
print(srpeadsheet_encode_column('AZ'))
print(srpeadsheet_encode_column('ZZ'))
