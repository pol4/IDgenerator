# import unittest
# from source.IDmodule import IDGen
#
#
# class IDGenTest(unittest.TestCase):
#     def test_digits(self):
#         t = IDGen()
#         self.assertEqual(t.__gigits(321), '0')
#         self.assertEqual(IDGen.__digits(4), '000')
#         self.assertEqual(IDGen.__digits(0), '000')
#         self.assertEqual(IDGen.__digits(32), '00')
#
#     def test_get_c(self):
#         a = IDGen()
#         for i in range(30):
#             a.__get_c()
#         self.assertEqual(a.__get_c(), '031')
#
#         a = IDGen()
#         for i in range(64):
#             a.__get_c()
#         self.assertEqual(a.__get_c(), '065')
#
#         a = IDGen()
#         for i in range(99):
#             a.__get_c()
#         self.assertEqual(a.__get_c(), '100')
#
#         a = IDGen()
#         for i in range(100):
#             a.__get_c()
#         self.assertEqual(a.__get_c(), '001')
#
#         a = IDGen()
#         self.assertEqual(a.__get_c(), '001')
#
#
# if __name__ == '__main__':
#     unittest.main()
