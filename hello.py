# print("Hello 黄楚特")

# 数据类型
# counter = 100  # 赋值整型变量
# miles = 1000.0  # 浮点型
# name = "John"  # 字符串
# print(counter)
# print(miles)
# print(name)

# if True:
#     print('true')
# else:
#     print('false')
# from sys import path

# 字符串
# str = '黄楚特'
# print(str, end="")
# print(str[2:3])
# print(str[0:])
# print(str[0])
# print(str[2:-1])
# print(str * 2)
# print(str + 'hhhh')
# print('-------------------------')
# print('abc\ndedede')
# print(r'abc\ndedede')
# input("\n\n按下 enter 键后退出。")

# 引入
# import sys; x = 'runoob'; sys.stdout.write(x + '\n' + x)
# print('path:', path)
# a, b, c = 1, 2, "runoob"
# print(5**4)

# 列表  与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
# list = []
# # tinylist = [123, 'runoob']
# # list[0] = 'hhh'
# # list[2:5] = []

# 元组  与列表类似，不同之处在于元组的元素不能修改，使用小括号。
# tup = (23, 34)
# print(tup)

# 集合  是一个无序的不重复元素序列。可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
# a = set('abracadabra')
# b = set('alacazam')
# print(a ^ b)

# 字典  字典是另一种可变容器模型，且可存储任意类型对象。字典的每个键值对key=>value用:分割，每个对之间用,分割，整个字典包括在花括号{}中
# tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
# print(tinydict.values())
# print(tinydict.keys())
# this = set(("abc", "def", "ghi"))
# this.add("adad")
# this.update([1, 2], [33, 667])

# "adwdwd" in this
# print(True)

# a, b = 0, 1
# while b < 100:
#     print(b, end=" ")
#     a, b = b, a + b
# number = 7
# guess = -1
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))

#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")

# n = 100
# sum = 0
# count = 1
# while count < n:
#     sum = sum + count
#     count += 1
# print(sum)

# count = 0
# while count < 5:
#     print(count, " 小于 5")
#     count = count + 1
# else:
#     print(count, " 大于或等于 5")
# import sys
# languages = ["C", "C++", "Perl", "Python"]

# for x in languages:
#     if x == "Perl":
#         print("done")
#         # break
#     else:
#         print(x)
# print("exit")

# for x in range(len(languages)):
#     print(x,languages[x])

# 迭代器
# it = iter(languages)
# for i in it:
#     print(i,end=" ")
# while True:
#     try:
# print(next(it))
# except StopIteration:
#     sys.exit()

# # 函数
# def hello():
#     print('abc')

# hello()

# def area(width, height):
#     return width * height

# w = 4
# h = 5
# print(area(w, h))

# a = 1
# while a < 10:
#     print(a)
#     a += 2
# else:
#     print('exit')

# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
# s = 'Hello, Runoob\nabcd'
# print(str(s))
# print(repr(s))

# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
# print('{}网址：{}'.format('百度', 'www.baidu.com'))

# 在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
# print('{a}网址：{b}'.format(a='百度', b='www.baidu.com'))

# str = input("输入姓名：")
# print(
#     str,
#     "是您的儿子",
# )
# 类
# 如果不加self，表示是类的一个属性（可以通过“类名.变量名”的方式引用），加了表示是类的实例的一个属性
# class hct:
#     i = 465456

#     def f(self):
#         return 'hct'

#     def __init__(self, a, b):
#         self.c = a
#         self.d = b

# x = hct(2, 3)
# print(x.i)
# print(x.f())
# print(x.c, x.d)


