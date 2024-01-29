# GovRptWordcloudv1.py
import jieba
import wordcloud
import requests

# Opening the file. Use proper quotation marks and the equal sign for the encoding parameter.
response = requests.get("https://python123.io/resources/pye/新时代中国特色社会主义.txt")
t = response.text

# Using jieba to segment the text. Use proper equal signs for assignment.
ls = jieba.lcut(t)  # Corrected
txt = " ".join(ls)  # Corrected

# Creating a wordcloud object. Correct the class name, use equal signs, and fix width and height values.
w = wordcloud.WordCloud(  # Corrected class name and equal signs
    font_path="msyh.ttc",
    width=1000,  # Corrected (assuming you meant 1000)
    height=700,  # Corrected (assuming you meant 700)
    background_color="white",  # Corrected
    max_words=15,  # Corrected
)

# Generating and saving the wordcloud
w.generate(txt)
w.to_file("reportWordCloudV2.png")
