# turtle正方形绘制
# 使用turtle库，绘制一个正方形。
# 注意：这不是自动评阅题目，仅用于练习，没有评阅。
# 首先，我们需要导入turtle库。
# 然后，我们将设置画笔的起始位置和方向。
# 接着，我们将使用一个for循环来绘制正方形的四条边。
# 在每次迭代中，我们将向前移动一定的距离，然后右转90度。
# 最后，我们将调用turtle.done()来完成绘图。
# 以下是实现这个功能的Python代码：
import turtle

# 设置起始位置
turtle.penup()
turtle.goto(-100, -100)  # 这将把画笔移动到(-100, -100)的位置
turtle.pendown()

# 绘制正方形
for i in range(4):
    turtle.forward(200)  # 向前移动200个单位
    turtle.right(90)  # 右转90度

# 完成绘图
turtle.done()
