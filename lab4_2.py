def decorator(function):
    def wrapper():
        obj = function(nums)
        if len(obj) > 10:
            return "очень много"
        elif len(obj) == 0:
            return "нет("
        else:
            return obj
    return wrapper


def even_num(nums):
    obj = []
    for i in nums:
        if i % 2 == 0:
            obj.append(i)
    return obj


nums = list(map(int, input().split()))
print(decorator(even_num(nums)))
