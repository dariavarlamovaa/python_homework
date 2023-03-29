# import re

# task 1
# strs = ['Aliquam erat volutpat', 'Fusce fringilla lobortis lorem, sed dictum quam accumsan',
#         'Etiam tristique interdum maximus', 'Ut quis quam quis dui posuere porttitor']
# for s in strs:
#     if re.findall(r'\A[aeiouyAEIOUY].*[bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXYZ]\Z', s):
#         print(s)

# task 2
# strs = ['https://www.w3schools.com/python/', 'https://www.youtube.com/', 'https://web.whatsapp.com',
#         'https://vk.com/feed', 'blabla.com', 'http://hello.com/', 'www.google.com', ]
# for s in strs:
#     if re.findall(r'https://\w+.\w+.+|http://\w+.\w+|www.\w+.\w+', s):
#         print(s)


# task 3
# strs = ['Aliquam erat volutpat', 'fusce fringilla Lobortis lorem, sed dictum quam accumsan',
#         'Etiam tristique interdum maximus', 'ut quis quam quis dui posuere porttitor']
# for s in strs:
#     if re.findall(r'.*\b[A-Z].*', s):
#         print(s)

# task 4
# text = 'book, look, love, key, hello, letter'.split(', ')
# words = [word for word in text if re.findall(r'\b\w*(\w)\1\w*\b', word)]
# print(*words, sep=', ')
