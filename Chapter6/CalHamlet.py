#CalHamietVi.py
import requests

def getText():
    response = requests.get("https://python123.io/resources/pye/hamlet.txt")
    # open()函数只能用于打开本地文件,不能用于打开URL.
    # 如果你想从URL读取文件,你需要使用一个可以处理HTTP请求的库,如requests.
    txt = response.text
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, ' ')
    return txt
# 从getText函数获取文本
hamletTxt = getText()

# 使用空格分割文本,得到单词列表
words = hamletTxt.split()

# 创建一个空字典来存储每个单词的出现次数
counts = {}

# 遍历单词列表
for word in words:
    # 对于每个单词,如果它已经在字典中,那么增加它的计数;如果它不在字典中,那么添加到字典并设置计数为1
    counts[word] = counts.get(word, 0) + 1

# 将字典转换为列表,每个元素是一个元组,元组的第一个元素是单词,第二个元素是计数
items = list(counts.items())

# 对列表进行排序,排序的关键是元组的第二个元素(计数),并且是降序排序
items.sort(key=lambda x: x[1], reverse=True)

# 打印出现次数最多的前10个单词及其出现次数
for i in range(10):
    word, count = items[i]
    print("{0:<10}:{1:>5}".format(word, count))                                                  
