from konlpy.tag import Kkma
from konlpy.utils import pprint
import pymysql

conn = pymysql.connect(host='localhost', user='itest', password='plmokn7034.tk', db='konlpy', charset='utf8')
curs = conn.cursor()

kkma=Kkma()
# pprint(kkma.pos(u'안녕 하세요 테스트 입니다.'))

reading = input("입력하세요: ")
sep = kkma.pos(reading)
# print(type(aaa))

for value in sep:
    # print(value)
    word, part = value
    print("word:{}, part:{}".format(word,part))
    

    sql = """insert into morpheme(word,part) values(%s, %s)"""

    curs.execute(sql,(word,part))

conn.commit()
conn.close()
