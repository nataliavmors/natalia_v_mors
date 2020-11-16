def get_combinations_with_r(s,n):
    from itertools import combinations_with_replacement
    res = combinations_with_replacement(s,n)
    res = list(res)
    res.sort()
    return res

s = input()
n = int(input())
rrr = get_combinations_with_r(s,n)
kkk = list()
for i in rrr:
    elem = str()
    for j in range(n):
        j=(i[j])
        #print(j)
        elem += j
    #print(elem)
    kkk.append(elem)
    #print(kkk)
print(kkk)