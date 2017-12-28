from mysql import read_from_db, write_to_db
from data import data_from_wa, iterate_data, convert_dict

sites = read_from_db()
list_from_wa = data_from_wa(sites)
print('list_from_wa')
print(list_from_wa)
result_list = iterate_data(list_from_wa)
print('result_list')
print(result_list)
big_query = convert_dict(result_list)
print(big_query)
write_to_db(big_query)

