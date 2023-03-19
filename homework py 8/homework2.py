# Задание 1
# def retry(num):
#     def decorator(func):
#         total = 0
#
#         def wrapper(*args, **kwargs):
#             nonlocal total
#             if total >= num:
#                 raise ValueError('too many calls')
#             total += 1
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
#
# @retry(3)
# def random_func():
#     print('hello, world')
#
#
# random_func()
# random_func()
# random_func()
# random_func()


# Задание 2
# def validate_args(*types):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(len(args)):
#                 if type(args[i]) is not types[i]:
#                     raise TypeError('you have entered incorrect data types. try again')
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @validate_args(int, str)
# def random_func(num: int, string: str):
#     print(f'{num} is {"int"}')
#     print(f'{string} is {"str"}')
#
#
# random_func(3, 'cool')
# random_func(3, 9)
# random_func('3', 'hello')
