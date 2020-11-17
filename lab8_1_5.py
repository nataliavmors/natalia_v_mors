def compress_string(s):
    from itertools import groupby
    sss = groupby(s, lambda x: x[0])
    return sss



# в душе не знаю просто оставлю это так пока
for key, group in compress_string(s):
    for thing in group:
        print(thing[1], key)