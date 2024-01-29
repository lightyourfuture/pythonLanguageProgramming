# 获取星期字符串
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
# 获取用户输入的数字
weekId = eval(input("请输入星期数字(1-7):"))
# 计算星期的起始位置
pos = (weekId - 1) * 3
# 截取字符串
weekStr = weekStr[pos:pos + 3]
# 输出结果
print(weekStr)
