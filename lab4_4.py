
def pre_decorator(way):
    def decorator(function):
        def wrapper(*args, **kwargs):
            import time
            #print(way)
            start = time.time()
            kkk = function(*args, **kwargs)
            end = time.time()
            period = end - start
            if function(*args, **kwargs) is not None:
                inform=function(*args, **kwargs)
            else:
                inform="-"
            with open(way, "w") as file:
                file.write(str(start)+'\n'+str(*args)+'\n'+str(inform)+'\n'+str(end)+'\n'+str(period))

        return wrapper
    return decorator

way="D:\programming.txt"
@pre_decorator(way)
def even_num(numss):
    obj = []
    for i in numss:
        if i % 2 == 0:
            obj.append(i)
    a=len(obj)
    return a


nums = list(map(int, input().split()))
even_num(nums)
