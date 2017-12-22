from mysql import read_from_db, write_to_db
from data import data_from_wa

sites = read_from_db()
list_from_wa = data_from_wa(sites)

print(list_from_wa)


