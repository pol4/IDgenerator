import unittest
from source.IDmodule import new_id


class IDGenTest(unittest.TestCase):
    def test_new_id(self):
        old_val = 0
        for i in range(1, 101):
            for j in range(1, i+1):
                current_val = new_id()
                self.assertTrue(current_val > old_val)
                old_val = current_val


if __name__ == '__main__':
    unittest.main()
