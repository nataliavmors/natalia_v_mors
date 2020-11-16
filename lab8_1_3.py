def get_combinations(s,n):
    from itertools import combinations
    res = combinations(s,n)
    res = list(res)
    res.sort()
    return res

s = input()
n = int(input())
kkk = list()
for t in range(1,n+1):
    rrr = get_combinations(s,t)
    for i in rrr:
        elem = str()
        for j in range(t):
            j = (i[j])
            elem += j
        kkk.append(elem)
print(kkk)