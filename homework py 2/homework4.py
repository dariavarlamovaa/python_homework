# Задание 1
start = int(input("enter the first number: "))
end = int(input("enter the second number: "))
numbers = []
for number in range(start, end + 1):
    div = 0
    for i in range(1, number + 1):
        if number % i == 0:
            div += 1
    if div <= 2:
        numbers += [number]
print('Prime numbers are: ', numbers, end='\n')

# Задание 2
for i in range(1, 10 + 1):
    for j in range(1, 10 + 1):
        print(f'{i} * {j} = {i * j}', end='\t')
    print()

# Задание 3
a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))
for i in range(a, b + 1):
    for j in range(1, 10 + 1):
        print(f'{i} * {j} = {i * j}', end='\t')
    print()