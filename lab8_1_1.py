def get_cartesian_product(a,b):
    from itertools import product
    return product(a,b)

a=input()
b=input()
print(a,b)
print(get_cartesian_product(a,b))
