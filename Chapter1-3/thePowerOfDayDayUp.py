# 问题1:一年365天,每天进步1%,累计进步多少呢？
# 问题2:一年365天,每天退步1%,累计剩余多少呢？
print("问题1:1%的力量")
print("一年365天,每天进步1%,累计进步多少呢？")
dayUp = pow(1.01, 365)
print("向上：{:.2f}".format(dayUp))
print("一年365天,每天退步1%,累计剩余多少呢？")
dayDown = pow(0.99, 365)
print("向下：{:.2f}".format(dayDown))
print("问题2:千分之五和百分之一的力量")
# 使用变量的好处是只需要修改一处,就可以修改所有的地方
dayFactor = 0.005
dayUp = pow(1 + dayFactor, 365)
dayDown = pow(1 - dayFactor, 365)
print("向上：{:.2f},向下：{:.2f}".format(dayUp, dayDown))
print("问题3:工作日的力量")
print("一年365天,一周5个工作日,每天进步1%,周末休息,一年365天,进步多少呢？")
dayUp = 1.0
dayFactor = 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        dayUp = dayUp * (1 - dayFactor)
    else:
        dayUp = dayUp * (1 + dayFactor)
print("工作日的力量：{:.2f}".format(dayUp))
print("问题4:工作日的努力")
print("工作模式要努力到什么水平,才能与每天努力1%的人一样呢？")
print("A君:一年365天,每天进步1%,不停歇？")
print("B君:一年365天,每周工作5天,休息两天,休息日下降1%,要多努力呢？")

dayUpA = pow(1.01, 365)


def dayUp(df):
    """根据每天的努力程度,计算一年的努力程度"""
    dayUp = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayUp = dayUp * (1 - 0.01)
        else:
            dayUp = dayUp * (1 + df)
    return dayUp


dayFactor = 0.01
while dayUp(dayFactor) < dayUpA:
    dayFactor += 0.001
print("工作日的努力程度是：{:.3f}".format(dayFactor))

