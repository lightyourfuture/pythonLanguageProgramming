import jieba
import wordcloud

# 准备中文文本数据
txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，\
它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理。"

# 创建WordCloud对象，设置图片的宽度、高度以及中文字体
w = wordcloud.WordCloud(width=1000, font_path="msyh.ttc", height=700)

# 使用jieba.lcut方法对中文文本进行分词，然后使用join拼接分词结果
w.generate("".join(jieba.lcut(txt)))

# 将生成的词云保存为图像文件
w.to_file("chinese_wordcloud.png")