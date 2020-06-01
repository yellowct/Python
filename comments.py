import requests
import re
import pymysql
import time
from socket import *  # NOQA
import json

db = pymysql.connect('localhost', 'root', '', 'db_products')
mysql = db.cursor()


def amazon(data_type, page):
    url = "https://www.amazon.com/hz/reviews-render/ajax/reviews/get/"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "cookie":
        'session-id=134-2998548-7757361; i18n-prefs=USD; lc-main=zh_CN; ubid-main=134-8208768-6948515; x-wl-uid=1QcpoeuvAL28lY1GSwF9mVDLsMmwNDo7nud00xgj0+YZaRFhSwvBFjIgIRJRBCi+dDH0hAUMWeDE=; session-id-time=2082787201l; s_nr=1583982015710-New; s_vnum=2015982015711%26vn%3D1; s_dslv=1583982015712; sp-cdn="L5Z9:CN"; csm-hit=tb:Y7C6D4BH2KCNQGQMZTF2+s-5GFAN7DW3XXXAGSPGX5F|1590635124245&t:1590635124245&adb:adblk_no; session-token=oMTfbCWHdQH2MWu23OBV+GeR/G1jL6j/ZQ1MyBcFL8yE1lmYNRkpDTWW1bgbvUMBNXny4Il4komDAtbpkkHUw8g5kSg9ae3+PO/hEnybuxGzrX0rPTAZliz0/Soh06aENrdoaogWYDm9NR9mQ0ZJG0jl8okZbnYq0L3v0LAatycpMuhkpeFJZH9bdTIgUJe7'
    }

    asin = data_type[1]
    data = {
        'reviewerType': 'all_reviews',
        'pageNumber': page,
        'asin': asin,
    }
    html = requests.post(url, headers=headers, data=data, timeout=5).text
    regix = 'a-icon-alt\\\\">(.*?) out of 5 stars</span>.*?a-row a-spacing-small review-data\\\\">.*?span>(.*?)</span>'
    res = re.findall(regix, html, re.S)
    save_amazon(res, data_type)
    return res


