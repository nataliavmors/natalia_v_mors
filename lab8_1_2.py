def get_permutations(s,n):
    from itertools import permutations
    res = permutations(s,n)
    res = list(res)
    res.sort()
    return res

s = input()
n = int(input())
rrr = get_permutations(s,n)
kkk = list()
for i in rrr:
    elem = str()
    for j in range(n):
        j=(i[j])
        elem += j
    kkk.append(elem)
print(kkk)



