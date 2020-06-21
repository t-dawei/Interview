from functools import cmp_to_key

dic={'and': 2, 'are': 2, 'the':4, 'is':2, 'it':3, 'you':3, 'a':1}

def cmp(a,b):
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        if a[0] > b[0]:
            return 1
        else:
            return -1

print(sorted(dic.items(), key=cmp_to_key(cmp), reverse=True))
