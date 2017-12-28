
returned_data = {'10topcasino.ru': {'captures': {'htm': 1, 'img': 1}, 'urls': {'htm': 1, 'img': 1}, 'new_urls': {'htm': 0, 'img': 1}}, '174-elki.ru': {'captures': {'htm': 1, 'img': 0}, 'urls': {'htm': 1, 'img': 0}, 'new_urls': {'htm': 1, 'img': 0}}, '188800.ru': {'captures': {'htm': 17609, 'img': 1338}, 'urls': {'htm': 6467, 'img': 619}, 'new_urls': {'htm': 4540, 'img': 270}}, '1avtolombard.ru': {'captures': {'htm': 33, 'img': 11}, 'urls': {'htm': 16, 'img': 11}, 'new_urls': {'htm': 4, 'img': 4}}}

#returned_data = {'10topcasino.ru': {'captures': {'2013': {'image/gif': 1, 'image/png': 2, 'text/html': 1, 'image/jpeg': 1, 'text/css': 1}},
#                                    'urls_total_compressed_size': {'2013': {'image/gif': 1118, 'image/png': 33707, 'text/html': 2385, 'image/jpeg': 2834, 'text/css': 16743}},
#                                    'type': 'host',  'urls': {'2013': {'image/gif': 1, 'image/png': 2, 'text/html': 1, 'image/jpeg': 1, 'text/css': 1}},
#                                    'new_urls': {'2013': {'image/gif': 1, 'image/png': 2, 'text/css': 1, 'image/jpeg': 1}}}}


def iterate_data(returned_data):
    domains = list(returned_data.keys())
    category_keys = ['captures', 'urls', 'new_urls']
    result_dict = {}
    for domain in domains:
        result_dct = {}
        domain_data = returned_data[domain]
        for category_key in category_keys:
            #keys = list(domain_data.keys())
            result_dct[category_key] = get_data(domain_data, category_key)
        result_dict[domain] = result_dct
    return result_dict


def get_data(domain_data, category_key):
    htmls = 0
    imgs = 0
    snap_years = list(domain_data[category_key].keys())
    #print("domain_data[category_key] {} [category_key] {} snap year {}".format(domain_data[category_key], category_key, snap_years))
    #if 'text/html' in domain_data[category_key]['2013']:
    #    print(domain_data[category_key]['2013']['text/html'])
    for snap_year in snap_years:
        if 'text/html' in domain_data[category_key][snap_year]:
            htmls += domain_data[category_key][snap_year]['text/html']
            print("category_key = {}, snap_year = {}, htmls = {}".format(category_key,snap_year,htmls))
        if 'image/jpeg' in domain_data[category_key][snap_year]:
            imgs += domain_data[category_key][snap_year]['image/jpeg']
            #print("category_key = {}, snap_year = {}, imgs = {}".format(category_key, snap_year, imgs))
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


result_dict = iterate_data(returned_data)

big_query = convert_dict(result_dict)

print(big_query)

