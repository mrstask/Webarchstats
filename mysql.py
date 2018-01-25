from settings import DBNAME, DBIP, DBUSER, DBPASS
import pymysql


def read_from_db():
    sites = {}
    db = pymysql.connect(DBIP, DBUSER, DBPASS, DBNAME)
    cursor = db.cursor()
    try:
        cursor.execute("SELECT domain,id FROM `source` WHERE inuse='0' LIMIT {}".format(10))
        results = cursor.fetchall()
        for row in results:
            sites[row[1]] = row[0]
    except:
        print("Error: unable to fetch data")
    db.close()
    return sites

def write_to_db(query_string):
    db = pymysql.connect(DBIP, DBUSER, DBPASS, DBNAME)
    cursor = db.cursor()
    sql = query_string
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def update_db(query_result):
    db = pymysql.connect(DBIP, DBUSER, DBPASS, DBNAME)
    cursor = db.cursor()
    for ids, url in query_result.items():
        sql = "UPDATE `source` SET `inuse`='1' WHERE `id`='{}'".format(ids)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
    db.close()


def quantity():
    db = pymysql.connect(DBIP, DBUSER, DBPASS, DBNAME)
    cursor = db.cursor()
    try:
        cursor.execute("SELECT COUNT(domain) FROM `source` WHERE inuse=0")
        results = cursor.fetchone()
    except:
        print("Error: unable to fetch data")
    db.close()
    return results[0]


def select_for_update():
    sites = {}
    db = pymysql.connect(DBIP, DBUSER, DBPASS, DBNAME)
    cursor = db.cursor()
    for _ in range(10):
        try:
            cursor.execute("SELECT domain, id FROM `source` WHERE inuse='0' LIMIT 1 FOR UPDATE")
            results = cursor.fetchone()
            print(results)
            print("UPDATE `source` SET `inuse`='1' WHERE `id`='{}'".format(results[1]))
            cursor.execute("UPDATE `source` SET `inuse`='1' WHERE `id`='{}'".format(results[1]))
            sites[results[1]] = results[0]
        except:
            print("Error: unable to fetch data")
    db.close()
    return sites
