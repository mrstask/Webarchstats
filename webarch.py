from mysql import read_from_db, write_to_db
from data import data_from_wa, iterate_data, convert_dict
import random
import time

for _ in range(1):
    sites = read_from_db()
    list_from_wa = data_from_wa(sites)
    if list_from_wa:
        result_list = iterate_data(list_from_wa)
        big_query = convert_dict(result_list)
        write_to_db(big_query)
    time.sleep(random.randint(30, 120))
