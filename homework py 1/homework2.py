# Задание 1

a = str(input('Введите первое число: '))
b = str(input('Введите второе число: '))
c = str(input('Введите третье число: '))
print('Ваше число:', a+b+c)

# Задание 2

num = input('Введите четырехзначное число: ')
if len(num) != 4:
    print('Ошибка! Напишите не меньше четырех чисел!')
else:
    ar = (list(map(int, str(num))))
    print('Произведение цифр:', ar[0]*ar[1]*ar[2]*ar[3])

# Задание 3

meters = int(input('Введите количество метров: '))
print('В сантиметрах:', meters*100)
print('В дециметрах:', meters*10)
print('В миллиметрах:', meters*1000)
print('В милях:', meters*0.00062)

# Задание 4

base = int(input('Введите размер основания: '))
height = int(input('Введите размер высоты: '))
print('Площадь треугольника:', int((base*height)/2))

# Задание 5

num2 = input('Введите четырехзначное число: ')
if len(num2) != 4:
    print('Ошибка! Напишите не меньше четырех чисел!')
else:
    num2 = num2[::-1]
    print('Число наоборот:', num2)
