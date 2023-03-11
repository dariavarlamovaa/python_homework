# Задание 1
num = int(input('Введите число от 1 до 100: '))
if 1 <= num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
else:
    print('Error')

# Задание 2
num2 = int(input('Введите число: '))
for i in range(8):
    print(pow(num2, i))

# Задача 3

minutes = int(input('Введите время звонка: '))
operator = input('Введите оператора: ')
if operator == 'МТС':
    print('Стоимость звонка:', int(minutes*3))
elif operator == 'Мегафон':
    print('Стоимость звонка:', int(minutes*2))
elif operator == 'Теле2':
    print('Стоимость звонка:', int(minutes*2.5))
elif operator == 'Билайн':
    print('Стоимость звонка:', int(minutes*3.5))
else:
    print('Извините, такой оператор еще не добавлен')

# Задача 4
m1 = int(input('Введите уровень продаж 1 менеджера: '))
m2 = int(input('Введите уровень продаж 2 менеджера: '))
m3 = int(input('Введите уровень продаж 3 менеджера: '))
salary_all = 200

if m1 >= 1000:
    salary1 = salary_all + (m1 * 0.08)
elif m1 <= 1000 or m1 >= 500:
    salary1 = salary_all + m1 * 0.05
else:
    salary1 = salary_all + m1 * 0.03
if m2 >= 1000:
    salary2 = salary_all + m2 * 0.08
elif m2 <= 1000 or m2 >= 500:
    salary2 = salary_all + m2 * 0.05
else:
    salary2 = salary_all + m2 * 0.03
if m3 >= 1000:
    salary3 = salary_all + m3 * 0.08
elif m3 <= 1000 or m3 >= 500:
    salary3 = salary_all + m3 * 0.05
else:
    salary3 = salary_all + m3 * 0.03
print(int(salary1), int(salary2), int(salary3))

if salary1 > salary2 and salary1 > salary3:
    print('Лучший менеджер - 1')
    salary1 += 200
if salary2 > salary1 and salary2 > salary3:
    print('Лучший менеджер - 2!')
    salary2 += 200
if salary3 > salary1 and salary3 > salary2:
    print('Лучший менеджер - 3!')
    salary3 += 200

print('Зарплата 1 менеджера ', salary1)
print('Зарплата 2 менеджера ', salary2)
print('Зарплата 3 менеджера ', salary3)