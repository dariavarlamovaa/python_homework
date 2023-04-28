# task 1
# class Node:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next
#
#
# class UserList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = Node(value)
#
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#
#         current_node.next = new_node
#         new_node.prev = current_node
#
#     def delete(self, value):
#         if self.head is None:
#             return
#
#         current_node = self.head
#         while current_node is not None:
#             if current_node.value == value:
#                 if current_node.prev is not None:
#                     current_node.prev.next = current_node.next
#                 else:
#                     self.head = current_node.next
#                 if current_node.next is not None:
#                     current_node.next.prev = current_node.prev
#             current_node = current_node.next
#
#     def contains(self, value):
#         current_node = self.head
#         while current_node:
#             if current_node.value == value:
#                 return True
#             current_node = current_node.next
#         return False
#
#     def show(self, reverse=False):
#         if self.head is None:
#             print('the list is empty!')
#             return
#
#         current_node = self.head
#
#         if reverse:
#             while current_node.next is not None:
#                 current_node = current_node.next
#
#         while current_node is not None:
#             print(current_node.value, end=' ')
#             if reverse:
#                 current_node = current_node.prev
#             else:
#                 current_node = current_node.next
#
#     def replace(self, value, new_value, all_suitable=False):
#         if self.head is None:
#             return
#         current_node = self.head
#         while current_node:
#             if current_node.value == value:
#                 current_node.value = new_value
#             if not all_suitable:
#                 return
#             current_node = current_node.next
#         return
#
#
# u = UserList()
#
# while True:
#     add = input('do you want to add some numbers ("yes" or "no"): ')
#     if add == 'yes':
#         for _ in range(int(input('enter the length of the list: '))):
#             u.append(int(input('enter the number: ')))
#         break
#     else:
#         break
#
# while True:
#     print('\n--------------------------')
#     command = int(input('1-add, 2-del, \n'
#                         '3-show, 4-search, \n'
#                         '5-replace, 0-exit \n'
#                         'enter the command: '))
#     if command == 1:
#         num = int(input('enter the number to add: '))
#         if u.contains(num):
#             print(f'{num} is already in the list')
#         else:
#             u.append(num)
#             print(f'{num} was added to the list')
#
#     elif command == 2:
#         num = int(input('enter the number to delete: '))
#         if u.contains(num):
#             u.delete(num)
#             print(f'{num} was deleted')
#         else:
#             print(f'{num} is not in the list')
#
#     elif command == 3:
#         rev = input('enter "yes" if you want to output a reversed list, otherwise "no": ')
#         if rev == 'yes':
#             u.show(reverse=True)
#         else:
#             u.show()
# 
#     elif command == 4:
#         num = int(input('enter the number to search: '))
#         if u.contains(num):
#             print(f'{num} is in the list')
#         else:
#             print(f'{num} is not in the list')
# 
#     elif command == 5:
#         num = int(input('enter the number to replace: '))
#         if u.contains(num):
#             all_or_first = input('enter "1" if you want to replace only first found number,\n'
#                                  'if all of them - enter: ')
#             new_num = int(input('enter the new number: '))
#             if all_or_first == '1':
#                 u.replace(num, new_num)
#                 print(f'the first found {num} was replaced with {new_num}')
#             else:
#                 u.replace(num, new_num, all_suitable=True)
#                 print(f'all {num} were replaced with {new_num}')
#         else:
#             print(f'{num} is not in the list')
#
#     elif command == 0:
#         print('bye-bye')
#         break
# 
#     else:
#         print('incorrect input. try again')
#         pass


# task 2 ----------- fixed size
# class Stack:
#     def __init__(self, size, iterable: str = None):
#         self.lst = list(iterable) if iterable else []
#         self.size = size
#
#     def push(self, string: str):
#         if not self.is_full():
#             self.lst.append(string)
#         else:
#             print('stack is full')
#
#     def pop(self):
#         return self.is_empty() or self.lst.pop()
#
#     def count_strings(self):
#         return len(self.lst)
#
#     def is_empty(self):
#         if len(self.lst) == 0:
#             return 'stack is empty'
#         return False
#
#     def is_full(self):
#         return len(self.lst) == self.size
#
#     def clean(self):
#         return self.lst.clear()
#
#     def peek(self):
#         return self.is_empty() or self.lst[-1]
#
#     def __str__(self):
#         return ', '.join(map(str, self.lst))
#
#
# s = Stack(5)
#
# while True:
#     print('--------------------------')
#     command = int(input('1-push, 2-pop, \n'
#                         '3-count, 4-is empty, \n'
#                         '5-is full, 6-clear,\n'
#                         '7-peek, 0-exit \n'
#                         'enter the command: '))
#     if command == 1:
#         strng = input('enter the string to push: ')
#         s.push(strng)
#
#     elif command == 2:
#         print(s.pop())
#
#     elif command == 3:
#         print(f'{s.count_strings()} string(s) in the list')
#
#     elif command == 4:
#         if not s.is_empty():
#             print('stack is not empty')
#         else:
#             print(s.is_empty())
#
#     elif command == 5:
#         if s.is_full():
#             print('stack is full')
#         else:
#             print('stack is not full')
#
#     elif command == 6:
#         s.clean()
#         print('stack is cleared')
#
#     elif command == 7:
#         print(s.peek())
#
#     elif command == 0:
#         print('bye-bye')
#         break
#
#     else:
#         print('incorrect input. try again')
#         pass


# task 3 ------------ unfixed size
# class Stack:
#     def __init__(self, iterable: str = None):
#         self.lst = list(iterable) if iterable else []
#
#     def push(self, string: str):
#         self.lst.append(string)
#
#     def pop(self):
#         return self.is_empty() or self.lst.pop()
#
#     def count_strings(self):
#         return len(self.lst)
#
#     def is_empty(self):
#         if len(self.lst) == 0:
#             return 'stack is empty'
#         return False
#
#     def clean(self):
#         return self.lst.clear()
#
#     def peek(self):
#         return self.is_empty() or self.lst[-1]
#
#     def __str__(self):
#         return ', '.join(map(str, self.lst))
#
#
# s = Stack()
#
# while True:
#     print('--------------------------')
#     command = int(input('1-push, 2-pop, \n'
#                         '3-count, 4-is empty, \n'
#                         '5-clear, 6-peek, 0-exit \n'
#                         'enter the command: '))
#     if command == 1:
#         strng = input('enter the string to push: ')
#         s.push(strng)
#
#     elif command == 2:
#         print(s.pop())
#
#     elif command == 3:
#         print(f'{s.count_strings()} string(s) in the list')
#
#     elif command == 4:
#         if not s.is_empty():
#             print('stack is not empty')
#         else:
#             print(s.is_empty())
#
#     elif command == 6:
#         s.clean()
#         print('stack is cleared')
#
#     elif command == 7:
#         print(s.peek())
#
#     elif command == 0:
#         print('bye-bye')
#         break
#
#     else:
#         print('incorrect input. try again')
#         pass
