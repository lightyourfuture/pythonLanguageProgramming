# turtle六边形绘制
# 使用turtle库，绘制一个六边形。
# 注意：这不是自动评阅题目，仅用于练习，没有评阅。
# 首先，我们需要导入turtle库。
# 然后，我们将设置画笔的起始位置和方向。
# 接着，我们将使用一个for循环来绘制六边形的六条边。
# 在每次迭代中，我们将向前移动一定的距离，然后右转60度。
# 最后，我们将调用turtle.done()来完成绘图。
# 以下是实现这个功能的Python代码：
import turtle

# 设置起始位置
turtle.penup()
turtle.goto(-100, -100)  # 这将把画笔移动到(-100, -100)的位置
turtle.pendown()

# 绘制六边形
for i in range(6):
    turtle.forward(100)  # 向前移动100个单位
    turtle.right(60)  # 右转60度

# 完成绘图
turtle.done()
