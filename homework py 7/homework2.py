# Задание 1
a1 = (1, 2, 3, 4, 5, 6, 7)
a2 = (2, 3, 1, 4, 5, 6, 9)
a3 = (6, 5, 4, 8, 9, 3, 7)
a4 = set(a1).intersection(a2).intersection(a3)
print(f'common elements: {tuple(a4)}')

# Задание 2
b1 = (1, 2, 3, 4, 5, 6, 7, 3, 4, 2, 5, 4, 6, 8)
b2 = (2, 3, 1, 4, 5, 6, 9, 9, 7, 5, 3, 2, 1, 5)
b3 = (6, 5, 4, 8, 9, 3, 7, 5, 4, 6, 3, 4, 8, 9)
print('unique elements(1): ', tuple(set(b1)))
print('unique elements(2): ', tuple(set(b2)))
print('unique elements(3): ', tuple(set(b3)))

# Задание 3
c1 = (1, 2, 3, 4, 5, 6, 7)
c2 = (1, 8, 3, 2, 5, 6, 7)
c3 = (6, 5, 3, 8, 5, 3, 7)
common_el = [c1[i] for i in range(min(len(c1), len(c2), len(c3))) if c1[i] == c2[i] == c3[i]]
print(f'common elements that are in the same position: {common_el}')