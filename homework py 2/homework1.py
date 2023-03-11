# Задание 1
start = int(input('Введите первое число: '))
end = int(input('Введите второе число: '))
sum_e = 0
sum_o = 0
summ9 = 0
for i in range(start, end+1):
    if i % 2 != 0:
        sum_e += i
    if i % 2 == 0:
        sum_o += i
    if i % 9 == 0:
        summ9 += i
print('Сумма четных чисел:', sum_e)
print('Сумма нечетных чисел:', sum_o)
print("Сумма кратных на 9: ", summ9)

# Задание 2
a = int(input('Введите длину строки: '))
b = input('Введите символ: ')
while a > 0:
    print(b)
    a -= 1

# Задача 3
num = 0
while True:
    num = int(input('Введите число: '))
    if num == 7:
        print('Good bye!')
        break
    elif num == 0:
        print('Number is equal to zero')
    else:
        if num > 0:
            print('Number is positive')
        else:
            print('Number is negative')

# Задание 4
summ = maximum = minimum = number = 0
while number != 7:
    number = int(input('Введите число:'))
    summ += number
    if number > maximum:
        maximum = number
    elif number < minimum:
        minimum = number
    print(f'Сумма:{summ}')
    print(f'Максимум:{maximum}')
    print(f'Минимум:{minimum}')
else:
    print('Good bye!')