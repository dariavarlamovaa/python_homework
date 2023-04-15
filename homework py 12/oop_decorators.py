# task 1
# from fractions import Fraction as Frac


# class Fraction:
#     count = 0

#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         Fraction.count += 1

#     @property
#     def numerator(self):
#         return self._numerator

#     @numerator.setter
#     def numerator(self, value):
#         self._numerator = value

#     @property
#     def denominator(self):
#         return self._denominator

#     @denominator.setter
#     def denominator(self, value):
#         if value == 0:
#             raise ValueError('the denominator can not be 0!')
#         else:
#             self._denominator = value

#     def __add__(self, other):
#         x = self.numerator * other.denominator + self.denominator * other.numerator
#         y = self.denominator * other.denominator
#         return f'the result is {Fraction.__simplify(x, y)}'

#     def __sub__(self, other):
#         x = self.numerator * other.denominator - self.denominator * other.numerator
#         y = self.denominator * other.denominator
#         return f'the result is {Fraction.__simplify(x, y)}'

#     def __mul__(self, other):
#         x = self.numerator * other.numerator
#         y = self.denominator * other.denominator
#         return f'the result is {Fraction.__simplify(x, y)}'

#     def __truediv__(self, other):
#         x = self.numerator * other.denominator
#         y = self.denominator * other.numerator
#         return f'the result is {Fraction.__simplify(x, y)}'

#     @staticmethod
#     def __simplify(numerator, denominator):
#         return Frac(numerator, denominator)

#     @staticmethod
#     def counter():
#         print(f'counter = {Fraction.count}')


# f1 = Fraction(3, 7)
# f2 = Fraction(2, 9)

# print(f1 + f2)
# print(f1 - f2)
# print(f1 * f2)
# print(f1 / f2)

# Fraction.counter()


# task 2
# class Temperature:
#     count = 0
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def convert_to_celsius(t):
#         Temperature.count += 1
#         return round((t - 32) * (5 / 9), 2)
#
#     @staticmethod
#     def convert_to_fahrenheit(t):
#         Temperature.count += 1
#         return round(t * (9 / 5) + 32, 2)
#
#     @staticmethod
#     def counter():
#         return f'counter = {Temperature.count}'
#
#
# a = Temperature()
# print(a.convert_to_fahrenheit(26))
# print(a.convert_to_celsius(87))
# print(a.counter())

# task 3
# class EnglishSystem:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def convert_cm_to_inches(num):
#         return f'{num} cm = {round(num * 0.3937, 2)} inches'
#
#     @staticmethod
#     def convert_cm_to_ft(num):
#         return f'{num} cm = {round(num * 0.0328, 2)} ft'
#
#     @staticmethod
#     def convert_km_to_miles(num):
#         return f'{num} km = {round(num * 0.6214, 2)} miles'
#
#     @staticmethod
#     def convert_kg_to_pounds(num):
#         return f'{num} kg = {round(num * 2.2046, 2)} pounds'
#
#     @staticmethod
#     def convert_litres_to_gallons(num):
#         return f'{num} litres = {round(num * 0.22, 2)} gallons'
#
#
# m = EnglishSystem()
# print(m.convert_kg_to_pounds(10))
# print(m.convert_cm_to_inches(175))
# print(m.convert_cm_to_ft(10))
# print(m.convert_litres_to_gallons(19))
# print(m.convert_km_to_miles(245))
