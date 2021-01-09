
# площадь параллелограма, построенного на  2-ух векторах

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


ax, ay, az = map(int, input().split())
bx, by, bz = map(int, input().split())
v1 = Vector(ax, ay, az)
v2 = Vector(bx, by, bz)
c = v1 @ v2
S = (c.x * c.x + c.y * c.y + c.z * c.z)**(1/2)
print(S)