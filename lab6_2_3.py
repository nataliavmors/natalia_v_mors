
# объем параллелепипеда, построенного на 3-х векторах

class Vector():
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __matmul__(self, other):
        x1 = self.y * other.z - self.z * other.y
        y1 = -self.x * other.z + self.z * other.x
        z1 = self.x * other.y - self.y * other.x
        return Vector(x1, y1, z1)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)


ax, ay, az = map(int, input().split())
bx, by, bz = map(int, input().split())
cx, cy, cz = map(int, input().split())
v1 = Vector(ax, ay, az)
v2 = Vector(bx, by, bz)
v3 = Vector(cx, cy, cz)
c = v1 @ v2
cc = v3 * c
S = (cc.x + cc.y + cc.z)/3
print(S)