# 定义类
class people:
    # 定义基本属性
    name = ''
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __age = 0

    #     # 定义构造函数
    #     def __init__(self, a, b):
    #         self.name = a
    #         self.age = b

    #     def out(self):
    #         print(self.name, "今年", self.age, "岁")

    # # # 实例化类
    # # p = people('hct', 18)
    # # # 调用方法
    # # p.out()

    # # 单继承
    # class student(people):
    #     sex = ''

    #     def __init__(self, a, b, c):
    #         # 调用父类的构造函数
    #         people.__init__(self, a, b)
    #         self.sex = c

    #     # 覆写父类方法
    #     def out(self):
    #         print(self.name, "今年", self.age, "岁,性别", self.sex)

    # p = student('hct', 20, '男')
    # p.out()

    # class JustCounter:
    #     __secretCount = 0  # 私有变量
    #     publicCount = 0  # 公开变量

    #     def count(self):
    #         self.__secretCount += 1
    #         self.publicCount += 1
    #         print(self.__secretCount)

    # counter = JustCounter()
    # counter.count()
    # counter.count()
    # print(counter.publicCount)
    # print(counter.__secretCount)  # 报错，实例不能访问私有变量

    # python 实例：

    # 求和
    # num1 = 3
    # num2 = 5
    # sum = num1 + num2
    # print('和为', num1 + num2 )6

    # 平方根
    # num = 9
    # sqrt = num**2
    # print(sqrt)

    # 生成随机数
    # import random
    # num = random.randint(0, 100)
    # print(num)

    # 转换变量
    # x = 1
    # y = 2
    # tamp = x
    # x = y
    # y = tamp
    # print(x)
    # print(y)

    # 判断最大值
    # print(max(4, 5, 6))

    # 字符与ASCII嘛转换
    # print('a的ascii码： ', ord('c'))
    # print('100的字符： ', chr(100))

    # # 计算每个月天数
    # import calendar
    # print(calendar.monthrange(2020, 2))

    # # 日期
    # import datetime
    # # 今天
    # today = datetime.date.today()
    # print(today)
    # # 昨天
    # days = datetime.timedelta(days=1)
    # print(today - days)

    # list 常用操作
    # li = ["a", "b", "mpilgrim", "z", "b", "example"]
    # print(li[1])
    # print(li[-2])
    # li.append('new')
    # li.insert(3, 'hct')
    # li.extend(['4', '5'])
    # print(li.index('z'))
    # li.remove('b')
    # li=li+['gg','mm']
    # li += ['dwdwdw']
    # li += 'dwdwdw'
    # li = li * 2
    # print(li)

    # 链接字符串&分割字符串
    # li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
    # s = ";".join(li)
    # print(s)
    # print(s.split(";"))
    # print(s.split(";", 2))

    # list 的映射解析
    # li = [1, 9, 8, 4]
    # print([elem*2 for elem in li])

    # dictionary 中的解析
    # params = {
    #     "server": "mpilgrim",
    #     "database": "master",
    #     "uid": "sa",
    #     "pwd": "secret"
    # }
    # print(params.keys())
    # print(params.values())
    # print(params.items())
    # print([k for k, v in params.items()])
    # print([v for k, v in params.items()])
    # print(["%s=%s" % (k, v) for k, v in params.items()])

    # list 过滤
    # li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
    # li=[elem for elem in li if len(elem)>1]
    # li=[elem for elem in li if elem != "b"]
    # li=[elem for elem in li if li.count(elem)>1]
    # print(li)

    # 时间格式
    # import time
    # now = time.time()
    # localtime=time.asctime(time.localtime(time.time()))
    # now = time.asctime(time.localtime(time.time()))
    # print(now)
    # print(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))
    # import calendar
    # cal = calendar.month(2020, 2)
    # print(cal)

    # 判断元素是否在列表中存在
    # test_list = [ 1, 6, 3, 5, 3, 4 ]
    # for i in test_list:
    #     if i==4:
    #         print('exit')

    # 清空列表
    # RUNOOB = [6, 0, 4, 1]
    # print(RUNOOB.clear())

    # 计算元素在列表中出现的次数
    # lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
    # print(lst.count(8))

    # 计算列表元素之和
    # total = 0
    # list1 = [11, 5, 17, 18, 23]
    # for elem in list1:
    #     total = total + elem

    # print(total)

    # elem = 0
    # while (elem < len(list1)):
    #     total = total + list1[elem]
    #     elem += 1

    # print(total)

    # 最小/大元素
    # list1 = [10, 20, 4, 45, 99]
    # print(min(list1))
    # print(max(list1))

    # 移除字符串中的指定位置字符
    # new_str = ""
    # test_str = "Runoob"
    # for i in range(0, len(test_str)):
    #     if i != 3:
    #         new_str = new_str + test_str[i]

    # print(new_str)

    # 判断字符串是否存在子字符串
    # test_str = "Runoob"
    # if (test_str.find("o") != -1):
    #     print("存在")

    # 按键(key)或值(value)对字典进行排序
    # 声明字典
    # key_value = {}
    # # 初始化
    # key_value[2] = 56
    # key_value[1] = 2
    # key_value[5] = 12
    # key_value[4] = 24
    # key_value[6] = 18
    # key_value[3] = 323

    # for i in sorted(key_value):
    #     print((i, key_value[i]), end=" ")


