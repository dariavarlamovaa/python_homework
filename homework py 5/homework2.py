# Задание 1
# import random
#
# n = int(input('enter the width: '))
# m = int(input('enter the length: '))
# main_matrix = [[random.randint(1, 10) for i in range(n)] for j in range(m)]
#
# for row in main_matrix:
#     for el in row:
#         print(el, end='\t')
#     print()
#
#
# def delete_highest_and_find_total(matrix):
#     total = 0
#     while matrix:
#         max_row = [max(row) for row in matrix if row]
#         if not max_row:
#             break
#         print('maximum from rows', max_row)
#         total += max(max_row)
#         for i in range(len(matrix)):
#             matrix[i].remove(max_row[i])
#         print(matrix)
#     print(f'the answer is {total}')
#     return total
#
#
# delete_highest_and_find_total(main_matrix)


# Задание 2
# def find_perimeter():
#     row = len(matrix)
#     col = len(matrix[0])
#     perimeter = 0
#     for i in range(row):
#         for j in range(col):
#             if matrix[i][j] == 1:
#                 perimeter += 4
#                 if i > 0 and matrix[i - 1][j] == 1:
#                     perimeter -= 2
#                 if j > 0 and matrix[i][j - 1] == 1:
#                     perimeter -= 2
#     print(perimeter)
#
#
# matrix = [[0, 0, 0, 0],
#           [0, 1, 1, 0],
#           [0, 1, 1, 0],
#           [0, 0, 0, 0]]
#
# find_perimeter()


# Задание 3
# n = int(input('length: '))
# m = int(input('width: '))
# matrix = [[random.randint(0, 9) for i in range(n)] for j in range(m)]
# for row in matrix:
#     print(*row)
#
#
# def transform_matrix(grid):
#     k = int(input('steps:'))
#     for _ in range(k):
#         new_matrix = [[0] * n for _ in range(m)]
#         new_matrix[0][0] = grid[m - 1][n - 1]
#         for i in range(m):
#             for j in range(n):
#                 if j < n - 1:
#                     new_matrix[i][(j + 1)] = grid[i][j]
#                 else:
#                     new_matrix[(i + 1) % m][0] = grid[i][n - 1]
#         grid = new_matrix
#     return grid
#
#
# print(transform_matrix(matrix))
