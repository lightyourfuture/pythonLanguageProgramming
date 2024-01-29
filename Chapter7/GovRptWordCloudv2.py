import jieba
import wordcloud
import requests

# Open the file
respond = requests.get("https://python123.io/resources/pye/关于实施乡村振兴战略的意见.txt")
f = respond.text


# Use jieba to segment the text
ls = jieba.lcut(f)
txt = " ".join(ls)

# Create a WordCloud object
w = wordcloud.WordCloud(
    font_path="msyh.ttc",  # Specify the path to the Chinese font file
    width=1000,  # Set the width of the canvas
    height=700,  # Set the height of the canvas
    background_color="white",  # Set the background color of the canvas
    max_words=15,
)  # Limit the number of words in the word cloud

# Generate the word cloud from the segmented text
w.generate(txt)

# Save the word cloud to a file
w.to_file("GovRptWordCloudv2.png")
