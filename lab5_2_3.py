class Animal():
    def __init__(self,n,a):
        self.name=n
        self.age=a

class Zebra(Animal):
    def __init__(self,n,a):
        self.name=n
        self.age=a
        self.legs=4

class Dolphin(Animal):
    def __init__(self,n,a):
        self.name=n
        self.age=a
        self.tails=1
n1='кузя'
n2='валера'
n3='Гриша'
a1=16
a2=4
a3=54
animal=Animal(n1,a1)
dolph=Dolphin(n3,a3)
zeb=Zebra(n2,a2)
print('\n',animal.name,animal.age,'\n',dolph.name,dolph.age,dolph.tails,'\n',zeb.name,zeb.age,zeb.legs)