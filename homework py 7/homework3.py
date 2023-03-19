# Задание 1
# data = {'Michael Jordan': 198, 'Kobe Bryant': 198, 'Stephen Curry': 188, 'Shaquille O`Neal': 216,
#         'Michael Brooks': 190}
#
#
# def basketball():
#     while True:
#         print('--------------')
#         print(data)
#         command = int(input('enter the command (1-add, 2-del, 3-find, 4-change, 0-exit): '))
#         if command == 1:
#             new_player = input('enter the name of the player to add: ').title().strip()
#             data[new_player] = int(input('enter his height in centimetres: '))
#             print('the player was successfully added')
#         elif command == 2:
#             del_player = input('enter the name of the player to delete: ').title().strip()
#             players_to_del = []
#             for key in data.keys():
#                 if del_player.lower() in key.lower():
#                     players_to_del.append(key)
#             if players_to_del:
#                 if len(players_to_del) == 1:
#                     deleted_name = players_to_del[0]
#                     del data[deleted_name]
#                     print(f'{deleted_name} was deleted')
#                 else:
#                     print('matching players are:')
#                     for index, element in enumerate(players_to_del):
#                         print(f"{index + 1}. {element}")
#                     pl_to_del = int(input('enter the number of the matching player to delete: '))
#                     if pl_to_del > len(players_to_del) or pl_to_del <= 0:
#                         print('error! incorrect input.')
#                     else:
#                         del data[players_to_del[pl_to_del - 1]]
#                         print(f'{players_to_del[pl_to_del - 1]} was deleted')
#             else:
#                 print('sorry. this player is not in the list')
#         elif command == 3:
#             find_player = input('enter the name of the player to find: ').strip()
#             matching_players = []
#             for key in data.keys():
#                 if find_player.lower() in key.lower():
#                     matching_players.append(key)
#             if matching_players:
#                 if len(matching_players) == 1:
#                     player_name = matching_players[0]
#                     print(f"{player_name} is {data[player_name]} centimetres tall.")
#                 else:
#                     print('matching players are:')
#                     for player in matching_players:
#                         print(f"{player} is {data[player]} centimetres tall.")
#                     print()
#             else:
#                 print('sorry. this player is not in the list')
#         elif command == 4:
#             change_player = input('enter the name of the player you want to change: ').strip()
#             new_name = input('enter the new player`s name: ').title().strip()
#             players_to_change = []
#             for key in data.keys():
#                 if change_player.lower() in key.lower():
#                     players_to_change.append(key)
#             if players_to_change:
#                 if len(players_to_change) == 1:
#                     data.pop(players_to_change[0])
#                     data[new_name] = int(input(f'enter the new height of {new_name}: '))
#                 else:
#                     print('matching players are:')
#                     for index, element in enumerate(players_to_change):
#                         print(f"{index + 1}. {element}")
#                     pl_to_change = int(input('enter the number of the matching player to change: '))
#                     if pl_to_change > len(players_to_change) or pl_to_change <= 0:
#                         print(f'error! incorrect input.')
#                     else:
#                         data.pop(players_to_change[pl_to_change - 1])
#                         data[new_name] = int(input(f'enter the new height of {new_name}: '))
#                         print(f'{players_to_change[pl_to_change - 1]} '
#                               f'was changed to {new_name}: {data[new_name]}')
#             else:
#                 print('sorry. this player is not in the list')
#         elif command == 0:
#             print('bye-bye!')
#             break
#         else:
#             print('incorrect input.try again')
#             pass
#
#
# basketball()

