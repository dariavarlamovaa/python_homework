import random


# Задание 1
# def find_greatest_div(a: int, b: int):
#     return find_greatest_div(b, a % b) if b != 0 else a
#
#
# print(f'the largest division of two integers is {find_greatest_div(12, 8)}')
# print(f'the largest division of two integers is {find_greatest_div(100, 8)}')
# print(f'the largest division of two integers is {find_greatest_div(10, 0)}')

# Задание 2. Bulls and cows game
# def generate_game_number():
#     digits = list(range(10))
#     random.shuffle(digits)
#     if digits[0] == 0:
#         digits[0], digits[1] = digits[1], digits[0]
#     digits = digits[:4]
#     return digits
#
#
# def count_bulls_and_cows(user_number, game_number):
#     bulls = 0
#     cows = 0
#     for i in range(4):
#         if user_number[i] == game_number[i]:
#             bulls += 1
#         elif user_number[i] in game_number:
#             cows += 1
#     return bulls, cows
#
#
# def bulls_and_cows_game(game_number, attempts=0):
#     user_number = input('enter a four-digit number: ')
#     if len(user_number) != 4 or not user_number.isdigit():
#         print('incorrect input! try again')
#         return bulls_and_cows_game(game_number, attempts)
#     user_number = list(map(int, user_number))
#
#     bulls, cows = count_bulls_and_cows(user_number, game_number)
#     print(f'{bulls} bulls, {cows} cows')
#
#     if bulls == 4:
#         print(f'you did it! it took you {attempts+1} attempts')
#         return
#     return bulls_and_cows_game(game_number, attempts+1)
#
#
# secret_num = generate_game_number()
# print('welcome to the bulls and cows game!')
# print('guess the 4-digit number(digits are unique)')
# bulls_and_cows_game(secret_num)