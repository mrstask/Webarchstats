
returned_data = {'10topcasino.ru': {'captures': {'htm': 1, 'img': 1}, 'urls': {'htm': 1, 'img': 1}, 'new_urls': {'htm': 0, 'img': 1}}, '174-elki.ru': {'captures': {'htm': 1, 'img': 0}, 'urls': {'htm': 1, 'img': 0}, 'new_urls': {'htm': 1, 'img': 0}}, '188800.ru': {'captures': {'htm': 17609, 'img': 1338}, 'urls': {'htm': 6467, 'img': 619}, 'new_urls': {'htm': 4540, 'img': 270}}, '1avtolombard.ru': {'captures': {'htm': 33, 'img': 11}, 'urls': {'htm': 16, 'img': 11}, 'new_urls': {'htm': 4, 'img': 4}}}

def iterate_data(returned_data):
    domains = list(returned_data.keys())
    category_keys = ['captures', 'urls', 'new_urls']
    result_dict = {}
    for domain in domains:
        result_dct = {}
        domain_data = returned_data[domain]
        for category_key in category_keys:
            keys = list(domain_data.keys())
            result_dct[category_key] = get_data(domain_data, keys)
        result_dict[domain] = result_dct
    return result_dict


def get_data(domain_data, keys):
    htmls = 0
    imgs = 0
    for key in keys:
        if 'text/html' in domain_data[key]:
            htmls += domain_data[key]['text/html']
        if 'image/jpeg' in domain_data[key]:
            imgs += domain_data[key]['image/jpeg']
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

#big_query = convert_dict(result_dict)

print(result_dict)

