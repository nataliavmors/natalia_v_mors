

def decorator(function):
    def wrapper(*args,**kwargs):

        import time
        start = time.time()
        kkk = function(*args,**kwargs)
        end = time.time()
        period = end - start
        inform = []
        inform.append(start)
        inform.append(*args)
        if function(*args,**kwargs) is not None:
            inform.append(function(*args,**kwargs))
        else:
            inform.append("-")
        inform.append(end)
        inform.append(period)
        with open(way, "w") as file:
            file.write(str(inform))
    return wrapper


@decorator
def even_num(nums):
    obj = []
    for i in nums:
        if i % 2 == 0:
            obj.append(i)
    a=len(obj)
    return a

way="D:\programming.txt"
nums = list(map(int, input().split()))
decorator(even_num(nums))
