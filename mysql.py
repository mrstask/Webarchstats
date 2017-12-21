import MySQLdb

#def mysql_write():
#    db = MySQLdb.connect("localhost","root","","webarch" )
#    cursor = db.cursor()
#    query =
#    cursor.execute("SELECT VERSION()")
#    data = cursor.fetchone()
#    db.close()

result_list = [{'site': '10topcasino.ru', 'category_key': 'captures', 'htmls': 1, 'imgs': 1},
               {'site': '10topcasino.ru', 'category_key': 'urls', 'htmls': 1, 'imgs': 1},
               {'site': '10topcasino.ru', 'category_key': 'new_urls', 'htmls': 0, 'imgs': 1}]

def convert_dict(result_list):
    site = result_list[0]['site']
    #category_key = result_list[0]['category_key']
    captures_html = result_list[0]['htmls']
    captures_img = result_list[0]['imgs']
    urls_html = result_list[1]['htmls']
    urls_img = result_list[1]['imgs']
    new_urls_html = result_list[2]['htmls']
    new_urls_img = result_list[2]['imgs']

    query_string = "INSERT INTO `result`(`site`, `captures_htm`, `captures_img`, `urls_htm`, `urls_img`," \
                   " `new_urls_htm`, `new_urls_img`) VALUES ('{}',{},{},{}," \
                   "{},{},{})".format(site, captures_html, captures_img, urls_html, urls_img, new_urls_html, new_urls_img)
    test_str = "site:{}, captures_htmls:{}, captures_imgs:{}, urls_htmls: {}, urls_imgs:{}, new_urls_htmls:{}, new_urls_" \
               "imgs:{}".format(site, captures_html, captures_img, urls_html, urls_img, new_urls_html, new_urls_img)
    print(query_string)

convert_dict(result_list)