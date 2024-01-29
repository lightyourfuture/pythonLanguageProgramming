import wordcloud

# 准备文本数据
txt = "life is short, you need python"

# 创建WordCloud对象，设置背景颜色为白色
w = wordcloud.WordCloud(background_color="white")

# 向WordCloud对象中加载文本
w.generate(txt)

# 将生成的词云保存为PNG格式的图像文件
w.to_file("pywcloud.png")