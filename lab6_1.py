class Complex:

    def __init__(self, real, imag):
        self.real=real
        self.imag=imag

    def __add__(self,other):
        z =self.real+other.real
        i =self.imag + other.imag
        return Complex(z,i)

    def __sub__(self, other):
        z =self.real-other.real
        i =self.imag - other.imag
        return Complex(z,i)

    def __mul__(self, other):
        z = self.real - other.real
        i = self.imag + other.imag
        return Complex(z,i)

    def __truediv__(self, other):
        z=(self.real * other.real + self.imag * other.y) / (other.real * other.real + other.imag * other.imag)
        i=(-self.real * other.y + self.imag * other.real) / (other.real * other.real + other.imag * other.imag)
        return Complex(z,i)

    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2)**0.5


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
a = Complex(x1, y1)
b = Complex(x2, y2)
z1 = a + b
z2 = a - b
z3 = a * b
z4 = a / b
print('a + b =', z1.x, '+', z1.y, 'i')
print('a - b =', z2.x, '+', z2.y, 'i')
print('a * b =', z3.x, '+', z3.y, 'i')
print('a / b =', z4.x, '+', z4.y, 'i')
MA = abs(a)
z5a = (MA.x + MA.y)**(1/2)
MB = abs(b)
z5b = (MB.x + MB.y)**(1/2)
print('|a| =', z5a)
print('|b| =', z5b)






