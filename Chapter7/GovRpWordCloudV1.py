import jieba
import wordcloud
from imageio import imread  # Use imageio.imread instead of scipy.misc.imread

# Read the mask image
mask = imread("fivestart.png")

# Read the text file
with open("新时代中国特色社会主义.txt", "r", encoding="utf-8") as f:
    t = f.read()

# Segment the text
ls = jieba.lcut(t)
txt = "".join(ls)

# Create a WordCloud object
w = wordcloud.WordCloud(
    font_path="msyh.ttc",  # Specify the path to the Chinese font file
    mask=mask,  # Use the image for the shape of the word cloud
    width=1000,  # Set the width of the canvas
    height=700,  # Set the height of the canvas
    background_color="white",  # Set the background color of the canvas
)

# Generate the word cloud from the segmented text
w.generate(txt)

# Save the word cloud to a file
w.to_file("grwordcloud.png")
