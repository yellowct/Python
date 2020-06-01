import requests
import re
import pymysql
import time

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
        elif spider is None:
            return "爬取失败"


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


if __name__ == '__main__':
    data_type = "指令/商品id"
    data_type = data_type.split("/")
    spider(data_type)
