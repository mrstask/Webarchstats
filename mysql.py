import MySQLdb


def read_from_db():
    sites = []
    db = MySQLdb.connect("138.68.163.33", "admin_webarch", "fZFUCSpcsx", "admin_webarch")
    cursor = db.cursor()
    sql = "SELECT sitename FROM `source` WHERE inuse='0' LIMIT 10"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            sites.append(row[0])
    except:
        print("Error: unable to fetch data")
    db.close()
    return sites

def write_to_db(query_string):
    db = MySQLdb.connect("138.68.163.33", "admin_webarch", "fZFUCSpcsx", "admin_webarch")
    cursor = db.cursor()
    sql = query_string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


# result_list = [{'site': '10topcasino.ru', 'category_key': 'captures', 'htmls': 1, 'imgs': 1},
#                {'site': '10topcasino.ru', 'category_key': 'urls', 'htmls': 1, 'imgs': 1},
#                {'site': '10topcasino.ru', 'category_key': 'new_urls', 'htmls': 0, 'imgs': 1}]


#query_string = convert_dict(result_list)
#mysql_write(query_string)
#print(read_from_db())

def write_to_db_test(query_string):
    db = MySQLdb.connect("45.63.13.67", "admin_webarch", "fZFUCSpcsx", "admin_webarch")
    cursor = db.cursor()
    sql = query_string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

write_to_db_test("INSERT INTO `result`(`sitename`, `captures_htm`, `captures_img`, `urls_htm`, `urls_img`," \
                   " `new_urls_htm`, `new_urls_img`) VALUES ('test',1,2,3," \
                   "4,5,6)")
def read_from_db_test():
    sites = []
    db = MySQLdb.connect("45.63.13.67", "admin_webarch", "fZFUCSpcsx", "admin_webarch")
    cursor = db.cursor()
    sql = "SELECT * FROM `result` WHERE inuse='0' LIMIT 10"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            sites.append(row[0])
    except:
        print("Error: unable to fetch data")
    db.close()
    return sites
print(read_from_db_test())