# task 1
# from abc import ABC, abstractmethod
#
#
# class Command(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#
#
# class TurnLightsOn(Command):
#     def __init__(self, light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_on()
#
#
# class TurnLightsOff(Command):
#     def __init__(self, light):
#         self.light = light
#
#     def execute(self):
#         self.light.turn_off()
#
#
# class Light:
#     @staticmethod
#     def turn_on():
#         print('Lights on')
#
#     @staticmethod
#     def turn_off():
#         print('Lights off')
#
#
# class Switch:
#     def __init__(self, on_cmd, off_cmd):
#         self.on_cmd = on_cmd
#         self.off_cmd = off_cmd
#
#     def on(self):
#         self.on_cmd.execute()
#
#     def off(self):
#         self.off_cmd.execute()
#
#
# lightning = Light()
# lights_on = TurnLightsOn(lightning)
# lights_off = TurnLightsOff(lightning)
# switch = Switch(lights_on, lights_off)
# switch.on()
# switch.off()


# 2.
# class Numbers:
#     def __init__(self, filepath):
#         self.filepath = filepath
#         self.numbers = []
#
#     def load_numbers(self):
#         with open(self.filepath, 'r') as f:
#             for num in f.read().split(', '):
#                 self.numbers.append(int(num))
#             return self.numbers
#
#
# class NumbersProxy:
#     def __init__(self):
#         self.filepath = input('enter the file name: ')
#         self.numbers = Numbers(self.filepath).load_numbers()
#         self.log_file = input('enter the log-file name: ')
#
#     @staticmethod
#     def logging(func):
#         def wrapper(self, *args, **kwargs):
#             with open(self.log_file, 'a') as f:
#                 f.write(f'{func.__name__} method was called\n')
#             return func(self, *args, **kwargs)
#
#         return wrapper
#
#     @logging
#     def get_sum(self):
#         return sum(self.numbers)
#
#     @logging
#     def get_max(self):
#         return max(self.numbers)
#
#     @logging
#     def get_min(self):
#         return min(self.numbers)
#
#
# n = NumbersProxy()
# while True:
#     print('-'*20)
#     command = input('1. sum\n'
#                     '2. max\n'
#                     '3. min\n'
#                     '0. exit\n'
#                     'enter the command: ')
#     if command == '1':
#         print(f'sum is {n.get_sum()}')
#     elif command == '2':
#         print(f'max is {n.get_max()}')
#     elif command == '3':
#         print(f'min is {n.get_min()}')
#     elif command == '0':
#         print('bye-bye')
#         break
#     else:
#         print('invalid input. try again')


# task 3
# import json
#
#
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.is_available = True
#
#
# class Librarian:
#     @staticmethod
#     def check_book_availability(book):
#         if book.is_available:
#             return 'the book is available'
#         else:
#             return 'the book is not available'
#
#     @staticmethod
#     def add_book_to_library(book, library):
#         library.add_book(book)
#
#
# class Reader:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#
#     def take_book(self, book, library):
#         if library.find_books(title=book.title, author=book.author, year=book.year, available_only=True):
#             self.books.append(book)
#             book.is_available = False
#             return 'now the book is yours'
#         else:
#             return 'the book can not be taken'
#
#     def return_book(self, book, library):
#         if book in self.books:
#             self.books.remove(book)
#             book.is_available = True
#             library.add_book(book)
#             return 'the book is returned'
#         else:
#             return 'the book was not found'
#
#
# class Library:
#     def __init__(self):
#         self.books = []
#         self.librarians = []
#         self.readers = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def remove_book(self, book):
#         self.books.remove(book)
#
#     def find_books(self, title=None, author=None, year=None, available_only=False):
#         result = []
#         for book in self.books:
#             if ((title is None) or (book.title == title)) and ((author is None) or (book.author == author)) and (
#                     (year is None) or (book.year == year)):
#                 if (not available_only) or book.is_available:
#                     result.append(book)
#         return result
#
#     def add_reader(self, reader):
#         self.readers.append(reader)
#
#     def remove_reader(self, reader):
#         self.readers.remove(reader)
#
#     def find_readers(self, name=None):
#         result = []
#         for reader in self.readers:
#             if name is None or reader.name == name:
#                 result.append(reader)
#         return result
#
#     def save_readers(self, filename):
#         data = {
#             'books': [{'title': book.title, 'author': book.author, 'year': book.year, 'is_available': book.is_available}
#                       for book in self.books],
#             'readers': [{'name': reader.name, 'books': [book.title for book in reader.books]} for reader in
#                         self.readers]
#         }
#         with open(filename, 'w') as f:
#             json.dump(data, f)
#
#     def load(self, filename):
#         with open(filename, 'r') as f:
#             data = json.load(f)
#             books_data = data['books']
#             for book_data in books_data:
#                 book = Book(book_data['title'], book_data['author'], book_data['year'])
#                 book.is_available = book_data['is_available']
#                 self.add_book(book)
#
#             readers_data = data['readers']
#             for reader_data in readers_data:
#                 reader = Reader(reader_data['name'])
#                 self.add_reader(reader)
#                 for book_title in reader_data['books']:
#                     books = self.find_books(title=book_title, available_only=False)
#                     if books:
#                         reader.books.append(books[0])
#                         books[0].is_available = False
#
#
# librarian = Librarian()
# library = Library()
# reader1 = Reader('Leo')
# book1 = Book("b1", "a1", 2000)
# book2 = Book("b2", "a2", 2010)
# library.add_book(book1)
# library.add_book(book2)
#
# library.add_reader(reader1)
#
# print(librarian.check_book_availability(book1))
#
# reader1.take_book(book1, library)
