from configparser import ConfigParser


def get_config():
    config = ConfigParser()
    config.read('../docs/config.ini')
    ip = str(config.get('server', 'ip'))
    port = str(config.get('server', 'port'))
    res = [ip, port]
    return res


if __name__ == "__main__":
    a = 0
    b = 0
    get_config(a, b)



# import sys
# 
# param_types = ('IP', 'PORT')
# 
# 
# def get_list(str_x=''):
#     list_x = str_x.split('=')
#     list_x = [i.rstrip() for i in list_x]
#     return list_x
# 
# 
# with open('../docs/config.py') as file:
#     for line in file:
#         param = get_list(line)
#         param_type = param[0]
# 
#         if param_type == param_types[0]:
#             IP = param[1]
# 
#         elif param_type == param_types[1]:
#             port = param[1]
# 
# 
# args = sys.argv[1:]
# if len(args) > 1:
#     IP = args[0]
# 
# if len(args) > 2:
#     port = args[1]
