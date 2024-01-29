import turtle as t  # 导入turtle库,用于绘图


# 定义一个曲线绘制函数
def DegreeCurve(n, r, d=1):
    for i in range(n):  # 循环n次
        t.left(d)  # 向左转d度
        t.circle(r, abs(d))  # 以r为半径,绘制abs(d)度的弧线


# 初始位置设定
s = 0.2  # size,用于调整图形的大小
t.setup(450 * 5 * s, 750 * 5 * s)  # 设置画布的大小
t.pencolor("black")  # 设置画笔颜色为黑色
t.fillcolor("red")  # 设置填充颜色为红色
t.speed(100)  # 设置画笔速度为100
t.penup()  # 提起画笔,移动时不绘制图形
t.goto(0, 900 * s)  # 移动到(0, 900*s)的位置
t.pendown()  # 放下画笔,移动时绘制图形

# 绘制花朵形状
t.begin_fill()  # 开始填充颜色
t.circle(200 * s, 30)  # 以200*s为半径,绘制30度的弧线
DegreeCurve(60, 50 * s)  # 调用DegreeCurve函数,绘制60次,每次以50*s为半径,绘制1度的弧线
t.circle(200 * s, 30)  # 以200*s为半径,绘制30度的弧线
DegreeCurve(4, 100 * s)  # 调用DegreeCurve函数,绘制4次,每次以100*s为半径,绘制1度的弧线
t.circle(200 * s, 50)  # 以200*s为半径,绘制50度的弧线
DegreeCurve(50, 50 * s)  # 调用DegreeCurve函数,绘制50次,每次以50*s为半径,绘制1度的弧线
t.circle(350 * s, 65)  # 以350*s为半径,绘制65度的弧线
DegreeCurve(40, 70 * s)  # 调用DegreeCurve函数,绘制40次,每次以70*s为半径,绘制1度的弧线
t.circle(150 * s, 50)  # 以150*s为半径,绘制50度的弧线
DegreeCurve(20, 50 * s, -1)  # 调用DegreeCurve函数,绘制20次,每次以50*s为半径,绘制-1度的弧线
t.circle(400 * s, 60)  # 以400*s为半径,绘制60度的弧线
DegreeCurve(18, 50 * s)  # 调用DegreeCurve函数,绘制18次,每次以50*s为半径,绘制1度的弧线
t.fd(250 * s)  # 向前移动250*s的距离
t.right(150)  # 向右转150度
t.circle(-500 * s, 12)  # 以-500*s为半径,绘制12度的弧线
t.left(140)  # 向左转140度
t.circle(550 * s, 110)  # 以550*s为半径,绘制110度的弧线
t.left(27)  # 向左转27度
t.circle(650 * s, 100)  # 以650*s为半径,绘制100度的弧线
t.left(130)  # 向左转130度
t.circle(-300 * s, 20)  # 以-300*s为半径,绘制20度的弧线
t.right(123)  # 向右转123度
t.circle(220 * s, 57)  # 以220*s为半径,绘制57度的弧线
t.end_fill()  # 结束填充颜色

# 绘制花枝形状
t.left(120)  # 向左转120度
t.fd(280 * s)  # 向前移动280*s的距离
t.left(115)  # 向左转115度
t.circle(300 * s, 33)  # 以300*s为半径,绘制33度的弧线
t.left(180)  # 向左转180度
t.circle(-300 * s, 33)  # 以-300*s为半径,绘制33度的弧线
DegreeCurve(70, 225 * s, -1)  # 调用DegreeCurve函数,绘制70次,每次以225*s为半径,绘制-1度的弧线
t.circle(350 * s, 104)  # 以350*s为半径,绘制104度的弧线
t.left(90)  # 向左转90度
t.circle(200 * s, 105)  # 以200*s为半径,绘制105度的弧线
t.circle(-500 * s, 63)  # 以-500*s为半径,绘制63度的弧线
t.penup()  # 提起画笔,移动时不绘制图形
t.goto(170 * s, -30 * s)  # 移动到(170*s, -30*s)的位置
t.pendown()  # 放下画笔,移动时绘制图形
t.left(160)  # 向左转160度
DegreeCurve(20, 2500 * s)  # 调用DegreeCurve函数,绘制20次,每次以2500*s为半径,绘制1度的弧线
DegreeCurve(220, 250 * s, -1)  # 调用DegreeCurve函数,绘制220次,每次以250*s为半径,绘制-1度的弧线

# 绘制一个绿色叶子
t.fillcolor("green")  # 设置填充颜色为绿色
t.penup()  # 提起画笔,移动时不绘制图形
t.goto(670 * s, -180 * s)  # 移动到(670*s, -180*s)的位置
t.pendown()  # 放下画笔,移动时绘制图形
t.right(140)  # 向右转140度
t.begin_fill()  # 开始填充颜色
t.circle(300 * s, 120)  # 以300*s为半径,绘制120度的弧线
t.left(60)  # 向左转60度
t.circle(300 * s, 120)  # 以300*s为半径,绘制120度的弧线
t.end_fill()  # 结束填充颜色
t.penup()  # 提起画笔,移动时不绘制图形
t.goto(180 * s, -550 * s)  # 移动到(180*s, -550*s)的位置
t.pendown()  # 放下画笔,移动时绘制图形
t.right(85)  # 向右转85度
t.circle(600 * s, 40)  # 以600*s为半径,绘制40度的弧线

# 绘制另一个绿色叶子
t.penup()  # 提起画笔,移动时不绘制图形
t.goto(-150 * s, -1000 * s)  # 移动到(-150*s, -1000*s)的位置
t.pendown()  # 放下画笔,移动时绘制图形
t.begin_fill()  # 开始填充颜色
t.rt(120)  # 向右转120度
t.circle(300 * s, 115)  # 以300*s为半径,绘制115度的弧线
t.left(75)  # 向左转75度
t.circle(300 * s, 100)  # 以300*s为半径,绘制100度的弧线
t.end_fill()  # 结束填充颜色
t.penup()  # 提起画笔,移动时不绘制图形
t.goto(430 * s, -1070 * s)  # 移动到(430*s, -1070*s)的位置
t.pendown()  # 放下画笔,移动时绘制图形
t.right(30)  # 向右转30度
t.circle(-600 * s, 35)  # 以-600*s为半径,绘制35度的弧线
t.done()  # 结束绘图