def jd(data_type):
    break_flag = False
    for i in range(0, 100):
        print(i)
        url = 'https://club.jd.com/comment/productPageComments.action'
        data = {
            'productId': data_type[1],
            'score': 0,
            'sortType': 5,
            'page': i,
            'pageSize': 10,
        }
        headers = {
            'Cookie':
            '__jdu=1188368200; shshshfpa=9d728c45-a916-4350-f906-068416ca9332-1575275266; shshshfpb=s2586a9PVepGntc4eoSAkFA%3D%3D; unpl=V2_ZzNtbREHExUhAUIDfRsJAmIDR1gSUUYWcAgWUn4fWwdnBxZYclRCFnQUR1BnGlUUZwYZXUJcQhVFCEdkfh1eAmUzIlxyVEMlfThGVHIQXgJuABNccmdEJUVTEzp%2bHlpWNwNCXUJUEUJ9OEZReRlbBGIBEVVyVnMVcA1OVXsbXQZuM1kzQxpDFXwBRFNyGl0EVwIiXg%3d%3d; __jdv=76161171|www.infinitynewtab.com|t_45363_|tuiguang|baa1e85f73d641d4a74241a747631554|1590646215178; areaId=19; ipLoc-djd=19-1607-3155-0; qd_ad=-%7C-%7C-%7C-%7C0; qd_uid=KAQDUY1R-ILCDG3EQSS9QI7272KMA; qd_fs=1590646504669; qd_ts=1590646504669; qd_ls=1590646504669; qd_sq=1; __jdc=122270672; 3AB9D23F7A4B3C9B=D6GXZC7GHVVAMZTIHTHXZA77K52DRRV3OMXNO4FUXXIN6G5BJPS6UU5KTRGTY5FMQJRMXHXEAGKRDZLFH5V7GBBFRQ; shshshfp=4a900e25b154cae027a177c05f2e5bb7; jwotest_product=99; __jda=122270672.1188368200.1572600050.1590653065.1590657945.21; JSESSIONID=5927EF204C28F9421786A3FDF1D8A4FB.s1; shshshsID=54dd604c2b309726c023a880f96b3500_13_1590659402771; __jdb=122270672.13.1188368200|21.1590657945',
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


def tmall(data_type):
    for i in range(1, 100):
        headers = {
            'cookie':
            'cna=wpE+FnvIkw0CAXd7xE9wdTc4; csa=0_0_0_0_0_0_0_0_0_0_0_0_0; sm4=440300; lid=ct_h%E6%A5%9A%E7%89%B9; enc=RdBF%2FoqM8h%2BwZM%2FwXcjGKrei0%2FzyfhQVrFtTjt%2B6%2FVmA2Q5S%2BWpckgAmyLc%2F7J2OmL3c9LmFA4YHtBzW4%2FPtqw%3D%3D; _m_h5_tk=a1524c62556b378da0a24656fecec64a_1590748388653; _m_h5_tk_enc=965c2f81b16e66604d88257ceebdd9cd; sgcookie=ErM4YnAehlRv8zePrpkIa; uc1=cookie14=UoTV7NFp6xUONA%3D%3D; t=dc3ffdc117d476112d16ebebbf97fb12; uc3=nk2=AG52vaYk7cI%3D&vt3=F8dBxGevyo7VmAtYt2k%3D&id2=UojVdaR6xdjerA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=ct_h%5Cu695A%5Cu7279; uc4=nk4=0%40AgBvi2Zdp%2B4E6jH%2BPRZeLVrh5g%3D%3D&id4=0%40UOBRFi4s2e3Rn0zk8ZS%2BZtcHZnO6; lgc=ct_h%5Cu695A%5Cu7279; _tb_token_=eee97d3befeb3; cookie2=157aac0a2ce99bd6860d175fd24f7daf; x5sec=7b22726174656d616e616765723b32223a223434643863323064653230633932396564663966616638343566366661623331434f7577772f5946454a4b2b3073584a784f5154227d; l=eBrPm7m4QOs8p-5hBO5Zourza779oCRf1sPzaNbMiInca1yPMsg1sNQDHfHpydtjgt5fYetPOzL1BRFvW84_Wx_ceTwhKXIpBjpM8e1..; isg=BK6u50IafElscoh4zOSunrgL_wRwr3KpdIrw-thznrAPu00VQD19u2X9cydXY2rB',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            "referer": 'https://detail.tmall.com/item.htm'
        }
        data = {
            'itemId': data_type[1],
            # 'spuId': spuId,
            'sellerId': data_type[2],
            'order': "3",
            'currentPage': i
        }
        url = 'https://rate.tmall.com/list_detail_rate.htm'
        html = requests.get(url, headers=headers, params=data).text
        result = re.findall('rateContent":"(.*?)","fromMall"', html)
        if result == []:
            break
        else:
            print(i)
            for content in result:
                # print(content)
                if content != '此用户没有填写评论!':
                    db = pymysql.connect('localhost', 'root', '',
                                         'db_products')
                    mysql = db.cursor()
                    sql = "insert into t_products (content,type) values (%s,%s)"
                    mysql.execute(sql, (content, data_type[1]))
                    db.commit()
        time.sleep(2)
    return 'exit'


def spider(data_type):
    for i in range(1, 1000):
        if i % 10 == 0:
            time.sleep(3)
        print(i)
        try:
            spider = amazon(data_type, i)
        except Exception as e:
            print(e)
            spider = amazon(data_type, i)
        # print(spider)
        if spider == []:
            return "exit"
            break
        elif spider is None:
            return "爬取失败"
            break


def check(data_type):
    count1 = rows(data_type)
    print(count1)
    if count1 != 0:
        delete(data_type)
    if data_type[0] == str(1001):
        res = spider(data_type)
    elif data_type[0] == str(1002):
        res = jd(data_type)
    else:
        res = tmall(data_type)
    print(res)
    count2 = rows(data_type)
    print(count2)
    msg = str(data_type[0]) + '/' + str(count2)
    # print(msg)
    return msg


def delete(data_type):
    sql = "delete from t_products where type='%s'" % data_type[1]
    rows = mysql.execute(sql)
    print(rows)
    db.commit()


def save_amazon(data, data_type):
    for i in data:
        sql = "insert into t_products (grade,content,type) values (%s,%s,%s)"
        grade = i[0]
        if '&nbsp;' in i[1]:
            content = i[1].split('&nbsp;')[1].replace('<br />', '')
        else:
            content = i[1].replace('<br />', '')
        mysql.execute(sql, (grade, content, data_type[1]))
        db.commit()


def rows(data_type):
    sql = "select * from t_products where type='%s'" % data_type[1]
    mysql.execute(sql)
    count = len(mysql.fetchall())
    return count


def get(data_type):
    db = pymysql.connect('localhost',
                         'root',
                         '',
                         'db_products',
                         cursorclass=pymysql.cursors.DictCursor)
    mysql = db.cursor()
    sql = "select grade,content from t_products where type='%s'" % data_type[1]
    mysql.execute(sql)
    res = mysql.fetchall()
    message = ",".join(map(str, res))
    msg1 = message.replace("},{", "/###/").replace("'grade':", "").replace(
        ", 'content': ", "/$$$/").replace("{", "")
    if data_type[0] == str(1011):
        msg = "1011/###/" + msg1 + '/#####/'
    elif data_type[0] == str(1012):
        msg = "1012/###/" + msg1 + '/#####/'
    else:
        msg = "1013/###/" + msg1 + '/#####/'
    return msg


if __name__ == '__main__':
    data_type = "1003/610144500330/686773455"
    data_type = data_type.split("/")
    res = check(data_type)
    print(res)
    # COD = 'utf-8'
    # HOST = '192.168.1.21'  # 主机ip
    # PORT = 8001  # 软件端口号
    # BUFSIZ = 2048
    # ADDR = (HOST, PORT)
    # SIZE = 10
    # tcpS = socket(AF_INET, SOCK_STREAM)  # 创建socket对象  # NOQA
    # tcpS.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  #加入socket配置，重用ip和端口  # NOQA
    # tcpS.bind(ADDR)  # 绑定ip端口号
    # tcpS.listen(SIZE)  # 设置最大链接数
    # while True:
    #     print("客户端未链接")
    #     conn, addr = tcpS.accept()
    #     print("链接的客户端", addr)
    #     while True:
    #         try:
    #             data = conn.recv(BUFSIZ)  # 读取已链接客户的发送的消息
    #             print(data)
    #             if type(data) == bytes:
    #                 get_data = str(data, encoding="utf-8")
    #             else:
    #                 get_data = data
    #             data_type = get_data.split("/")
    #             if data_type[0][0:3] == str(100):
    #                 msg = check(data_type)
    #             else:
    #                 msg = get(data_type)
    #         except Exception as e:
    #             print(e)
    #             print("断开的客户端", addr)
    #             break
    #         # print("客户端发送的内容:", data.decode(COD))
    #         if not data:
    #             break
    #         conn.send(bytes(msg, encoding='utf-8'))
        # conn.close()  # 关闭客户端链接
    # tcpS.closel()
