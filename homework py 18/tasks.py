# task 1
# import re
#
#
# def analysis_and_summarize_file(filename):
#     with open(filename, 'r') as f:
#         content = [line.replace('\n', '') for line in f.readlines()]
#         line_count = len(content)
#         words = re.findall(r'\b[\w]+\b', str(content))
#         frequency_of_words = {}
#         len_of_words = {}
#         sum_of_values = 0
#         count_values = 0
#
#         for word in words:
#             word = word.lower()
#             if word in frequency_of_words:
#                 frequency_of_words[word] += 1
#             else:
#                 frequency_of_words[word] = 1
#         sorted_words = sorted(frequency_of_words.items(), key=lambda x: x[1], reverse=True)
#
#         for word in words:
#             word = word.lower()
#             if word not in len_of_words:
#                 len_of_words[word] = len(word)
#             else:
#                 continue
#
#         for value in len_of_words.values():
#             sum_of_values += value
#             count_values += 1
#
#     with open('report.txt', 'w') as report:
#         report.write('Frequency of the words:\n')
#         for i in sorted_words:
#             report.write(f'{i[0]}: {i[1]}\n')
#         report.write(f'\nNumber of lines: {line_count}\n')
#         report.write(f'Average length of the word: {round(sum_of_values / count_values)}')
#
#
# analysis_and_summarize_file('f.txt')
import datetime

# task 2
# import time
#
#
# def encryption_logging(func):
#     def wrapper(filename, key):
#         date = time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime())
#         print(f'Filename: {filename}')
#         print(f'Key: {key}')
#         print(f'Date: {date}')
#         return func(filename, key)
#
#     return wrapper
#
#
# @encryption_logging
# def encrypt_file(filename, key):
#     with open(filename, 'r') as f:
#         try:
#             content = f.read()
#         except FileNotFoundError:
#             print('File was not found')
#
#         encrypted = []
#         for i, c in enumerate(content):
#             encrypted.append(chr((ord(c) + ord(key[i % len(key)])) % 127))
#     with open('encrypted.txt', 'w') as enc:
#         enc.write(''.join(encrypted))
#
#
# @encryption_logging
# def decrypt_file(filename, key):
#     with open(filename, 'r') as f:
#         try:
#             content = f.read()
#         except FileNotFoundError:
#             print('File was not found')
#
#         decrypted = []
#         for i, c in enumerate(content):
#             decrypted.append(chr((ord(c) - ord(key[i % len(key)])) % 127))
#     with open('decrypted.txt', 'w') as dec:
#         dec.write(''.join(decrypted))
#
#
# key = input('enter the key: ')
# encrypt_file('text.txt', key)
# print()
# decrypt_file('encrypted.txt', key)

# task 3
# import os
#
#
# def analysis_file_sizes(dirpath):
#     files = {}
#     try:
#         for i in os.listdir(dirpath):
#             filepath = os.path.join(dirpath, i)
#             if os.path.isfile(filepath):
#                 files[filepath] = round(os.path.getsize(filepath) * 0.0078, 3)
#             if os.path.isdir(filepath):
#                 folder_file = analysis_file_sizes(filepath)
#                 files.update(folder_file)
#         for key, value in files.items():
#             print(f'{key}: {value} KB')
#         return files
#     except FileNotFoundError:
#         print(f'Directory "{dirpath}" does not exist')
#
#
# dirpath = input('Enter directory path: ')
# analysis_file_sizes(dirpath)