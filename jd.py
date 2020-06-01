import requests
import json
import pymysql
import time

db = pymysql.connect('localhost', 'root', '', 'db_products')
mysql = db.cursor()


def jd(data_type):
    break_flag = False
    for i in range(0, 100):
        print(i)
        url = 'https://club.jd.com/comment/productPageComments.action'
        data = {
            # 'callback': 'fetchJSON_comment98',
            'productId': data_type[1],
            'score': 0,
            'sortType': 5,
            'page': i,
            'pageSize': 10,
        }
        headers = {
            'Cookie':
            'unpl=V2_ZzNtbREHExUhAUIDfRsJAmIDR1gSUUYWcAgWUn4fWwdnBxZYclRCFnQUR1BnGlUUZwYZXUJcQhVFCEdkfh1eAmUzIlxyVEMlfThGVHIQXgJuABNccmdEJUVTEzp%2bHlpWNwNCXUJUEUJ9OEZReRlbBGIBEVVyVnMVcA1OVXsbXQZuM1kzQxpDFXwBRFNyGl0EVwIiXg%3d%3d; __jdv=76161171|www.infinitynewtab.com|t_45363_|tuiguang|baa1e85f73d641d4a74241a747631554|1590646215178; areaId=19; ipLoc-djd=19-1607-3155-0; qd_ad=-%7C-%7C-%7C-%7C0; qd_uid=KAQDUY1R-ILCDG3EQSS9QI7272KMA; qd_fs=1590646504669; qd_ts=1590646504669; qd_ls=1590646504669; qd_sq=1; __jdc=122270672; 3AB9D23F7A4B3C9B=D6GXZC7GHVVAMZTIHTHXZA77K52DRRV3OMXNO4FUXXIN6G5BJPS6UU5KTRGTY5FMQJRMXHXEAGKRDZLFH5V7GBBFRQ; shshshfp=4a900e25b154cae027a177c05f2e5bb7; jwotest_product=99; __jda=122270672.1188368200.1572600050.1590653065.1590657945.21;',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        # print(url)
        html = requests.get(url, params=data, headers=headers).text
        data = json.loads(html)
        if data['comments'] == []:
            break
        elif break_flag is True:
            break
        else:
            for comments in data['comments']:
                # print(i)
                if comments['content'] == "此用户未填写评价内容":
                    break_flag = True
                    break
                sql = "insert into t_products (grade,content,type) values (%s,%s,%s)"
                mysql.execute(
                    sql,
                    (comments['score'], comments['content'], data_type[1]))
                db.commit()
            time.sleep(1)
    return 'exit'


data_type = ['1002', '100003656027']
res = jd(data_type)
print(res)
