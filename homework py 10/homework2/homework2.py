# import re

# task 1
# with open('file1_task1', 'r') as f1, open('file2_task1', 'r') as f2:
#     lines1 = f1.readlines()
#     lines2 = f2.readlines()
#     if f1 == f2:
#         print('all lines are the same')
#     for line in lines1:
#         if line not in lines2:
#             print(line, end='')
#     for line in lines2:
#         if line not in lines1:
#             print(line, end='')

# task 2
# with open('file1_task2.txt', 'r') as f1, open('file2_task2.txt', 'w') as f2:
#     content = f1.readlines()
#     symbols = 0
#     rows = len(content)
#     vowels = 0
#     consonants = 0
#     digits = 0
#     for i in content:
#         for j in i:
#             if j.isalpha():
#                 symbols += 1
#             if j.isdigit():
#                 digits += 1
#             if re.match(r'[АЕЁИОУЫЭЮЯаеёиоуыэюя]', j):
#                 vowels += 1
#             if re.match(r'[БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ]', j):
#                 consonants += 1
#
#     f2.write(f'Количество символов: {symbols}\n'
#              f'Количество строк: {rows}\n'
#              f'Количество гласных букв: {vowels}\n'
#              f'Количество согласных букв: {consonants}\n'
#              f'Количество цифр: {digits}')

# task 3
# with open('file1_task3.txt') as f1, open('file2_task3.txt', 'w') as f2:
#     lines = f1.readlines()
#     last_line = lines[-1]
#     f2.write(last_line)
# with open('file1_task3.txt', 'w') as f1w:
#     f1w.writelines([line for line in lines[:-1]])

# task 4
# with open('file1_task2.txt', 'r') as f:
#     maximum = float('-inf')
#     content = f.readlines()
#     for line in content:
#         if len(line) > maximum:
#             maximum = len(line)
#     print(f'Длина самой длинной строки = {maximum}')

# task 5
# with open('file1_task2.txt', 'r') as f:
#     word = input('введите слово, которое надо найти: ').lower()
#     content = f.read().lower()
#     counter = content.count(word)
#     if counter == 0:
#         print(f'слово {word} не было найдено в тексте')
#     else:
#         print(f'слово "{word}" было найдено в тексте {counter} раз')

# task 6
# with open('file1_task2.txt', 'r') as f:
#     change_word = input('введите слово для замены: ')
#     new_word = input('введите новое слово: ')
#     content = f.read().strip()
#     content = content.replace(change_word, new_word)
#     print(content)
# with open('file1_task2.txt', 'w') as ff:
#     ff.write(content)