# Задание 1
new_str = lambda str1: ''.join([i for i in str1 if i not in 'aeioyuAEIOYU'])
print(new_str(str(input('enter the string: '))))

# Задание 2
new_str2 = lambda str2: all(x.isalpha() or x.isspace() for x in str2)
print(new_str2(str(input('enter the string: '))))

# Задание 3
nums = lambda x: x[0] * nums(x[1:]) if x else 1
print(nums([int(x) for x in input('enter the numbers with ",": ').split(',')]))

# Задание 4
palindrome = lambda strs: [x for x in strs if x[:] == x[::-1]]
print(palindrome([str(x) for x in input('enter the words with ", ": ').split(', ')]))

# Задание 5
new_num = lambda num: all(num % y != 0 for y in range(2, num))
print(new_num(int(input('enter the number: '))))

# Задание 6
fact = lambda x: 1 if x == 0 else x * fact(x-1)
print(fact(int(input('enter the number: '))))