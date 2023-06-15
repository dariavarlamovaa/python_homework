# task 1

# class Customers:
#     def __init__(self):
#         self.customers = {}
#
#
# class Products:
#     def __init__(self):
#         self.products = {}
#
#
# class CustomerManager(Customers):
#     def add_customer(self, name, email):
#         self.customers[name] = email
#
#     def update_customer(self, name, new_email):
#         self.customers[name] = new_email
#
#     def get_customer(self, name):
#         print(f'{name} - {self.customers.get(name)}')
#
#
# class ProductInventory(Products):
#     def add_product(self, prod_name, price):
#         self.products[prod_name] = price
#
#     def update_product(self, prod_name, new_price):
#         self.products[prod_name] = new_price
#
#     def get_product(self, prod_name):
#         print(f'{prod_name} - {self.products.get(prod_name)}')


# task 2

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def add_book(self):
#         print(f'Title: {self.title}\n'
#               f'Author: {self.author}')
#
#
# class FictionBook(Book):
#     def __init__(self, title, author, genre):
#         super().__init__(title, author)
#         self.genre = genre
#
#     def add_book(self):
#         super().add_book()
#         print(f'Genre: {self.genre}')
#
#
# class NonFictionBook(Book):
#     def __init__(self, title, author, field):
#         super().__init__(title, author)
#         self.field = field
#
#     def add_book(self):
#         super().add_book()
#         print(f'Genre: {self.field}')
#
#
# class ReferenceBook(Book):
#     def __init__(self, title, author, subject):
#         super().__init__(title, author)
#         self.subject = subject
#
#     def add_book(self):
#         super().add_book()
#         print(f'Genre: {self.subject}')

# task 3
# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
#     @abstractmethod
#     def calculate_perimeter(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         print(self.radius ** 2 * 3.14)
#
#     def calculate_perimeter(self):
#         print(self.radius * 2 * 3.14)
#
#
# class Rectangle(Shape):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def calculate_area(self):
#         print(self.x * self.y)
#
#     def calculate_perimeter(self):
#         print(2 * (self.x + self.y))
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c, height):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.height = height
#
#     def calculate_area(self):
#         print(self.a * self.height * 0.5)
#
#     def calculate_perimeter(self):
#         print(self.a + self.b + self.c)


# task 4
# class TextMessaging:
#     @staticmethod
#     def send_text_message(message):
#         print(f'{message} was sent')
#
#     @staticmethod
#     def receive_text_message(res_mes):
#         print(f'You received one message - {res_mes}')
#
#     @staticmethod
#     def get_message_history(all_messages):
#         print(all_messages)
#
#
# class MultimediaMessaging:
#     @staticmethod
#     def send_multimedia_message(self, media):
#         print(f'{media} was sent')
#
#     @staticmethod
#     def receive_multimedia_message(self, media):
#         print(f'You received one message - {media}')
#
#     @staticmethod
#     def view_media_gallery(all_messages):
#         print(all_messages)


# task 5
# from abc import ABC, abstractmethod
#
#
# class Logger(ABC):
#     @abstractmethod
#     def log_info(self, data):
#         pass
#
#     @abstractmethod
#     def log_warning(self, data):
#         pass
#
#     @abstractmethod
#     def log_error(self, data):
#         pass
#
#
# class ConsoleLogger(Logger):
#     def log_info(self, data):
#         print(f'Info: {data}')
#
#     def log_warning(self, data):
#         print(f'Warning: {data}')
#
#     def log_error(self, data):
#         print(f'Error: {data}')
#
#
# class FileLogger(Logger):
#     def __init__(self, filename):
#         self.filename = filename
#
#     def log_info(self, data):
#         with open(self.filename, 'a') as f:
#             f.write(f'Info: {data}')
#
#     def log_warning(self, data):
#         with open(self.filename, 'a') as f:
#             f.write(f'Warning: {data}')
#
#     def log_error(self, data):
#         with open(self.filename, 'a') as f:
#             f.write(f'Error: {data}')
#
#
# class DatabaseLogger(Logger):
#     def __init__(self):
#         self.database = {}
#
#     def log_info(self, data):
#         self.database[data] = 'Info'
#
#     def log_warning(self, data):
#         self.database[data] = 'Warning'
#
#     def log_error(self, data):
#         self.database[data] = 'Error'
