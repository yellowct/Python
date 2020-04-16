import requests
import os
from bs4 import BeautifulSoup
# 1.创建文件夹
path = './photo'
imgs = []
if os.path.exists(path) == False:
    os.makedirs(path)
# 加headers防gank
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
url = 'https://www.zhihu.com/question/26620889/answer/905030937'
res = requests.get(url, headers=headers)
bs = BeautifulSoup(res.text)
# 2.获取所有图片路径
texts = bs.find_all('img', class_='origin_image')
# 生成图片路径list
for i in texts:
    if i not in imgs:
        imgs.append(i.get('data-original'))
# 去重
photo = list(set(imgs))
# 3.循环保存图片到本地
for i, j in enumerate(photo):
    # 获取图片二进制文本
    img = requests.get(j, headers=headers).content
    # 以索引为图片名
    img_name = str(i) + '.jpg'
    # 保存到本地
    with open(path + '/' + img_name, 'wb') as file:
        file.write(img)

# url = 'https://pic2.zhimg.com/v2-cf78768bea163035880695bb715fcba3_r.jpg'
# img = img = requests.get(url).content
# img_name = 'hct.jpg'
# with open(path + '/' + img_name, 'wb') as file:
#     file.write(img)

# with open('C:\\Users\\Administrator\\Desktop\\imgs\\' + str(i.get('data-original')), 'wb') as file:
#     file.write(i.get('data-original'))
# url = 'https://club.jd.com/discussion/getProductPageImageCommentList.action?productId=1198996&isShadowSku=0&callback=jQuery8798734&page=1&pageSize=10&_=1583918609625'
# # print(url)
# req = requests.get(url)
# # req.encoding = 'GBK'
# # html = req.text
# # content = json.loads(req.text)
# # bf = BeautifulSoup(html)
# # texts = bf.find_all('div', class_='comment-con')
# # texts = texts[0].text.replace('\xa0' * 8, '\n\n')
# string = req.text.lstrip('jQuery8798734(').rstrip(');')
# json = json.loads(string)
# com_list = json['imgComments']['imgList']
# # path = "D:\Python\program\text.txt"
# with open(r"D:\Python\program\text.txt", "w") as file:
#     for i in com_list:
#         file.write(i['commentVo']['content'] + '\n')

# jd = json.loads(
#     req.text.lstrip('jQuery8798734(').rstrip(');'))

# com_list = jd['imgList']
# print(req.text)
# html = html.replace('jQuery8798734', '')
# html = html.rsplit(";")
# html = json.loads(html)
# print(jd)
# import requests

# def getHTMLText(url):
#     try:
#         kv = {'user-agent': 'Mozilla/5.0'}
#         r = requests.get(url, headers=kv, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text[:3000]
#     except Exception as err:
#         return str(err)

# if __name__ == '__main__':
#     url = 'https://www.amazon.com/-/zh/dp/B000LXA9YI?pf_rd_r=KF0017G55QNAE6RKST8B&pf_rd_p=3e7c8265-9bb7-5ab2-be71-1af95f06a1ad&pd_rd_r=c6213375-ef3e-407b-b4d0-93acc30263a4&pd_rd_w=pOrWY&pd_rd_wg=bayyR&ref_=pd_gw_ri&th=1'
#     print(getHTMLText(url))

# import requests
# url = "https://www.amazon.com/-/zh/Apple-Clear-Case-iPhone-11/product-reviews/B07XQSSC2T/ref=cm_cr_getr_d_paging_btm_prev_3?ie=UTF8&reviewerType=all_reviews&pageNumber=1"
# try:
#     kv = {'user-agent': 'Mozilla/5.0'}
#     r = requests.get(url, headers=kv)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[1000:2000])
# except:
#     print("爬取失败")
