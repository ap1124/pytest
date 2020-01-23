import re

def sum_f(strl):
    res = 0
    for iter1 in strl:
        res += float(iter1)
    return res

str1 = input("Enter the list: ")
rstr = re.split(r'[;,\s]\s*',str1)
print(rstr,sum_f(rstr))
