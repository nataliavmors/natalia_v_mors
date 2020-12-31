with open("D:\programming.txt", "r") as file:
   # print(file.read())
   for line in file:
       i=0
       while line[i]==" ":
           line = line[1:]
       while line[len(line)-1]==" ":
           line = line[:-1]
       print(line)

