# Задача 1
import random
matrix = [[random.randint(10, 1000) for i in range(10)]for j in range(10)]
nums = []
for row in matrix:
    for num in row:
        print(num, end='\t')
    print()
for i in range(10):
    for j in range(10):
        if 100 < matrix[i][j] < 1000:
            nums.append(matrix[i][j])
print(nums)
res = [(sum(map(int, str(i)))) for i in nums]
print(res)
five_res = [i for i in res if i % 5 == 0]
print(five_res)
# OR
# five_res = []
# for i in res:
#     if res[i] % 5 == 0:
#         five_res.append(res[i])
# print(five_res)
print(f'there are {len(five_res)} three-digit numbers,'
      f' the sum of the digits of each '
      f'of which is a multiple of 5')

# Задача 2
n = int(input("width: "))
m = int(input("length: "))
matrix = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = abs(i) + abs(j)

for row in matrix:
    for num in row:
        print(num, end='\t')
    print()


# Задача 3
matrix = [[random.randint(0, 10) for i in range(5)]for j in range(5)]
for row in matrix:
    for num in row:
        print(num, end='\t')
    print()

min_sum = float('inf')
min_line = []
for i in matrix:
    row_sum = sum(i)
    if row_sum < min_sum:
        min_sum = row_sum
        min_line = i
for j in range(5):
    col_sum = sum(matrix[i][j] for i in range(5))
    if col_sum < min_sum:
        min_sum = col_sum
        min_line = [matrix[i][j] for i in range(5)]
print('the minimum line is:')
for i in range(5):
    print(min_line[i])
print()