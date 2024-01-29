import jieba
import wordcloud
import requests

# 读取文本文件
response = requests.get("https://python123.io/resources/pye/新时代中国特色社会主义.txt")
t = response.text

# 利用jieba进行中文分词
ls = jieba.lcut(t)
txt = "".join(ls)

# 创建wordcloud.WordCloud对象，设置词云参数
w = wordcloud.WordCloud(
    font_path="msyh.ttc", width=1000, height=700, background_color="white"
)

# 生成词云
w.generate(txt)

# 将生成的词云保存为图像文件
w.to_file("reportWordCloud.png")
