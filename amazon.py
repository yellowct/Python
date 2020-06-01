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
<<<<<<< HEAD
    spider(data_type)
=======
    res = check(data_type)
    print(res)
    COD = 'utf-8'
    HOST = '192.168.1.21'  # 主机ip
    PORT = 8001  # 软件端口号
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    SIZE = 10
    tcpS = socket(AF_INET, SOCK_STREAM)  # 创建socket对象  # NOQA
    tcpS.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  #加入socket配置，重用ip和端口  # NOQA
    tcpS.bind(ADDR)  # 绑定ip端口号
    tcpS.listen(SIZE)  # 设置最大链接数
    while True:
        print("服务器启动，监听客户端链接")
        conn, addr = tcpS.accept()
        print("链接的客户端", addr)
        while True:
            try:
                data = conn.recv(BUFSIZ)  # 读取已链接客户的发送的消息
                if type(data) == bytes:
                    data_type = str(data, encoding="utf-8")
                else:
                    data_type = data
                data_type = data_type.split("/")
                if data_type[0] == str(1001):
                    check = check(data_type)
                    msg = '1001/' + str(check)
                    print(msg)
                    conn.send(msg.encode(COD))
                    # conn.send(bytes(data, encoding='utf-8'))
                elif data_type[0] == str(1011):
                    res = get(data_type)
                    msg = ",".join(map(str, res))
                    msg = msg.replace("},{",
                                      "/###/").replace("'grade':", "").replace(
                                          ", 'content': ",
                                          "/$$$/").replace("{", "")
                    conn.send(msg.encode(COD))
            except Exception:
                print("断开的客户端", addr)
                break
            print("客户端发送的内容:", data.decode(COD))
            if not data:
                break
            msg = time.strftime("%Y-%m-%d %X")  # 获取结构化事件戳
            msg1 = '[%s]:%s' % (msg, data.decode(COD))
            conn.send(msg1.encode(COD))  # 发送消息给已链接客户端
        conn.close()  # 关闭客户端链接
    tcpS.closel()


>>>>>>> fd41db8bdb7df31c0b607db809e0258e3d5798e8
