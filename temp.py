
returned_data = {'captures': {'2015': {'application/x-shockwave-flash': 1, 'text/html': 7, 'image/jpeg': 3}, '2014': {'application/x-shockwave-flash': 2, 'text/html': 5}, '2016': {'application/x-shockwave-flash': 3, 'text/html': 16, 'image/jpeg': 4}, '2013': {'application/x-shockwave-flash': 1, 'text/html': 5, 'image/jpeg': 4}}, 'urls_total_compressed_size': {'2015': {'application/x-shockwave-flash': 259829, 'text/html': 10301, 'image/jpeg': 201361}, '2014': {'application/x-shockwave-flash': 259831, 'text/html': 10304}, '2016': {'application/x-shockwave-flash': 259831, 'text/html': 13918, 'image/jpeg': 270477}, '2013': {'application/x-shockwave-flash': 259831, 'text/html': 10136, 'image/jpeg': 270473}}, 'type': 'host', 'urls': {'2015': {'application/x-shockwave-flash': 1, 'text/html': 4, 'image/jpeg': 3}, '2014': {'application/x-shockwave-flash': 1, 'text/html': 4}, '2016': {'application/x-shockwave-flash': 1, 'text/html': 4, 'image/jpeg': 4}, '2013': {'application/x-shockwave-flash': 1, 'text/html': 4, 'image/jpeg': 4}}, 'new_urls': {'2013': {'application/x-shockwave-flash': 1, 'text/html': 4, 'image/jpeg': 4}}}



def get_data(keys, html_key, image_key, category_key):
    htmls = 0
    imgs = 0
    sitename = 'site'
    for key in keys:
        if html_key in returned_data[category_key][key]:
            htmls += returned_data[category_key][key][html_key]
        if image_key in returned_data[category_key][key]:
            imgs += returned_data[category_key][key][image_key]
    return_dict = {
        'site': sitename,
        'category_key': category_key,
        'htmls': htmls,
        'imgs': imgs
    }
    print(return_dict)
    print("category_key:{}, htmls:{}".format(category_key, htmls))
    print("category_key:{}, imgs:{}".format(category_key, imgs))

def iterate_data(returned_data):
    category_keys = ['captures', 'urls', 'new_urls']
    html_key = 'text/html'
    image_key = 'image/jpeg'
    for category_key in category_keys:
        keys = returned_data[category_key].keys()
        get_data(keys, html_key, image_key, category_key)





iterate_data(returned_data)