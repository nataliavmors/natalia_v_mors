class Mother:
    def me(self):
        print("я мама")

class Daughter(Mother):
    def me(self):
        print('я дочь')

m=Mother()
m.me()
d=Daughter()
d.me()