# Задание 3
# def add_employee(employees):
#     name = input('full name: ').title().strip()
#     phone = input('phone number: ').strip()
#     email = input('email: ').strip()
#     job = input('job title: ').capitalize().strip()
#     cabinet = input('cabinet number: ').strip()
#     skype = input('skype: ').strip()
#     employees[name] = {'phone': phone, 'email': email, 'job_title': job, 'cabinet': cabinet, 'skype': skype}
#     print('the employee was successfully added')
#
#
# def del_employee(employees):
#     name = input('enter the employee`s name: ')
#     matching_employees = []
#     for key in employees.keys():
#         if name.lower() in key.lower():
#             matching_employees.append(key)
#     if matching_employees:
#         if len(matching_employees) == 1:
#             employee_name = matching_employees[0]
#             del employees[employee_name]
#             print(f'{employee_name} was deleted from the database')
#         else:
#             print('matching employees are:')
#             for index, person in enumerate(matching_employees):
#                 print(f"{index + 1}. {person}")
#             num = int(input('enter the number of the matching employee to delete: '))
#             del employees[matching_employees[num - 1]]
#             print(f'{matching_employees[num - 1]} was deleted from the database')
#     else:
#         print(f'{name} was not found')
#
#
# def find_employee(employees):
#     name = input('enter the employee`s name: ')
#     matching_employees = []
#     for key in employees.keys():
#         if name.lower() in key.lower():
#             matching_employees.append(key)
#     if matching_employees:
#         if len(matching_employees) == 1:
#             employee_name = matching_employees[0]
#             print(f'{employee_name} : {employees[employee_name]}')
#         else:
#             print('matching employees are:')
#             for employee in matching_employees:
#                 print(f'{employee} : {employees[employee]}')
#     else:
#         print(f'sorry. {name} is not in the database')
#
#
# def replace_employee(employees):
#     name = input('enter the employee`s name: ')
#     matching_employees = []
#     for key in employees.keys():
#         if name.lower() in key.lower():
#             matching_employees.append(key)
#     if matching_employees:
#         if len(matching_employees) == 1:
#             employee_name = matching_employees[0]
#             phone = input('phone number: ').strip()
#             email = input('email: ').strip()
#             job = input('job title: ').capitalize().strip()
#             cabinet = input('cabinet number: ').strip()
#             skype = input('skype: ').strip()
#             employees[employee_name] = {'phone': phone, 'email': email, 'job_title': job, 'cabinet': cabinet,
#                                         'skype': skype}
#             print(f'{employee_name}`s has been successfully changed')
#
#         else:
#             print('matching employees are:')
#             for index, person in enumerate(matching_employees):
#                 print(f"{index + 1}. {person}")
#             num = int(input('enter the number of the matching employee to replace: '))
#             phone = input('phone number: ').strip()
#             email = input('email: ').strip()
#             job = input('job title: ').capitalize().strip()
#             cabinet = input('cabinet number: ').strip()
#             skype = input('skype: ').strip()
#             employees[matching_employees[num - 1]] = {'phone': phone, 'email': email, 'job_title': job,
#                                                       'cabinet': cabinet,
#                                                       'skype': skype}
#             print(f'{matching_employees[num - 1]}`s info has been successfully changed')
#     else:
#         print(f'{name} was not found in the database')
#
#
# def firm():
#     employees = {
#         'Chris Wall': {"phone": '+2903939303', "email": 'chris_wall@gmail.com', "job_title": 'Director', "cabinet": '1',
#                        "skype": 'chris0222'},
#         'Chris Board': {"phone": '+4839849234', "email": 'chris_board@gmail.com', "job_title": 'Project manager',
#                         "cabinet": '8', "skype": 'chris7772'},
#         'Frank Lion': {"phone": '+3334443343', "email": 'frank_frank@gmail.com', "job_title": 'Junior developer',
#                        "cabinet": '9', "skype": 'frank_frank09'}}
#     while True:
#         print('---------------------')
#         for e in employees:
#             print(f'{e}: {employees[e]}', end='\n')
#         print()
#         command = int(input('enter the command (1-add, 2-del, 3-find, 4-replace, 0-exit): '))
#         if command == 1:
#             add_employee(employees)
#         elif command == 2:
#             del_employee(employees)
#         elif command == 3:
#             find_employee(employees)
#         elif command == 4:
#             replace_employee(employees)
#         elif command == 0:
#             print('bye-bye')
#             break
#         else:
#             print('incorrect input. try again')
#             pass
#
#
# firm()