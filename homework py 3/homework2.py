import random
# ПЕРЕДЕЛАННОЕ ЗАДАНИЕ
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

# Задание 1
numbers = input('enter the expression: ')
try:
    if '+' in numbers:
        num1, num2 = numbers.split('+')
        print(int(num1) + int(num2))
    elif '-' in numbers:
        num1, num2 = numbers.split('-')
        print(int(num1) - int(num2))
    elif '*' in numbers:
        num1, num2 = numbers.split('*')
        print(int(num1) * int(num2))
    elif '/' in numbers:
        num1, num2 = numbers.split('/')
        print(int(num1) / int(num2))
    else:
        print('ERROR!')
except ValueError:
    print('ERROR')

# Задача 2
nums_range = list(range(-10, 10))
nums = random.sample(nums_range, 10)
negatives = 0
positives = 0
zeros = 0
print(nums)
print(f'maximum number is {max(nums)}')
print(f'minimum number is {min(nums)}')
for x in nums:
    if x < 0:
        negatives += 1
print(f'there are {negatives} negative number(s)')
for x in nums:
    if x > 0:
        positives += 1
print(f'there are {positives} positive number(s)')
for x in nums:
    if x == 0:
        zeros += 1
print(f'there are {zeros} zero(s)')