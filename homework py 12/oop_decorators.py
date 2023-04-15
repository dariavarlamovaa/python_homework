# task 1
# class Fraction:
#     count = 0
#
#     def __init__(self, numerator, denominator):
#         self.n = numerator
#         self.d = denominator
#
#     def addition(self):
#         Fraction.count += 1
#         return f'addition = {self.n + self.d}'
#
#     def subtraction(self):
#         Fraction.count += 1
#         return f'subtraction = {self.n - self.d}'
#
#     def multiplication(self):
#         Fraction.count += 1
#         return f'multiplication = {self.n * self.d}'
#
#     def division(self):
#         Fraction.count += 1
#         return f'division = {self.n / self.d}'
#
#     @staticmethod
#     def counter():
#         print(f'counter = {Fraction.count}')
#
#
# a = Fraction(3, 5)
# print(a.multiplication())
# Fraction.counter()
# print(a.addition())
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