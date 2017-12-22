# def reding_file():
#     with open('data.txt') as f:
#         content = f.readlines()
#         content = [x.strip() for x in content]
#         return content
#
# def write_file():
#     with open('result.txt', "a") as f:
#         f.write(str(iterate_data(returned_data)) + "\r\n")
#         time.sleep(1)
#         print(url)
#
#
# def get_data_from_file():
#     for url in read_from_db():
#         sitename = url
#         url = 'https://web.archive.org/__wb/search/metadata?q=' + url
#         r = requests.get(url, headers=headers, proxies=proxyDict)
#         returned_data = r.json()
#
#         if returned_data != {}:
#            write_to_db()
#         else:
#             time.sleep(1)
#             print("useless:{}".format(url)url)