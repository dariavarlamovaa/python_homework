# Задание 1
# def sort_sort(nums):
#     pivot = len(nums) // 3
#     if sum(nums) / len(nums) > 0:
#         pivot *= 2
#     return sorted(nums[:pivot]) + nums[pivot:][::-1]
#
#
#
#
# print(sort_sort([8, 6, 3, 0, 5, 2, 9, 1, 4, 7]))
# print(sort_sort([-3,-5,-6,-4,-3,5]))

# Задание 2
# def get_grades():
#     grades = []
#     for x in range(10):
#         while True:
#             n = int(input(f'enter your {x + 1} grade: '))
#             if 12 >= n >= 1:
#                 grades.append(n)
#                 break
#             else:
#                 print('invalid number. number should be from 1 to 12')
#     return grades
#
#
# def performance(grades):
#     while True:
#         print('---------------')
#         command = int(input('1 - view grades\n'
#                             '2 - change the grade\n'
#                             '3 - check scholarship availability\n'
#                             '4 - sort the grades\n'
#                             '0 - exit\n'
#                             'enter the command: '))
#         if command == 1:
#             print('your grades are:')
#             print(*grades, sep=', ')
#         elif command == 2:
#             while True:
#                 change_grade = input('enter the grade number in the list: ')
#                 if 10 >= int(change_grade) >= 1 or not change_grade.isdigit():
#                     change_grade = int(change_grade)
#                     break
#                 else:
#                     print('invalid number. the grade number in the list should be from 1 to 10')
#             while True:
#                 new_grade = input('enter the new grade: ')
#                 if 12 >= int(new_grade) >= 1:
#                     grades[change_grade - 1] = int(new_grade)
#                     print(*grades, sep=', ')
#                     break
#                 else:
#                     print('invalid number. number should be from 1 to 12')
#         elif command == 3:
#             average_of_grades = sum(grades) / len(grades)
#             print('your average score is', average_of_grades)
#             if average_of_grades > 10.7:
#                 print('yes, you can have a scholarship')
#             else:
#                 print('no, you can not have a scholarship')
#         elif command == 4:
#             while True:
#                 sort_number = int(input('enter 1, if you wanna sort grades in ascending order\n'
#                                         'enter 2, if in descending order: '))
#                 if sort_number != 1 and sort_number != 2:
#                     print('error. enter the number 1 or 2')
#                 elif sort_number == 1:
#                     grades.sort()
#                     print('grades were sorted in ascending order')
#                     print(grades)
#                     break
#                 elif sort_number == 2:
#                     grades.sort(reverse=True)
#                     print('grades were sorted in descending order')
#                     print(grades)
#                     break
#         elif command == 0:
#             print('bye-bye')
#             break
#         else:
#             print('incorrect input. try again')
#             pass
#
#
# performance(get_grades())


# Задание 3
# def improved_bubble_sort():
#     nums = [8, 7, 4, 2, 9]
#     swapped = True
#     total = 0
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 swapped = True
#         total += 1
#     return nums, total
#
#
# print(improved_bubble_sort())
