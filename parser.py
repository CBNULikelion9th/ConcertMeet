from bs4 import BeautifulSoup
from django.db import models
import requests, re, os
from PIL import Image
from urllib.request import urlretrieve 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "concertmeet.settings")
import django

django.setup()
from meetapp.models import Concert

# try:
#     if not (os.path.isdir('image')):
#         os.makedirs(os.path.join('image'))
# except OSError as e:
#     if e.errno != e.EEXIST:
#         print("폴더 생성 실패!")
#         exit()

def start():
    try:
        if not (os.path.isdir('./meetapp/image')):
            os.makedirs(os.path.join('./meetapp/image'))
    except OSError as e:
        if e.errno != e.EEXIST:
            print("폴더 생성 실패!")
            exit()

    html = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Rap#")
    soup = BeautifulSoup(html.text, 'html.parser')
    html.close()

    data1_list=soup.find_all('tbody')

    data = []
    li_list = []
    location=''
    date=''

    for data1 in data1_list:
        #제목+썸내일 영역 추출
        li_list.extend(data1.findAll('tr')) #해당 부분을 찾아 li_list와 병합
    #pprint(li_list)
    #pprint(len(li_list))

    #각각 썸네일과 제목 추출하기
    for li in li_list:
        img = li.find('img')
        img_src = img['src']
        title = img['alt']
        # place = li.find_all('td', {'class' : 'Rkdate'})
        # data.append(title)
        # data.append(img_src)

        print(img_src)

        for el in li.find_all('td', {'class' : 'Rkdate'}):
            test = el.get_text()
            test2 = re.sub('\r\n\t\t\t\t\t\t\t', '', test)
            check = len(test2)
            if check == 23 :
                date = test2
            else:
                location = test2

        if img_src != 'http://ticketimage.interpark.com/rz/image/play/goods/poster/21/21005521_p_s.jpg':
            urlretrieve( img_src , './meetapp/image/'+title+'.jpg') #주소, 파일경로+파일명+확장자

        concert_obj = {
            'title' : title,
            'image_url' : img_src,
            'location' : location,
            'date' : date
        }
        data.append(concert_obj)

    for item in data:
        print(item['image_url'])
        Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date']).save()
        print("new item added!! " + item['title'])
    
    return data

# n = 4
# data = [data[i * n:(i + 1) * n] for i in range((len(data) + n - 1) // n )]

if __name__ == '__main__':
    start()
