import requests
import pymysql
import time
import re
import time


def tmall():
    for i in range(1, 100):
        itemId = '613832405367'
        # spuId = '1183066737'
        sellerId = '2838892713'
        headers = {
            'cookie':
            'cna=wpE+FnvIkw0CAXd7xE9wdTc4; csa=0_0_0_0_0_0_0_0_0_0_0_0_0; sm4=440300; lid=ct_h%E6%A5%9A%E7%89%B9; enc=RdBF%2FoqM8h%2BwZM%2FwXcjGKrei0%2FzyfhQVrFtTjt%2B6%2FVmA2Q5S%2BWpckgAmyLc%2F7J2OmL3c9LmFA4YHtBzW4%2FPtqw%3D%3D; _m_h5_tk=a1524c62556b378da0a24656fecec64a_1590748388653; _m_h5_tk_enc=965c2f81b16e66604d88257ceebdd9cd; sgcookie=ErM4YnAehlRv8zePrpkIa; uc1=cookie14=UoTV7NFp6xUONA%3D%3D; t=dc3ffdc117d476112d16ebebbf97fb12; uc3=nk2=AG52vaYk7cI%3D&vt3=F8dBxGevyo7VmAtYt2k%3D&id2=UojVdaR6xdjerA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=ct_h%5Cu695A%5Cu7279; uc4=nk4=0%40AgBvi2Zdp%2B4E6jH%2BPRZeLVrh5g%3D%3D&id4=0%40UOBRFi4s2e3Rn0zk8ZS%2BZtcHZnO6; lgc=ct_h%5Cu695A%5Cu7279; _tb_token_=eee97d3befeb3; cookie2=157aac0a2ce99bd6860d175fd24f7daf; x5sec=7b22726174656d616e616765723b32223a223434643863323064653230633932396564663966616638343566366661623331434f7577772f5946454a4b2b3073584a784f5154227d; l=eBrPm7m4QOs8p-5hBO5Zourza779oCRf1sPzaNbMiInca1yPMsg1sNQDHfHpydtjgt5fYetPOzL1BRFvW84_Wx_ceTwhKXIpBjpM8e1..; isg=BK6u50IafElscoh4zOSunrgL_wRwr3KpdIrw-thznrAPu00VQD19u2X9cydXY2rB',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            "referer": 'https://detail.tmall.com/item.htm'
        }
        data = {
            'itemId': itemId,
            # 'spuId': spuId,
            'sellerId': sellerId,
            'order': "3",
            'currentPage': i
        }
        url = 'https://rate.tmall.com/list_detail_rate.htm'
        html = requests.get(url, headers=headers, params=data).text
        # time.sleep(10)
        result = re.findall('rateContent":"(.*?)","fromMall"', html)
        # print(result)
        if result == []:
            break
        else:
            print(i)
            for content in result:
                print(content)
                if content != '此用户没有填写评论!':
                    db = pymysql.connect('localhost', 'root', '',
                                         'db_products')
                    mysql = db.cursor()
                    sql = "insert into t_products (content,type) values (%s,%s)"
                    mysql.execute(sql, (content, itemId))
                    db.commit()
        time.sleep(2)
    print('exit')


res = tmall()