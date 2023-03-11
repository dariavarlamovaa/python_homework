# Задание 1
from random import randint
import math


def count_primes(numbers):
    counter = 0
    for number in numbers:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            counter += 1
    return counter


example_nums = [randint(1, 100) for _ in range(10)]
print(f'random numbers: {example_nums}')
print(f'there are {count_primes(example_nums)} prime numbers in the list')


# Задача 2


def delete_items(numbers):
    n = int(input('number to delete: '))
    counter = 0
    for i in numbers:
        if i == n:
            numbers.remove(i)
            counter += 1
    return counter


nums = [randint(1, 11) for _ in range(10)]
print(f'numbers: {nums}')
print(f'{delete_items(nums)} numbers were deleted')
print(f'new list: {nums}')

# Задание 3


def count_negatives(matrix):
    negatives = 0
    for i in range(4):
        for j in range(4):
            if matrix[i][j] < 0:
                negatives += 1
    return negatives


main_matrix = [[randint(-20, 10) for _ in range(4)] for _ in range(4)]
for row in main_matrix:
    print(*row, sep='\t')

print(f'there are {count_negatives(main_matrix)} negative numbers in the matrix')

# Задание 4


def calculate_square():
    f = int(input('select the shape (1-triangle, 2-rectangle, 3-circle): '))
    if f == 1:
        a, b, c = int(input('enter the side 1: ')), int(input('enter the side 2: ')), \
            int(input('enter the side 3: '))
        p = (a + b + c) / 2
        square = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
    elif f == 2:
        a, b = int(input('enter the side 1: ')), int(input('enter the side 2: '))
        square = a * b
    elif f == 3:
        a = int(input('enter the radius: '))
        square = round(math.pi*(a**2), 6)
    else:
        print('Error!')
    return square


print(f'the square is {calculate_square()}')