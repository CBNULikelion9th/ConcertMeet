from bs4 import BeautifulSoup
from django.db import models
import requests, re, os
from PIL import Image
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "concertmeet.settings")
import django

django.setup()
from meetapp.models import Concert

def hiphop():
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
        link = li.find("a")["href"]
        f_link = "http://ticket.interpark.com" + link;

        for el in li.find_all('td', {'class' : 'Rkdate'}):
            test = el.get_text()
            test2 = re.sub('\r\n\t\t\t\t\t\t\t', '', test)
            check = len(test2)
            # 날짜와 장소 구분
            if check == 23 :
                date = test2
            else:
                location = test2

        # print(f_link);
        concert_obj = {
            'title' : title,
            'image_url' : img_src,
            'location' : location,
            'date' : date,
            'link' : f_link
        }
        data.append(concert_obj)

    # print(data)

    for item in data:
        # print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="힙합", link=item['link']).save()    
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data

def indi():
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
        link = li.find("a")["href"]
        f_link = "http://ticket.interpark.com" + link;

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
            'date' : date,
            'link' : f_link
        }
        data.append(concert_obj)

    # print(data)

    for item in data:
        # print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="인디", link=item['link']).save()        
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data

def festival():
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
        link = li.find("a")["href"]
        f_link = "http://ticket.interpark.com" + link;

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
            'date' : date,
            'link' : f_link
        }
        data.append(concert_obj)

    # print(data)

    for item in data:
        # print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="페스티벌", link=item['link']).save()        
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data

def ballad():
    html = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Bal#")
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
        link = li.find("a")["href"]
        f_link = "http://ticket.interpark.com" + link;

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
            'date' : date,
            'link' : f_link
        }
        data.append(concert_obj)

    # print(data)

    for item in data:
        # print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="발라드", link=item['link']).save()        
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data

def rock():
    html = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Roc#")
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
        link = li.find("a")["href"]
        f_link = "http://ticket.interpark.com" + link;

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
            'date' : date,
            'link' : f_link
        }
        data.append(concert_obj)

    # print(data)

    for item in data:
        # print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="락", link=item['link']).save()        
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data

def jazz():
    html = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Jaz#")
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
        link = li.find("a")["href"]
        f_link = "http://ticket.interpark.com" + link;

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
            'date' : date,
            'link' : f_link
        }
        data.append(concert_obj)

    # print(data)

    for item in data:
        # print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="재즈", link=item['link']).save()        
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data

def pop():
    html = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=For#")
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
        link = li.find("a")["href"]
        f_link = "http://ticket.interpark.com" + link;

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
            'date' : date,
            'link' : f_link
        }
        data.append(concert_obj)

    # print(data)

    for item in data:
        # print(item['image_url'])
        try:
            Concert(title = item['title'], image_url=item['image_url'], location=item['location'], date=item['date'], genre="내한공연", link=item['link']).save()        
            # print("new item added!! " + item['title'])
        except:
            # 데이터 중복 시 저장 불가
            print("중복")
    return data


if __name__ == '__main__':
    hiphop()
    ballad()
    pop()
    rock()
    jazz()
    festival()
    indi()
