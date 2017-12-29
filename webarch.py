from mysql import read_from_db, write_to_db, update_db
from data import data_from_wa, iterate_data, convert_dict
import random
import time

for _ in range(300):
    sites = read_from_db(20)
    for site in sites:
        update_db(site)
    list_from_wa = data_from_wa(sites)
    result_list = iterate_data(list_from_wa)
    big_query = convert_dict(result_list)
    write_to_db(big_query)
    time.sleep(random.randint(30, 120))

