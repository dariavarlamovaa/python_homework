import unittest


# task 1
# class Numbers:
#     @staticmethod
#     def get_sum_sum(*args):
#         return sum(args)
#
#     @staticmethod
#     def get_average(*args):
#         return round(sum(args) / len(args), 4)
#
#     @staticmethod
#     def get_max(*args):
#         return max(args)
#
#     @staticmethod
#     def get_min(*args):
#         return min(args)
#
#
# class TestNumbers(unittest.TestCase):
#     def setUp(self) -> None:
#         self.n1 = 1
#         self.n2 = 5
#         self.n3 = 7
#
#     def test_sum_sum(self):
#         self.assertEqual(13, Numbers.get_sum_sum(self.n1, self.n2, self.n3), 'Expected result = 13')
#
#     def test_get_average(self):
#         self.assertEqual(4.3333, Numbers.get_average(self.n1, self.n2, self.n3), 'Expected result = 4.3333')
#
#     def test_get_max(self):
#         self.assertEqual(7, Numbers.get_max(self.n1, self.n2, self.n3), 'Expected result = 7')
#
#     def test_get_min(self):
#         self.assertEqual(1, Numbers.get_min(self.n1, self.n2, self.n3), 'Expected result = 1')
#
#
# if __name__ == '__main__':
#     unittest.main()


# task 2
# class Number:
#     def __init__(self):
#         self.num = None
#
#     def set_num(self, new_num):
#         self.num = new_num
#
#     def get_num(self):
#         return self.num
#
#     def get_octal_num(self):
#         return int(oct(self.num)[2:])
#
#     def get_hexadecimal_num(self):
#         return hex(self.num)[2:]
#
#     def get_binary_num(self):
#         return int(bin(self.num)[2:])
#
#
# class TestNumber(unittest.TestCase):
#     def setUp(self) -> None:
#         self.number = Number()
#         self.num = 10
#         self.number.set_num(self.num)
#
#     def test_set_num(self):
#         self.assertEqual(10, self.number.get_num(), 'Expected result = 10')
#
#     def test_get_oct(self):
#         self.assertEqual(12, self.number.get_octal_num(), 'Expected result = 12')
#
#     def test_get_hex(self):
#         self.assertEqual('a', self.number.get_hexadecimal_num(), 'Expected result = a')
#
#     def test_get_bin(self):
#         self.assertEqual(1010, self.number.get_binary_num(), 'Expected result = 1010')
#
#
# if __name__ == '__main__':
#     unittest.main()
