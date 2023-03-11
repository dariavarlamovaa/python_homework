# # Задание 1
# import random
# n = int(input('enter the length of the array: '))
# people = [input(f'enter the {_+1} name: ').capitalize() for _ in range(n)]
# heights = [random.randint(150, 200) for _ in range(n)]
# print(f'names: {people}')
# print(f'heights: {heights}')
#
# data = list(range(len(heights)))
# data.sort(key=lambda i: heights[i], reverse=True)
# print(f'sorted names by their height:{[people[i] for i in data]}')
#
# # Задание 2
# k = int(input('enter the length of the array: '))
# nums = [random.randint(0, 100) for _ in range(k)]
# print(nums)
# counter = 0
#
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] == nums[j] and i < j:
#             counter += 1
#             print(nums[i], nums[j])
# print(f'number of good pairs: {counter}')
#
# # Задание 3
# p = int(input('enter the length of the array: '))
# numbers = [random.randint(1, 10) for _ in range(p)]
# print(f'nums: {numbers}')
# res = []
# counter = 0
#
# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if j != i and numbers[j] < numbers[i]:
#             counter += 1
#     res.append(counter)
#     counter = 0
# print(f'output: {res}')
