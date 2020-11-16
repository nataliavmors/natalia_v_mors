def get_cartesian_product(a,b):
    from itertools import product
    return list(map(list, product(a,b)))

a = input()
b = input()
print(get_cartesian_product(a,b))
