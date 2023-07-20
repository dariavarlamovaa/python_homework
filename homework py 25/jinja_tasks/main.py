# from jinja2 import Template, Environment, FileSystemLoader

# task 1

# users = [
#     {'name': 'Leo', 'email': 'leo27@gmail.com'},
#     {'name': 'Antony', 'email': 'antony_an@gmail.com'},
#     {'name': 'Vladimir', 'email': 'vova@mail.ru'},
#     {'name': 'Peter', 'email': 'peterrr@gmail.com'},
#     {'name': 'Daniel', 'email': 'danya222@yandex.ru'}
# ]
#
# tm = '''
# {%- macro list_users(users) -%}
# <ul>
#     {%- for user in users -%}
#         {% if user.email.endswith("gmail.com") %}
#             <li>{{ user.name }} - {{ user.email }}</li>
#         {%- endif -%}
#     {% endfor %}
# </ul>
# {% endmacro -%}
#
# {{ list_users(users) }}
# '''
#
# tm = Template(tm)
# msg = tm.render(users=users)
# print(msg)

# task 2

# products = [
#     {'name': 'Carrot', 'price': 5},
#     {'name': 'Potato', 'price': 11},
#     {'name': 'Watermelon', 'price': 30},
#     {'name': 'Lemon', 'price': 9},
#     {'name': 'Coconut', 'price': 17}
# ]
#
# tm = '''
# {%- macro list_products(products) -%}
# <ul>
#     {%- for p in products %}
#         {% if p.price <= 10 -%}
#             <li>{{ p.name }} is affordable</li>
#         {%- elif p.price <= 20 -%}
#             <li>{{ p.name }} is at an average price</li>
#         {%- else -%}
#             <li>{{ p.name }} is expensive</li>
#         {%- endif -%}
#     {% endfor %}
# </ul>
# {% endmacro %}
#
# {{ list_products(products) }}
# '''
#
# tm = Template(tm)
# msg = tm.render(products=products)
# print(msg)

# task 3

# file_loader = FileSystemLoader('')
# env = Environment(loader=file_loader)
# tm = env.get_template('homework.html')
# msg = tm.render(title='Homework')
# print(msg)
