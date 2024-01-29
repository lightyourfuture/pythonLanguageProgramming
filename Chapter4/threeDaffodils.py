# 三位水仙花数
# "水仙花数"是指一个三位整数,其各位数字的3次方和等于该数本身.
# 例如:ABC是一个"3位水仙花数",则:A的3次方＋B的3次方＋C的3次方 = ABC.
# 请按照从小到大的顺序输出所有的3位水仙花数,请用"逗号"分隔输出结果.
# 初始化一个空列表来存储水仙花数
narcissistic_numbers = []

# 遍历所有的三位数
for num in range(100, 1000):
    # 计算每位数字
    a = num // 100  # 百位
    b = (num // 10) % 10  # 十位
    c = num % 10  # 个位
    
    # 检查是否为水仙花数
    if a**3 + b**3 + c**3 == num:
        narcissistic_numbers.append(num)

# 输出结果
print("所有的三位水仙花数是:", ', '.join(map(str, narcissistic_numbers)))
