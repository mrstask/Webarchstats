# def reding_file():
#     with open('data.txt') as f:
#         content = f.readlines()
#         content = [x.strip() for x in content]
#         return content
#
# def write_file():
#     with open('result.txt', "a") as f:
#         f.write(str(iterate_data(returned_data)) + "\r\n")
#         time.sleep(1)
#         print(url)
#
#
# def get_data_from_file():
#     for url in read_from_db():
#         sitename = url
#         url = 'https://web.archive.org/__wb/search/metadata?q=' + url
#         r = requests.get(url, headers=headers, proxies=proxyDict)
#         returned_data = r.json()
#
#         if returned_data != {}:
#            write_to_db()
#         else:
#             time.sleep(1)
#             print("useless:{}".format(url)url)

#def write_to_db2():

#    db = pymysql.connect(DBIP,DBUSER,DBPASS,DBNAME)
#    cursor = db.cursor()
#    cursor.execute("SELECT VERSION()")
#    data = cursor.fetchone()
#    print("Database version : %s " % data)
#    db.close()
#    return data


#def write_to_db3():
#    DBNAME = "regru"
#    DBIP = "localhost"
#    DBUSER = "root"
#    DBPASS = "trololo123"
#    db = pymysql.connect(DBIP, DBUSER, DBPASS, DBNAME)
#    cursor = db.cursor()
#    cursor.execute("SELECT VERSION()")
#    data = cursor.fetchone()
#    print("Database version : %s " % data)
#    db.close()
#    return data

# result_list = [{'site': '10topcasino.ru', 'category_key': 'captures', 'htmls': 1, 'imgs': 1},
#                {'site': '10topcasino.ru', 'category_key': 'urls', 'htmls': 1, 'imgs': 1},
#                {'site': '10topcasino.ru', 'category_key': 'new_urls', 'htmls': 0, 'imgs': 1}]


#query_string = convert_dict(result_list)
#mysql_write(query_string)
#print(read_from_db())
#some_list = read_from_db()
#print(some_list[0])
#update_db(some_list[0])

#def read_from_db_old(quant):
#    db = MySQLdb.connect(db_connection_data)
#    sites = []
#    cursor = db.cursor()
#    sql = "SELECT domain,id FROM `source` WHERE inuse='0' LIMIT {}".format(quant)
#    try:
#        cursor.execute(sql)
#        results = cursor.fetchall()
#        for row in results:
#            sites.append(row[0])
#    except:
#        print("Error: unable to fetch data")
#    db.close()
#    return sites