# 计算字典值之和
# sum = 0
# for v in key_value.values():
#     sum = sum + v

# print(sum)
# 二分查找
# def binarySearch(
#     arr,
#     i,
#     l,
#     x,
# ):
#     if l >= i:
#         mid = int((i + l) / 2)
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binarySearch(arr, i, mid, x)
#         else:
#             return binarySearch(arr, mid, l, x)
#     else:
#         return -1

# arr = [2, 3, 4, 6, 8, 10, 40]
# x = 10
# l = len(arr) - 1
# i = 0
# res = binarySearch(arr, i, l, x)
# print(res)

# # 线性查找
# arr = ['A', 'B', 'C', 'D', 'E']
# n = len(arr)
# x = "G"

# def search(arr, n, x):
#     for i in range(0, n):
#         if arr[i] == x:
#             return i

#     return -1

# res = search(arr,n,x)
# print(res)

# # 插入排序
# def insertionSort(arr, n):
#     for i in range(1, n):
#         j = i - 1
#         while j >= 0 and arr[j + 1] < arr[j]:
#             tamp = arr[j + 1]
#             arr[j + 1] = arr[j]
#             arr[j] = tamp
#             j -= 1

#     return arr

# arr = [12, 11, 13, 5, 6]
# res = insertionSort(arr, len(arr))
# print(res)

# 冒泡排序
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(0, n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# arr = [64, 34, 25, 12, 22, 11, 90]
# print(bubbleSort(arr))

# 选择排序
# arr = [64, 25, 12, 22, 11]
# for i in range(len(arr)):
#     x = i
#     for j in range(i + 1, len(arr)):
#         if arr[x] > arr[j]:
#             x = j
#     arr[i], arr[x] = arr[x], arr[i]

# print(arr)


# 快速排序
# def quickSort(arr, start, end):
#     if start >= end:
#         return -1
#     mid = arr[start]
#     low = start
#     high = end
#     while low < high:
#         # 从右到左找出小于mid的值
#         while low < high and mid <= arr[high]:
#             high -= 1
#         arr[low] = arr[high]
#         # 从左到右找出大于mid的值
#         while low < high and mid >= arr[low]:
#             low += 1
#         arr[high] = arr[low]
#     arr[low] = mid
#     quickSort(arr, start, low - 1)
#     quickSort(arr, low + 1, end)


# arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# quickSort(arr, 0, len(arr) - 1)
# print(arr)

# def quick_sort(alist, start, end):
#     """快速排序"""
#     if start >= end:  # 递归的退出条件
#         return
#     mid = alist[start]  # 设定起始的基准元素
#     low = start  # low为序列左边在开始位置的由左向右移动的游标
#     high = end  # high为序列右边末尾位置的由右向左移动的游标
#     while low < high:
#         # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
#         while low < high and alist[high] >= mid:
#             high -= 1
#         alist[low] = alist[
#             high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
#         # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
#         while low < high and alist[low] < mid:
#             low += 1
#         alist[high] = alist[
#             low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处

#     # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
#     alist[low] = mid  # 将基准元素放到该位置,
#     # 对基准元素左边的子序列进行快速排序
#     quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
#     # 对基准元素右边的子序列进行快速排序
#     quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后

# if __name__ == '__main__':
#     alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#     quick_sort(alist, 0, len(alist) - 1)
#     print(alist)

from urllib import request
import chardet

# 构建Request
req=request.Request("")

# 访问页面，并获取从服务器的回应，如果是HTTPS？
response=request.urlopen(req)
print(response.geturl()+'\n')
print(response.info())
print(response.getcode())

# 读取页面
html=response.read()

# 检测页面使用的编码
charset=chardet.detect(html)

# 解码：获得易于阅读的网页源码
html=html.decode(charset['encoding']