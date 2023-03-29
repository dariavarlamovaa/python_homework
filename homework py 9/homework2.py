# Задание 1
# def directory():
#     users_ids = [4, 5, 1, 3, 2]
#     users_phones = [89114093434, 89419034855, 89545323431, 89319090953, 89619121232]
#     while True:
#         print('---------------')
#         command = int(input('1 - sort by identification numbers\n'
#                             '2 - sort by phone numbers\n'
#                             '3 - show the list of IDs and phone numbers\n'
#                             '0 - exit\n'
#                             'enter the command: '))
#         if command == 1:
#             swapped = True
#             while swapped:
#                 swapped = False
#                 for j in range(len(users_ids) - 1):
#                     if users_ids[j] > users_ids[j+1]:
#                         users_ids[j], users_ids[j+1] = users_ids[j+1], users_ids[j]
#                         users_phones[j], users_phones[j+1] = users_phones[j+1], users_phones[j]
#                         swapped = True
#             print('the lists were sorted by ids')
#         elif command == 2:
#             swapped = True
#             while swapped:
#                 swapped = False
#                 for j in range(len(users_phones) - 1):
#                     if users_phones[j] > users_phones[j+1]:
#                         users_phones[j], users_phones[j+1] = users_phones[j+1], users_phones[j]
#                         users_ids[j], users_ids[j+1] = users_ids[j+1], users_ids[j]
#                         swapped = True
#             print('the lists were sorted by phone numbers')
#         elif command == 3:
#             print('id\tphone')
#             for i in range(len(users_ids)):
#                 print(f'{users_ids[i]}\t{users_phones[i]}')
#         elif command == 0:
#             print('bye-bye')
#             break
#         else:
#             print('incorrect input, try again')
#             pass
#
#
# directory()


# Задание 2
# def books():
#     titles = ['Война и Мир', 'Преступление и наказание', 'Идиот', 'Братья Карамазовы', 'Бедная Лиза']
#     years = [1863, 1865, 1867, 1878, 1792]
#     while True:
#         print('---------------')
#         command = int(input('1 - отсортировать по названиям книг\n'
#                             '2 - отсортировать по годам выпуска \n'
#                             '3 - показать список книг с названиями и годами выпуска\n'
#                             '0 - выйти\n'
#                             'введите команду: '))
#         if command == 1:
#             swapped = True
#             while swapped:
#                 swapped = False
#                 for j in range(len(titles) - 1):
#                     if titles[j] > titles[j+1]:
#                         titles[j], titles[j+1] = titles[j+1], titles[j]
#                         years[j], years[j+1] = years[j+1], years[j]
#                         swapped = True
#             print('список был отсортирован по названиям книг')
#         elif command == 2:
#             swapped = True
#             while swapped:
#                 swapped = False
#                 for j in range(len(years) - 1):
#                     if years[j] > years[j+1]:
#                         years[j], years[j+1] = years[j+1], years[j]
#                         titles[j], titles[j+1] = titles[j+1], titles[j]
#                         swapped = True
#             print('список был отсортирован по годам выпуска')
#         elif command == 3:
#             print('год\tназвание')
#             for i in range(len(years)):
#                 print(f'{years[i]}\t{titles[i]}')
#         elif command == 0:
#             print('пока-пока')
#             break
#         else:
#             print('неверный ввод. попробуйте еще раз')
#             pass
#
#
# books()
