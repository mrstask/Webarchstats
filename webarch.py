import requests
import time
import MySQLdb

def get_data(keys, html_key, image_key, category_key):
    htmls = 0
    imgs = 0
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

def iterate_data(returned_data):
    category_keys = ['captures', 'urls', 'new_urls']
    html_key = 'text/html'
    image_key = 'image/jpeg'
    result_list = []
    for category_key in category_keys:
        keys = returned_data[category_key].keys()
        result_list.append(get_data(keys, html_key, image_key, category_key))
    return result_list

http_proxy = "http://134.0.116.68:5010"
https_proxy = "https://134.0.116.68:5010"
ftp_proxy = "ftp://134.0.116.68:5010"

proxyDict = {
              "http": http_proxy,
              "https": https_proxy,
              "ftp": ftp_proxy
            }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'From': 'https://web.archive.org'
}

def reding_file():
    with open('data.txt') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        return content

def write_file():
    with open('result.txt', "a") as f:
        f.write(str(iterate_data(returned_data)) + "\r\n")
        time.sleep(1)
        print(url)

#todo reading from db
#todo converting dict to query
def convert_dict(result_list):
    for row in result_list:
        site = row[]

#todo writing to db

for url in reding_file():
    sitename = url
    url = 'https://web.archive.org/__wb/search/metadata?q=' + url
    r = requests.get(url, headers=headers, proxies=proxyDict)
    returned_data = r.json()

    if returned_data != {}:
        write_file()
    else:
        time.sleep(1)
        print(url)








#result_dict['urls']['2013']['text/html']



