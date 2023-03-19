# Задание 1
# def repeat_until(func, p):
#     def closure(x):
#         while not p(x):
#             x = func(x)
#         return x
#     return closure
#
#
# def half(x):
#     return x // 2
#
#
# def is_even(x):
#     return x % 2 == 0
#
#
# repeat_until_half_even = repeat_until(half, is_even)
# print(repeat_until_half_even(99))


# Задание 2
# def make_counter(n):
#     def closure():
#         nonlocal n
#         if n > -1:
#             print(n)
#             n -= 1
#         else:
#             print('error. counter has reached 0')
#     return closure
#
#
# c = make_counter(3)
# c()
# c()
# c()
# c()
# c()


# Задание 3
# def print_once(func):
#     execution = False
#
#     def closure():
#         nonlocal execution
#         if execution is False:
#             execution = True
#             print(func)
#             return func
#         return
#     return closure
#
#
# def hello_world():
#     return 'hello, world!'
#
#
# once = print_once(hello_world())
# once()
# once()
# once()
# once()
