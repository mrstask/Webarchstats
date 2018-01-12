from settings import db_connection_data
import pymysql

def read_from_db():
    sites = {}
    DBNAME = "admin_regru"
    DBIP = "194.58.122.231"
    DBUSER = "admin_regru"
    DBPASS = "uvT9TO6Aw7"
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
    DBNAME = "admin_regru"
    DBIP = "194.58.122.231"
    DBUSER = "admin_regru"
    DBPASS = "uvT9TO6Aw7"
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
    DBNAME = "admin_regru"
    DBIP = "194.58.122.231"
    DBUSER = "admin_regru"
    DBPASS = "uvT9TO6Aw7"
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

