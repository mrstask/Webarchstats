from settings import headers,proxyDict
import requests
import time
from mysql import write_to_db,read_from_db

def data_from_wa(read_from_db):
    list_from_wa = {}
    for url in read_from_db:
        sitename = url
        url = 'https://web.archive.org/__wb/search/metadata?q=' + url
        r = requests.get(url, headers=headers, proxies=proxyDict)
        returned_data = r.json()

        if returned_data != {}:
            list_from_wa[sitename] = returned_data
        else:
            time.sleep(1)
            print("useless:{}".format(url))
    return list_from_wa


def iterate_data(returned_data):
    category_keys = ['captures', 'urls', 'new_urls']
    html_key = 'text/html'
    image_key = 'image/jpeg'
    result_list = []
    for category_key in category_keys:
        keys = returned_data[category_key].keys()
        result_list.append(get_data(keys, html_key, image_key, category_key))
    return result_list


def get_data(returned_data, keys, html_key, image_key, category_key):
    htmls = 0
    imgs = 0
    sitename = returned_data['sitename']
    for key in keys:
        if html_key in returned_data[category_key][key]:
            htmls += returned_data[category_key][key][html_key]
        if image_key in returned_data[category_key][key]:
            imgs += returned_data[category_key][key][image_key]
    return_dict = {
        'site': sitename,
        'category_key': category_key,
        'htm': htmls,
        'img': imgs
    }
    return return_dict

def convert_dict(result_list):
    site = result_list[0]['site']
    captures_html = result_list[0]['htmls']
    captures_img = result_list[0]['imgs']
    urls_html = result_list[1]['htmls']
    urls_img = result_list[1]['imgs']
    new_urls_html = result_list[2]['htmls']
    new_urls_img = result_list[2]['imgs']

    query_string = "INSERT INTO `result`(`site`, `captures_htm`, `captures_img`, `urls_htm`, `urls_img`," \
                   " `new_urls_htm`, `new_urls_img`) VALUES ('{}',{},{},{}," \
                   "{},{},{})".format(site, captures_html, captures_img, urls_html, urls_img, new_urls_html, new_urls_img)

    return query_string
