import MySQLdb

def read_from_db(quant):
    sites = []
    db = MySQLdb.connect("localhost", "root", "", "webarch")
    cursor = db.cursor()
    sql = "SELECT sitename FROM `source` WHERE inuse='0' LIMIT {}".format(quant)
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
    db = MySQLdb.connect("localhost","root","","webarch")
    cursor = db.cursor()
    sql = query_string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def update_db(sitename):
    db = MySQLdb.connect("localhost","root","","webarch")
    cursor = db.cursor()
    sql = "UPDATE `source` SET `inuse`='1' WHERE `sitename`='{}'".format(sitename)
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
#some_list = read_from_db()
#print(some_list[0])
#update_db(some_list[0])


