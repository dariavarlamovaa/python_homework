# task 1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def perimeter(self):
#         return self.radius * 2 * 3.14
#
#     def __eq__(self, other):
#         return self.perimeter == other.perimeter
#
#     def __ne__(self, other):
#         return self.perimeter != other.perimeter
#
#     def __lt__(self, other):
#         return self.perimeter < other.perimeter
#
#     def __le__(self, other):
#         return self.perimeter <= other.perimeter
#
#     def __gt__(self, other):
#         return self.perimeter > other.perimeter
#
#     def __ge__(self, other):
#         return self.perimeter >= other.perimeter
#
#     def __add__(self, other):
#         self.radius = self.radius + other
#         return self
#
#     def __radd__(self, other):
#         self.radius = other + self.radius
#         return self
#
#     def __sub__(self, other):
#         self.radius = self.radius - other
#         return self
#
#     def __rsub__(self, other):
#         self.radius = other - self.radius
#         return self
#
#     def __iadd__(self, other):
#         self.radius += other
#         return self
#
#     def __isub__(self, other):
#         self.radius -= other
#         return self
#
#     def __str__(self):
#         return f'Perimeter is {self.perimeter}'
#
#
# a = Circle(10)
# b = Circle(7)
# print(a == b)
# print(a != b)
# print(a < b)
# print(a <= b)
# print(a > b)
# print(a >= b)
# a + 8
# print(a)
# b + 10
# print(b)
# a += 90
# print(a)
# b += 18
# print(b)


# task 2
# class Complex:
#     def __init__(self, real=0, imaginary=0):
#         self.real = real
#         self.imaginary = imaginary
#
#     def __add__(self, other):
#         real = self.real + other.real
#         imaginary = self.imaginary + other.imaginary
#         return Complex(real, imaginary)
#
#     def __sub__(self, other):
#         real = self.real - other.real
#         imaginary = self.imaginary - other.imaginary
#         return Complex(real, imaginary)
#
#     def __mul__(self, other):
#         real = self.real * other.real - self.imaginary * other.imaginary
#         imaginary = self.real * other.imaginary + self.imaginary * other.real
#         return Complex(real, imaginary)
#
#     def __truediv__(self, other):
#         if other.real == 0 or other.imaginary == 0:
#             raise ZeroDivisionError('you cannot divide by zero')
#         conjugate = Complex(other.real, -other.imaginary)
#         numerator = self * conjugate
#         denominator = other * conjugate
#         return Complex(numerator.real / denominator.real, numerator.imaginary / denominator.real)
#
#     def __repr__(self):
#         return f"{self.real}, {self.imaginary}"
#
#     def __str__(self):
#         if self.imaginary > 0:
#             return f'{round(self.real, 2)} + {round(self.imaginary, 2)}i'
#         return f'{round(self.real, 2)} - {round(abs(self.imaginary), 2)}i'
#
#
# a = Complex(4, 5)
# b = Complex(3, 7)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# task 3
# class Airplane:
#     def __init__(self, aircraft_type, passengers, capacity):
#         self.aircraft_type = aircraft_type
#         self.passengers = passengers
#         self.capacity = capacity
#
#     def __eq__(self, other):
#         return self.aircraft_type.lower() == other.aircraft_type.lower()
#
#     def __add__(self, other):
#         self.passengers = self.passengers + other
#         return self
#
#     def __radd__(self, other):
#         self.passengers = other + self.passengers
#         return self
#
#     def __sub__(self, other):
#         self.passengers = self.passengers - other
#         return self
#
#     def __rsub__(self, other):
#         self.passengers = other - self.passengers
#         return self
#
#     def __iadd__(self, other):
#         self.passengers += other
#         return self
#
#     def __isub__(self, other):
#         self.passengers -= other
#         return self
#
#     def __lt__(self, other):
#         return self.capacity < other.capacity
#
#     def __le__(self, other):
#         return self.capacity <= other.capacity
#
#     def __gt__(self, other):
#         return self.capacity > other.capacity
#
#     def __ge__(self, other):
#         return self.capacity >= other.capacity
#
#     def __str__(self):
#         return f'{self.passengers}'
#
#
# c = Airplane('R18', 15, 35)
# d = Airplane('R20', 23, 30)
#
# print(c == d)
# print(c < d)
# print(c <= d)
# print(c > d)
# print(c >= d)
# print(c + d)
# print(10 + c)
# print(90 - c)
# c += 10
# print(c)
# c -= 20
# print(c)

# task 4
# class Flat:
#     def __init__(self, square, price):
#         self.square = square
#         self.price = price
#
#     def __eq__(self, other):
#         return self.square == other.square
#
#     def __ne__(self, other):
#         return self.square != other.square
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __le__(self, other):
#         return self.price <= other.price
#
#     def __gt__(self, other):
#         return self.price > other.price
#
#     def __ge__(self, other):
#         return self.price >= other.price
#
#
# f1 = Flat(120, 100000)
# f2 = Flat(50, 20000)
# print(f1 == f2)
# print(f1 != f2)
# print(f1 < f2)
# print(f1 <= f2)
# print(f1 > f2)
# print(f1 >= f2)