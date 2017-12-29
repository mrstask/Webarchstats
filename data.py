from settings import headers,proxyDict
import requests
import time
import random
from mysql import write_to_db,read_from_db

def data_from_wa(read_from_db):
    random_sleep = random.randint(1,10)
    list_from_wa = {}
    for url in read_from_db:
        sitename = url
        url = 'https://web.archive.org/__wb/search/metadata?q=' + url
        r = requests.get(url, headers=headers, proxies=proxyDict)
        returned_data = r.json()

        if returned_data != {}:
            list_from_wa[sitename] = returned_data
            print("in webarchive {}".format(sitename))
            time.sleep(random_sleep)
        else:
            print("not webarchive {}".format(sitename))
            time.sleep(random_sleep)
    return list_from_wa


def iterate_data(returned_data):
    domains = list(returned_data.keys())
    category_keys = ['captures', 'urls', 'new_urls']
    result_dict = {}
    for domain in domains:
        result_dct = {}
        domain_data = returned_data[domain]
        for category_key in category_keys:
            result_dct[category_key] = get_data(domain_data, category_key)
        result_dict[domain] = result_dct
    return result_dict


def get_data(domain_data, category_key):
    htmls = 0
    imgs = 0
    snap_years = list(domain_data[category_key].keys())
    for snap_year in snap_years:
        if 'text/html' in domain_data[category_key][snap_year]:
            htmls += domain_data[category_key][snap_year]['text/html']
        if 'image/jpeg' in domain_data[category_key][snap_year]:
            imgs += domain_data[category_key][snap_year]['image/jpeg']
    return_dict = {
        'htm': htmls,
        'img': imgs
    }
    return return_dict


def convert_dict(result_dict):
    keys = list(result_dict.keys())
    multiple_query = ''
    for key in keys:
        site = key
        captures_html = result_dict[key]['captures']['htm']
        captures_img = result_dict[key]['captures']['img']
        urls_html = result_dict[key]['urls']['htm']
        urls_img = result_dict[key]['urls']['img']
        new_urls_html = result_dict[key]['new_urls']['htm']
        new_urls_img = result_dict[key]['new_urls']['img']
        multiple_query += "('{}',{},{},{},{},{},{}),".format(site, captures_html, captures_img, urls_html, urls_img,
                                                          new_urls_html, new_urls_img)
    query_string = "INSERT INTO `result`(`site`, `captures_htm`, `captures_img`, `urls_htm`, `urls_img`, `new_urls_htm`" \
                   ", `new_urls_img`) VALUES {}".format(multiple_query)
    query_string = query_string[:-1]
    return query_string
