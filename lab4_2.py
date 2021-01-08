def decorator(function):
    def wrapper(a):
        kkk=function(a)
        if kkk > 10:
            print("очень много")
        elif kkk == 0:
            print("нет(")
        else:
            print(len(a))
    return wrapper

@decorator
def even_num(nums):
    obj = []
    for i in nums:
        if i % 2 == 0:
            obj.append(i)
    a=len(obj)
    return a


nums = list(map(int, input().split()))
decorator(even_num(nums))
