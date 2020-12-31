with open("D:\programming.txt", "r") as file, open("D:\programming_1.txt", "w") as new_file:
    new_file.write(file.read())