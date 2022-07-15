import uuid


def new_id():
    """ returns a custom id, created from uuid.uuid1"""
    id_hex = uuid.uuid1(node=(uuid.getnode() & 0x000000000FFF))
    id_hex_sep = str(id_hex).split("-")

    pure_time = '{}{}{}'.format(id_hex_sep[2][1:],
                                id_hex_sep[1],
                                id_hex_sep[0])

    pure_time = str(int(pure_time, 16) - 0x1ea2c29a747c000)  # switch timestamp to 0:00, 01.01.2020

    res = int("{}{}{}{}{}".format('1',
                                  '0' * (17 - len(pure_time)),
                                  int(pure_time),
                                  int(id_hex_sep[3], 16),
                                  int(id_hex_sep[4], 16)))
    return res
