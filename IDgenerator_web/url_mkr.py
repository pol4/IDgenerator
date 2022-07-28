import os.path
from pprint import pprint
import sys

sys.path.append(os.path.join(os.getcwd(), '..'))
# sys.path.append('..')

param_types = ('IP', 'PORT')


def get_list(str_x=''):
    list_x = str_x.split('=')
    list_x = [i.rstrip() for i in list_x]
    return list_x


with open('IDgenerator_web/config.txt') as file:
    for line in file:
        param = get_list(line)
        param_type = param[0]

        if param_type == param_types[0]:
            IP = param[1]

        elif param_type == param_types[1]:
            port = param[1]


args = sys.argv[1:]
if len(args) > 1:
    IP = args[0]

if len(args) > 2:
    port = args[1]
