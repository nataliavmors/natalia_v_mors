
# центр масс

class Vector():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y, self.z / other.z)


n = int(input())
ax, ay, az = map(int, input().split())
v1 = Vector(ax, ay, az)
while n - 1 != 0:
    bx, by, bz = map(int, input().split())
    v2 = Vector(bx, by, bz)
    v1 = v1 + v2
    n -= 1
nnn = Vector(n, n, n)
c = v1 / nnn
print(c.x, c.y, c.z)