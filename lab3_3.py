import shutil
import os

shutil.unpack_archive('D:\main.zip',
                      'D:\main', 'zip')
list = []
for dpath, dnames, finames in os.walk('D:\main'):
     for dirname in dnames:
          for filename in finames:
               if filename.endswith('.py') and dirname not in list:
                    list.append(dirname)

list.sort()

with open('D:\oop.txt', 'w') as file:
     for line in range(len(list)):
          file.write(list[line])
          file.write('\n')