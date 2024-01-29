# 导入所需的库
import jieba
import requests

# 定义一个函数来计算词频
def calculate_word_frequency():
    """
    这个函数计算从URL获取的文本中每个词的频率.
    它使用jieba库进行中文分词,使用requests库从URL获取文本.
    词频存储在字典中,然后按降序排序.
    打印出频率最高的前15个词及其频率.
    """
    # 从URL获取文本
    response = requests.get("https://python123.io/resources/pye/threekingdoms.txt")
    txt = response.text

    # 使用jieba库进行中文分词
    words = jieba.lcut(txt)

    # 创建一个空字典来存储每个词的频率
    counts = {}

    # 遍历词列表
    for word in words:
        # 如果词的长度为1,忽略它
        if len(word) == 1:
            continue
        # 否则,如果词已经在字典中,增加它的计数;如果词不在字典中,添加到字典并设置计数为1
        else:
            counts[word] = counts.get(word, 0) + 1

    # 将字典转换为列表,每个元素是一个元组,元组的第一个元素是词,第二个元素是频率
    items = list(counts.items())

    # 对列表进行排序,排序的关键是元组的第二个元素(频率),并且是降序排序
    items.sort(key=lambda x: x[1], reverse=True)

    # 打印出频率最高的前15个词及其频率
    for i in range(15):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))

# 调用函数
calculate_word_frequency()