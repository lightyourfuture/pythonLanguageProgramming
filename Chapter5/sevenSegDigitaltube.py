import turtle as t
import time

# 绘制单段数码管
def drawLine(draw): 
    # 如果draw为True,则下笔,否则抬笔
    t.pendown() if draw else t.penup()
    # 向前移动40个单位
    t.fd(40)
    # 右转90度
    t.right(90)

# 根据数字绘制七段数码管
def drawDigit(digit): 
    # 根据数字的特性,决定是否需要绘制每一段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup() # 为绘制后续数字确定位置
    t.fd(20) # 为绘制后续数字确定位置

# 获得要输出的数字
def drawDate(date): 
    t.pencolor("red")
    for i in date:
        # 根据日期的格式,绘制对应的字符
        if i == '-':
            t.write('年',font=("Arial",18,"normal"))
            t.pencolor("green")
            t.fd(40)
        elif i == '=':
            t.write('月',font=("Arial",18,"normal"))
            t.pencolor("blue")
            t.fd(40)
        elif i == '+':
            t.write('日',font=("Arial",18,"normal"))
        else:
            # 通过eval()函数将数字变为整数,然后绘制
            drawDigit(eval(i)) 

# 主函数
def main():
    # 设置画布大小和位置
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    # 获取当前的日期,并绘制
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    # 这段代码的主要功能是获取当前的日期
    # 并将其格式化为特定的格式
    # 然后在turtle画布上进行显示.
    # time.strftime('%Y-%m=%d+',time.gmtime())
    # 这行代码的作用是获取当前的格林威治时间
    # 并将其格式化为 '年-月=日+' 的形式.
    # 其中,%Y 代表四位数的年份,%m 代表两位数的月份,%d 代表两位数的日期.
    # -,= 和 + 是自定义的分隔符
    # 用于在后续的 drawDate 函数中判断应该绘制哪个字符.
    # drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    # 这行代码的作用是调用 drawDate 函数,将格式化后的日期字符串传入.
    # 在 drawDate 函数中,会遍历这个日期字符串,对于每个字符
    # 如果是 -,就在画布上写下 '年',并将画笔颜色改为绿色;
    # 如果是 =,就在画布上写下 '月',并将画笔颜色改为蓝色;
    # 如果是 +,就在画布上写下 '日'.
    # 对于其他的字符,都视为数字,会调用 drawDigit 函数
    # 将这个字符转换为整数,然后在画布上绘制对应的七段数码管数字.
    t.hideturtle()
    t.done()

# 调用主函数
main()