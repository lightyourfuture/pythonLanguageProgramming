import jieba  # 导入 jieba 库,用于中文分词
import requests  # 导入 requests 库,用于发起网络请求

# 发起网络请求获取<三国演义>文本内容
response = requests.get("https://python123.io/resources/pye/threekingdoms.txt")
txt = response.text  # 获取请求响应的文本内容

# 设置排除词汇的集合,这些词汇在统计时将不予考虑
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", 
            "商议", "如何", "主公","军士","左右","军马","引兵",
            "次日","大喜","天下","东吴","于是","今日","不敢",
            "魏兵","陛下","一人","都督","人马","不知","汉中",
            "只见","众将","后主","蜀兵","上马","大叫","太守",
            "此人","夫人","先主","后人","背后","城中","天子",
            "一面","何不","大军","忽报","先生","百姓","何故",
            "然后","先锋","不如","赶来","原来","令人","江东",
            "下马","喊声","正是","徐州","忽然","因此","成都",
            "不见","未知","大败","大事","之后","一军","引军",
            "起兵","军中","接应","进兵","大惊","可以","以为",
            "大怒","不得","心中","下文","一声","追赶","粮草",
            "大叫","之计","起兵","以为","以后","以兵","入城"
            }

# 使用 jieba 对文本进行分词
words = jieba.lcut(txt)

# 初始化一个字典,用于存储词汇及其出现的次数
counts = {}

# 遍历分词结果,统计词汇出现的次数
for word in words:
    if len(word) == 1:  # 如果词语长度为1(单个字),则跳过不计
        continue
    # 对特定的人物名称进行统一处理,以便统计时不分散计数
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1  # 更新词汇计数

# 从统计结果中删除需要排除的词汇
for word in excludes:
    del counts[word]

# 将统计结果转换为列表,并按照出现次数降序排序
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

# 打印出现次数最多的前10个词汇及其次数
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))