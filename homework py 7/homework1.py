# Задание 1
# countries = {'Russia', 'Finland', 'Latvia', 'Ukraine', 'USA'}
# print(countries)
#
#
# def func():
#     while True:
#         command = int(input('enter the command (1-add, 2-del, 3-find, 4-check): '))
#         if command == 1:
#             countries.add(input('enter the new country: '))
#             print(countries)
#         elif command == 2:
#             countries.discard(input('enter the county to delete: '))
#             print(countries)
#         elif command == 3:
#             find = input('enter the symbols: ').lower()
#             print(tuple(country for country in countries if country.lower().startswith(find)))
#         elif command == 4:
#             con = input('enter the country to check: ')
#             print(countries.isdisjoint(con))
#         else:
#             print('incorrect input. try again')
#             pass
#
#
# func()

# Задание 2
# a1 = {'Petroskoi', 'Helsinki', 'Tampere', 'Joensuu'}
# a2 = {'Joensuu', 'Oulu', 'Petroskoi', 'Kemi'}
# a3 = a1.intersection(a2)
# print(a3)

# Задание 3
# b1 = {'Petroskoi', 'Helsinki', 'Tampere', 'Joensuu'}
# b2 = {'Joensuu', 'Oulu', 'Petroskoi', 'Kemi'}
# b3 = b1.difference(b2)
# print(b3)

# Задание 4
# c1 = {'Petroskoi', 'Helsinki', 'Tampere', 'Joensuu'}
# c2 = {'Joensuu', 'Oulu', 'Petroskoi', 'Kemi'}
# c3 = c2.difference(c1)
# print(c3)

# Задание 5
# d1 = {'Petroskoi', 'Helsinki', 'Tampere', 'Joensuu'}
# d2 = {'Joensuu', 'Oulu', 'Petroskoi', 'Kemi'}
# d3 = d1 | d2
# print(d3)

# Задание 6
# cities = {'Russia': 'Moscow', 'Finland': 'Helsinki', 'Turkey': 'Istanbul'}
# print(cities)
#
#
# def dict_func():
#     while True:
#         command = int(input('enter the command (1-add, 2-del, 3-check, 4-change): '))
#         if command == 1:
#             country = input('enter the county to add: ').capitalize()
#             cities[country] = input('enter the city to add: ').capitalize()
#             print(cities)
#         elif command == 2:
#             del cities[input('enter the country to del: ').capitalize()]
#             print(cities)
#         elif command == 3:
#             find = input('enter the country to check: ').capitalize()
#             for key, value in cities.items():
#                 if key in find:
#                     print(f'yes, this country is in the dictionary.\n{key}: {value}')
#                 else:
#                     print('no, this country is not in the dictionary')
#                     break
#         elif command == 4:
#             country = input('enter the country to change: ').capitalize()
#             for key in cities.keys():
#                 if key == country:
#                     cities[country] = input('enter the new city of this country: ').capitalize()
#                 else:
#                     print('this country is not in the dictionary')
#                     break
#             print(cities)
#         else:
#             print('incorrect input. try again')
#             pass
#
#
# dict_func()