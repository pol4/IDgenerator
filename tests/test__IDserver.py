import os
import requests
import unittest
import json
import sys
sys.path.append(os.path.join(os.getcwd(), 'IDgenerator_web'))
import url_mkr


class IDGenTest(unittest.TestCase):
    def test_new_id(self):
        for i in range(102):
            str_json = requests.get('http://{}:{}'.format(url_mkr.IP,
                                                          url_mkr.port)).text
            dict_json = json.loads(str_json)
            self.assertTrue(type(dict_json['ID']) == int)
            birth = dict_json['birth']
            self.assertTrue(type(birth) == str and birth[2] == birth[5] and birth[14] == birth[17])
            self.assertTrue(type(dict_json['host']) == int and 0 <= (dict_json['host']) <= 4095)


if __name__ == '__main__':
    unittest.main()
