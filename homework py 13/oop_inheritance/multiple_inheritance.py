# task 1
# from abc import ABC, abstractmethod
#
#
# class Figure(ABC):
#     def __init__(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     def __str__(self):
#         return f'the area of the {self.__class__.__name__} is {self.area()}'
#
#     def __int__(self):
#         return int(self.area())
#
#
# class Rectangle(Figure):
#     def __init__(self, side, height):
#         self.side = side
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.side * self.height
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# class RightTriangle(Figure):
#     def __init__(self, side1, side2):
#         self.side1 = side1
#         self.side2 = side2
#
#     def area(self):
#         return 0.5 * self.side1 * self.side2
#
#
# class Trapezoid(Figure):
#     def __init__(self, side1, side2, height):
#         self.side1 = side1
#         self.side2 = side2
#         self.height = height
#
#     def area(self):
#         return ((self.side1 + self.side2) / 2) * self.height
#
#
# r = Rectangle(9, 5)
# print(r)
# print(int(r))
# c = Circle(3)
# print(c)
# print(int(c))
# rt = RightTriangle(10, 6)
# print(rt)
# print(int(rt))
# t = Trapezoid(7, 10, 5)
# print(t)
# print(int(t))

# task 2
# The magic int and str methods were added to task 1

# task 3
# import json
#
#
# class Shape:
#     def show(self):
#         pass
#
#     @staticmethod
#     def save(file_shapes):
#         data = []
#         for save_shape in file_shapes:
#             data.append(save_shape.__dict__)
#         with open('shapes.json', 'w') as f:
#             json.dump(data, f)
#
#     @staticmethod
#     def load():
#         file_shapes = []
#         with open('shapes.json', 'r') as f:
#             data = json.load(f)
#             for item in data:
#                 if item['type'] == 'square':
#                     load_shape = Square(item['x'], item['y'], item['length'])
#                 elif item['type'] == 'rectangle':
#                     load_shape = Rectangle(item['x'], item['y'], item['width'], item['height'])
#                 elif item['type'] == 'circle':
#                     load_shape = Circle(item['x'], item['y'], item['radius'])
#                 elif item['type'] == 'ellipse':
#                     load_shape = Ellipse(item['x'], item['y'], item['width'], item['height'])
#                 else:
#                     raise ValueError(f"Unknown shape type: {item['type']}")
#                 file_shapes.append(load_shape)
#         return file_shapes
#
#
# class Square(Shape):
#     def __init__(self, x, y, length):
#         self.x = x
#         self.y = y
#         self.length = length
#         self.type = 'square'
#
#     def show(self):
#         print(f"Square: x={self.x}, y={self.y}, length={self.length}")
#
#
# class Rectangle(Shape):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.type = 'rectangle'
#
#     def show(self):
#         print(f"Rectangle: x={self.x}, y={self.y}, width={self.width}, height={self.height}")
#
#
# class Circle(Shape):
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.type = 'circle'
#
#     def show(self):
#         print(f"Circle: x={self.x}, y={self.y}, radius={self.radius}")
#
#
# class Ellipse(Shape):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.type = 'ellipse'
#
#     def show(self):
#         print(f"Ellipse: x={self.x}, y={self.y}, width={self.width}, height={self.height}")
#
#
# shapes = [Square(0, 0, 10), Rectangle(20, 20, 30, 40), Circle(50, 50, 15), Ellipse(70, 70, 20, 30)]
# Shape.save(shapes)
# loaded_shapes = Shape.load()
# for shape in loaded_shapes:
#     shape.show()