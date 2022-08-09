from datetime import datetime
import uuid
import json


class IDGen:
    mac = 0

    def __init__(self):
        self.mac = uuid.getnode() & 0x000000000FFF

    def new_id(self):
        """ returns a custom id, created from uuid.uuid1"""
        id_hex = uuid.uuid1(node=self.mac)
        id_hex_sep = str(id_hex).split("-")

        pure_time = '{}{}{}'.format(id_hex_sep[2][1:],
                                    id_hex_sep[1],
                                    id_hex_sep[0])

        pure_time = str(int(pure_time, 16) - 0x1ea2c29a747c000)  # switch timestamp to 0:00, 01.01.2020

        temp = int(id_hex_sep[4], 16)
        res = int("{}{}{}{}{}{}".format('1',
                                        '0' * (17 - len(pure_time)),
                                        int(pure_time),
                                        int(id_hex_sep[3], 16),
                                        '0' * (4 - len(str(temp))),
                                        temp))
        return res

    def json(self):
        json_id = {'ID': self.new_id(), 'birth': str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")), 'host': self.mac}
        json_id = json.dumps(json_id)
        return json_id


if __name__ == "__main__":
    a = IDGen()
    a = a.new_id()
    print(a)
