import requests
import re
# import json
import pymysql


def movies(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    proxies = {"http": "http://123.207.96.189:80"}
    res = requests.get(url, headers=headers, proxies=proxies)
    text = res.text
    regix = '<div class="item">.*?<div class="pic">.*?<em class="">(.*?)</em>.*?<img.*?src="(.*?)" class="">.*?div class="info.*?class="hd".*?class="title">(.*?)</span>.*?<div class="bd">.*?<p class="">(.*?)<br>(.*?)</p>.*?class="star.*?<span class="(.*?)"></span>.*?span class="rating_num".*?average">(.*?)</span>'
    movies = re.findall(regix, text, re.S)
    for movie in movies:
        index = movie[3].strip()[4:-1].find(" ")
        yield {
            'name': movie[2],
            'director': movie[3].strip()[4:index + 4],
            'score': movie[6],
        }

def main():
    db = pymysql.connect('localhost', 'root', '', 'db_test')
    mysql = db.cursor()
    for offset in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
        for item in movies(url):
            # print(item)
            sql = "insert into douban250 (name,director,score) values (%s,%s,%s)"
            mysql.execute(sql, (item['name'], item['director'], str(item['score'])))
            db.commit()        

if __name__ == '__main__':
    main()
