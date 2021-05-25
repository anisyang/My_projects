from bs4 import BeautifulSoup
from pprint import pprint
import requests
import pymysql
from datetime import datetime

conn = pymysql.connect(host='localhost', user='itest', password='plmokn7034.tk', db='new_pics', charset='utf8')
curs = conn.cursor()

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

data1 = soup.find('div', {'class': 'weather_box'})

find_address = data1.find('span', {'class':'btn_select'}).text
print('현재 서버 위치: '+find_address)

find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
print('현재 서버 주변 온도: '+find_currenttemp+'℃')

data2 = data1.findAll('dd')
find_dust = data2[0].find('span', {'class':'num'}).text
find_ultra_dust = data2[1].find('span', {'class':'num'}).text
find_ozone = data2[2].find('span', {'class':'num'}).text
print('현재 서버 주변 미세먼지 농도: '+find_dust)
print('현재 서버 주변 초미세먼지 농도: '+find_ultra_dust)
print('현재 서버 주변 오존지수: '+find_ozone)

#name = "자동 업로드"
#pw = "hill0208"
Title = "현재 기상상태"
date = datetime.today().strftime("%Y-%m-%d")
sub_title="자동 업로드 입니다."
img_url="test"
#hit = '0'
content ="현재 미세먼지: {}\n 현재 초미세먼지: {}\n 현재 오존지수:{}\n".format(find_dust, find_ultra_dust,find_ozone)
#lock_post = '0'
#files =""



sql = """insert into pics_table(Title,img_url,sub_title,content,date)
         values (%s, %s, %s, %s, %s)"""
curs.execute(sql, (Title,img_url,sub_title,content,date))
conn.commit()
 
conn.close()
