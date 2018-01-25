from mysql import read_from_db, write_to_db,quantity
from data import data_from_wa, iterate_data, convert_dict
import random
import time

if quantity() > 100:
    for _ in range(10):
        if quantity() > 100:
            print("start range")
            sites = read_from_db()
            list_from_wa = data_from_wa(sites)
            if list_from_wa:
                result_list = iterate_data(list_from_wa)
                big_query = convert_dict(result_list)
                write_to_db(big_query)
            print("finish range")
            time.sleep(random.randint(30, 120))
