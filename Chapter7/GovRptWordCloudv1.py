# GovRptWordcloudv1.py
import jieba
import wordcloud
import requests

# Opening the file. Note the use of correct quotation marks and encoding parameter.
respond = requests.get("https://python123.io/resources/pye/关于实施乡村振兴战略的意见.txt")
f = respond.text

# Using jieba to segment the text
ls = jieba.lcut(f)
txt = "".join(ls)

# Creating a wordcloud object. Note that 'WordCloud' is properly capitalized.
w = wordcloud.WordCloud(
    font_path="msyh.ttc", width=1000, height=700, background_color="white"
)

# Generating and saving the wordcloud
w.generate(txt)
w.to_file("GovRptWordcloud.png")
