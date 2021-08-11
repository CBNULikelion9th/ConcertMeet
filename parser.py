from bs4 import BeautifulSoup
from django.db import models
import requests, re, os
from PIL import Image
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "concertmeet.settings")
import django

django.setup()
from meetapp.models import Concert

def start():
    html = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Rap#")
    soup = BeautifulSoup(html.text, 'html.parser')
    html.close()

    data1_list=soup.find_all('tbody')

    data = []
    li_list = []
    location=''
    date=''

    for data1 in data1_list:
        li_list.extend(data1.findAll('tr')) 

    for li in li_list:
        img = li.find('img')
        img_src = img['src']
        title = img['alt']

        for el in li.find_all('td', {'class' : 'Rkdate'}):
            test = el.get_text()
            test2 = re.sub('\r\n\t\t\t\t\t\t\t', '', test)
            check = len(test2)
            # 날짜와 장소 구분
            if check == 23 :
                date = test2
            else:
                location = test2

        concert_obj = {
            'title' : title,
            'image_url' : img_src,
            'location' : location,
            'date' : date
        }
        data.append(concert_obj)

    print(data)

    for item in data:
        print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="힙합").save()    
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data

def start2():
    html = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Ind")
    soup = BeautifulSoup(html.text, 'html.parser')
    html.close()

    data1_list=soup.find_all('tbody')

    data = []
    li_list = []
    location=''
    date=''

    for data1 in data1_list:
        li_list.extend(data1.findAll('tr')) 

    for li in li_list:
        img = li.find('img')
        img_src = img['src']
        title = img['alt']

        for el in li.find_all('td', {'class' : 'Rkdate'}):
            test = el.get_text()
            test2 = re.sub('\r\n\t\t\t\t\t\t\t', '', test)
            check = len(test2)
            # 날짜와 장소 구분
            if check == 23 :
                date = test2
            else:
                location = test2

        concert_obj = {
            'title' : title,
            'image_url' : img_src,
            'location' : location,
            'date' : date
        }
        data.append(concert_obj)

    print(data)

    for item in data:
        print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="인디").save()    
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data

def start3():
    html = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Fes#")
    soup = BeautifulSoup(html.text, 'html.parser')
    html.close()

    data1_list=soup.find_all('tbody')

    data = []
    li_list = []
    location=''
    date=''

    for data1 in data1_list:
        li_list.extend(data1.findAll('tr')) 

    for li in li_list:
        img = li.find('img')
        img_src = img['src']
        title = img['alt']

        for el in li.find_all('td', {'class' : 'Rkdate'}):
            test = el.get_text()
            test2 = re.sub('\r\n\t\t\t\t\t\t\t', '', test)
            check = len(test2)
            # 날짜와 장소 구분
            if check == 23 :
                date = test2
            else:
                location = test2

        concert_obj = {
            'title' : title,
            'image_url' : img_src,
            'location' : location,
            'date' : date
        }
        data.append(concert_obj)

    print(data)

    for item in data:
        print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="페스티벌").save()    
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data

if __name__ == '__main__':
    start()
    start2()
    start3()