import re

# Задание 1
palindrome1 = input('enter the string: ').lower().split(',')
if palindrome1 == palindrome1[::-1]:
    print('yes, this is a palindrome')
else:
    print('no, this is not a palindrome')

# Задание 2
a = input('enter your text: ').lower()
b = input('enter the keywords: ').lower().split()
for w in b:
    a = a.replace(w, w.upper())
print(a)

# Задание 3
text = input('enter your text: ')
clear_sentences = re.findall(r"\s*([^.?!]+)\s*", text)
print(f"The text has {len(clear_sentences)} sentences.")
