# ----------add json and pickle for packing and unpacking data------------

# task 1
# import json
# import pickle


# class Auto:
#     def __init__(self):
#         self.manufacturer = None
#         self.model = None
#         self.year = None
#         self.engine_capacity = None
#         self.color = None
#         self.price = None
#
#     def fill_it_up(self):
#         self.manufacturer = input('enter manufacturer`s name: ').capitalize()
#         self.model = input('enter car`s model: ').capitalize()
#         self.year = input('enter car`s year of release: ')
#         self.engine_capacity = input('enter car`s engine capacity: ')
#         self.color = input('enter its color: ').capitalize()
#         self.price = input('enter its price: ')
#
#     def print_it_out(self):
#         print(f'manufacturer: {self.manufacturer}\n'
#               f'model: {self.model}\n'
#               f'year of release: {self.year}\n'
#               f'engine capacity: {self.engine_capacity}\n'
#               f'color: {self.color}\n'
#               f'price: {self.price}')
#
#
#     def load_data_pickle(self, filename):
#         with open(filename, 'rb') as f:
#             try:
#                 data = pickle.load(f)
#                 self.__dict__.update(data)
#             except Exception:
#                 print('UNPACKING ERROR')
#
#     def save_data_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self.__dict__, f)
#             print(f'data was save in {filename}')
#
#
#     def load_data_json(self, filename):
#         try:
#             with open(filename, 'r') as f:
#                 data = json.load(f)
#                 new_data = data.get(self.__class__.__name__)
#                 self.manufacturer = new_data.get("manufacturer")
#                 self.model = new_data.get("model")
#                 self.year = new_data.get("year")
#                 self.engine_capacity = new_data.get("engine_capacity")
#                 self.color = new_data.get("color")
#                 self.price = new_data.get("price")
#         except Exception:
#             print('ERROR')
#
#     def save_data_json(self, filename):
#         json_string = {self.__class__.__name__: self.__dict__}
#         with open(filename, 'w') as f:
#             json.dump(json_string, f)
#
#
# auto1 = Auto()
# auto1.fill_it_up()
# print('______________')
# auto1.save_data_pickle('file.txt')
# auto1.load_data_pickle('file.txt')
# auto1.print_it_out()
# auto1.save_data_json('file.json')
# auto1.load_data_json('file.json')
# print('______________')
# auto1.print_it_out()

# task 2

# class Book:
#     def __init__(self):
#         self.title = ''
#         self.year = ''
#         self.publisher = ''
#         self.genre = ''
#         self.author = ''
#         self.price = ''
#
#     def fill_it_up(self):
#         self.title = input('enter the title of the book: ')
#         self.author = input('enter autor`s name: ')
#         self.year = input('enter the year of it`s release: ')
#         self.publisher = input('enter its publishing house: ')
#         self.genre = input('enter its genre: ')
#         self.price = input('enter book`s price: ')
#
#     def print_it_out(self):
#         print(f'title: {self.title}\n'
#               f'author: {self.author}\n'
#               f'year of release: {self.year}\n'
#               f'publishing house: {self.publisher}\n'
#               f'genre: {self.genre}\n'
#               f'price: {self.price}')
#
#
#     def load_data_pickle(self, filename):
#         with open(filename, 'rb') as f:
#             try:
#                 data = pickle.load(f)
#                 self.__dict__.update(data)
#             except Exception:
#                 print('UNPACKING ERROR')
#
#     def save_data_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self.__dict__, f)
#
#
#     def load_data_json(self, filename):
#         try:
#             with open(filename, 'r') as f:
#                 data = json.load(f)
#                 new_data = data.get(self.__class__.__name__)
#                 self.title = new_data.get("title")
#                 self.author = new_data.get("author")
#                 self.year = new_data.get("year")
#                 self.publisher = new_data.get("publisher")
#                 self.genre = new_data.get("genre")
#                 self.price = new_data.get("price")
#         except Exception:
#             print('ERROR')
#
#     def save_data_json(self, filename):
#         json_string = {self.__class__.__name__: self.__dict__}
#         with open(filename, 'w') as f:
#             json.dump(json_string, f)


# book1 = Book()
# book1.fill_it_up()
# print('---------------')
# book1.save_data_pickle('file.txt')
# book1.load_data_pickle('file.txt')
# book1.save_data_json('file.json')
# book1.load_data_json('file.json')
# book1.print_it_out()

# task 3
# class Stadium:
#     def __init__(self, name, date_of_opening, country, city, capacity):
#         self.name = name
#         self.date_of_opening = date_of_opening
#         self.country = country
#         self.city = city
#         self.capacity = capacity
#
#     def fill_it_up(self):
#         self.name = input('enter the name of stadium: ')
#         self.date_of_opening = input('enter the opening date: ')
#         self.country = input('enter the name of the country in which it is located: ')
#         self.city = input('enter the name of the city in which it is located: ')
#         self.capacity = input('enter its capacity: ')
#
#     def print_it_out(self):
#         print(f'stadium name: {self.name}\n'
#               f'opening date: {self.date_of_opening}\n'
#               f'country: {self.country}\n'
#               f'city: {self.city}\n'
#               f'capacity: {self.capacity}\n')
#
#     def load_data_pickle(self, filename):
#         with open(filename, 'rb') as f:
#             try:
#                 data = pickle.load(f)
#                 self.__dict__.update(data)
#             except Exception:
#                 print('UNPACKING ERROR')
#
#     def save_data_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self.__dict__, f)
#
#     def load_data_json(self, filename):
#         try:
#             with open(filename, 'r') as f:
#                 data = json.load(f)
#                 new_data = data.get(self.__class__.__name__)
#                 self.name = new_data.get("name")
#                 self.date_of_opening = new_data.get("date_of_opening")
#                 self.country = new_data.get("country")
#                 self.city = new_data.get("city")
#                 self.capacity = new_data.get("capacity")
#         except Exception:
#             print('ERROR')
#
#     def save_data_json(self, filename):
#         json_string = {self.__class__.__name__: self.__dict__}
#         with open(filename, 'w') as f:
#             json.dump(json_string, f)
#
#
# stadium1 = Stadium(name='?', date_of_opening='?', country='?', city='?', capacity='?')
# stadium1.fill_it_up()
# print('~~~~~~~~~~~~~~~~~~')
# stadium1.save_data_pickle('file.txt')
# stadium1.load_data_pickle('file.txt')
# stadium1.save_data_json('file.json')
# stadium1.load_data_json('file.json')
# stadium1.print_it_out()
