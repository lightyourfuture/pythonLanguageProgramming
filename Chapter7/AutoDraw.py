# AutoTraceDraw.py
import turtle as t  # 导入turtle库

t.title('自动轨迹绘制')  # 设置窗口标题
t.setup(800, 600, 0, 0)  # 设置窗口大小和位置
t.pencolor("red")  # 设置画笔颜色
t.pensize(5)  # 设置画笔大小

# 数据读取
datals = []

f = open("Chapter7\data.txt")  # 打开文件
for line in f:
    line = line.replace("\n", "")  # 移除行尾的换行符
    datals.append(list(map(eval, line.split(","))))  # 将每行的数据转换成列表,并添加到datals
f.close()  # 关闭文件
# 自动绘制
for i in range(len(datals)):
    # 设置画笔颜色，datals[i][3], datals[i][4], datals[i][5] 应该是RGB颜色值
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])  # 修复了缺少的右括号
    
    # 根据datals的内容前进
    t.fd(datals[i][0])  # 修复了索引，假设datals[i][0]是前进的距离
    
    # 根据datals的内容决定是向左还是向右转，以及转的角度
    if datals[i][1]:  # 判断左转还是右转
        t.right(datals[i][2])  # 右转
    else:
        t.left(datals[i][2])  # 左转
