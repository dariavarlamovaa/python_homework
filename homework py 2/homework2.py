# Задание 1
start, end = int(input('Введите начало: ')), int(input('Введите конец: '))
for i in range(start, end + 1):
    if i % 7 == 0:
        print(i)

# Задание 2
a, b = int(input('Введите начало: ')), int(input('Введите конец: '))
all_numbers = []
numbers7 = []
numbers5 = []
for i in range(a, b + 1):
    all_numbers.append(i)
for j in range(a, b + 1):
    if j % 7 == 0:
        numbers7.append(j)
    if j % 5 == 0:
        numbers5.append(j)
print('Все числа диапазона:', all_numbers)
print('Все числа диапазона в убывающем порядке:', all_numbers[::-1])
print('Числа диапазона, кратные 7:', numbers7)
print('Количество чисел, кратных 5:', len(numbers5))

# Задача 3
c, b = int(input('Введите начало: ')), int(input('Введите конец: '))
for k in range(c, b + 1):
    if k % 3 == 0 and k % 5 == 0:
        print('Fizz Buzz')
    elif k % 3 == 0:
        print('Fizz')
    elif k % 5 == 0:
        print('Buzz')
    else:
        print(k)