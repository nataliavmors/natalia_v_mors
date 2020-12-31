with open("D:\programming.txt", "r") as file:
   # print(file.read())
   for line in file:
        i=0
        t=0
        #print(len(line))
        while line[i]==" ":
           i += 1
        n = i
        #if len(line)== 2:
           #k=0
        #else:
        for p in range(len(line)-i, len(line)):
            t += 1
            if line[p]==" ":
                #print(t)
                 break
        k = len(line)-n-t
        print(line[n:len(line)-k])
