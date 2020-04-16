import requests
import os
from bs4 import BeautifulSoup

# 1.创建文件夹
path = './photo'
if os.path.exists(path) == False:
    os.makedirs(path)

# 2.获取所有图片路径
# 加headers防止404错误（某些网站有反爬机制）
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
# 以知乎某回答中的图片为例
url = 'https://www.zhihu.com/question/26620889/answer/905030937'
res = requests.get(url, headers=headers)
bs = BeautifulSoup(res.text)
# 获取所有class为origin_image的img标签
texts = bs.find_all('img', class_='origin_image')
# 循环生成图片路径list
imgs = []
for i in texts:
    if i not in imgs:
        # 获取img标签中data-original属性的值，即图片url
        imgs.append(i.get('data-original'))
# 去重（爬图过程中可能会产生重复路径）
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
        