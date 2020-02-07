import requests
client_id = 'rsiUjuINDag8anLQgN_O'
client_secret = 'wji5s_qele'

headers = {'X-Naver-Client-ID':client_id, 'X-Naver-Client-Secret':client_secret}


def get_api_result(keyword, display, start):
    url = 'https://openapi.naver.com/v1/search/image?query=' + keyword \
    + '&display=' + str(display) \
    + '&start=' + str(start)
    result = requests.get(url, headers = headers)
    return result.json()

def call_and_print(keyword, total_page):
    link_list = []
    for page in range(1,total_page):
        json_obj = get_api_result(keyword, 20,(page-1)*20+1)
        for item in json_obj['items']:
            link_list.append(item['link'])
    return link_list

link1 = call_and_print('소나타', 50)


import requests
for i, link in enumerate(link1):
    img_data = requests.get(link).content
    img_format = link.split(".")[-1]
    # 확장자 제어
    if img_format in ['png', 'jpg', 'jpeg']:
        with open(f'sonata{i}.{img_format}', 'wb') as handler:
            handler.write(img_data)



##import urllib.request
##for url in link1:
##    try:
##        image = urllib.request.urlopen(url).read()
##        image_type = url.split('.')[-1]
##        content_type = 'image/{}'.format(image_type)
##        image_name = url.split('/')[-1]
##
##        grid_in = bucket.open_upload_stream(
##            image_name, metadata = {'contentType' : content_type, 'type':'dog' })
##        grid_in.write(image)
##        grid_in.close()
##        print('image_type:', image_type, 'content_type:',content_type,
##             'image_name:', image_name)
##    except:
##        print('ERROR')
