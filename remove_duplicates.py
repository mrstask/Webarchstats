from settings import DBNAME, DBIP, DBUSER, DBPASS
import pymysql


def read_duplicates():
    sites = []
    db = pymysql.connect(DBIP, DBUSER, DBPASS, DBNAME)
    cursor = db.cursor()
    query = 'SELECT domain, COUNT(*) c FROM source GROUP BY domain HAVING c > 1'
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            sites.append(row)
    except:
        print("Error: unable to fetch data")
    db.close()
    return sites

def removing_prepare(site):
    ids = []
    site_id = {}
    db = pymysql.connect(DBIP, DBUSER, DBPASS, DBNAME)
    cursor = db.cursor()
    domain = site[0]
    query = "SELECT id FROM source WHERE domain='{}' ORDER BY id DESC".format(domain)
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            ids.append(row)
        site_id[domain] = ids
    except:
        db.rollback()
    db.close()
    return site_id

def remove_duplicates(site):
    db = pymysql.connect(DBIP, DBUSER, DBPASS, DBNAME)
    cursor = db.cursor()

    for key in site.keys():
        site_name = key
    ids_list = site[site_name]
    print(site_name)
    for _ in range(len(ids_list)-1):
        sql = "DELETE FROM `source` WHERE id ={}".format(ids_list[0][0])
        del ids_list[0]
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            db.close()



# list_of_duplicates = read_duplicates()
#
# for site in list_of_duplicates:
#     some = removing_prepare(site)
#     remove_duplicates(some)


