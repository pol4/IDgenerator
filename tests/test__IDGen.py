import unittest
from source.IDmodule import IDGen


class IDGenTest(unittest.TestCase):
    def test_digits(self):
        self.assertEqual(IDGen.digits(321), '0')
        self.assertEqual(IDGen.digits(4), '000')
        self.assertEqual(IDGen.digits(0), '000')
        self.assertEqual(IDGen.digits(32), '00')

    def test_get_c(self):
        a = IDGen()
        for i in range(30):
            a.get_c()
        self.assertEqual(a.get_c(), '031')

        a = IDGen()
        for i in range(64):
            a.get_c()
        self.assertEqual(a.get_c(), '065')

        a = IDGen()
        for i in range(99):
            a.get_c()
        self.assertEqual(a.get_c(), '100')

        a = IDGen()
        for i in range(100):
            a.get_c()
        self.assertEqual(a.get_c(), '001')

        a = IDGen()
        self.assertEqual(a.get_c(), '001')


if __name__ == '__main__':
    unittest.main()
