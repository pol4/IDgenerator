import unittest
from IDgenerator.IDmodule import IDGen


class IDGenTest(unittest.TestCase):
    def test_new_id(self):
        t_id = IDGen()
        old_val = t_id.new_id()
        str_old_val = str(old_val)
        for i in range(102):            # :)
            current_val = t_id.new_id()
            str_current_val = str(current_val)
            self.assertTrue(current_val > old_val)  # monotone growth
            self.assertTrue(len(str_old_val) == len(str_current_val))  # size match
            self.assertTrue(str_old_val[-4:] == str_current_val[-4:])  # node match
            self.assertTrue(str(current_val)[0] == "1")  # 1st bit match


if __name__ == '__main__':
    unittest.main()
