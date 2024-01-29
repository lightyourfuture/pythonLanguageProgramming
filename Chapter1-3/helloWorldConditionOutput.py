# Hello World的条件输出
# 描述
# 获得用户输入的一个整数，参考该整数值，打印输出"Hello World"，要求：
# 如果输入值是0，直接输出"Hello World"
# 如果输入值大于0，以两个字符一行方式输出"Hello World"（空格也是字符）
# 如果输入值小于0，以垂直方式输出"Hello World"

# Get user input
num = int(input())

# Check conditions and print "Hello World" accordingly
if num == 0:
    print("Hello World")
elif num > 0:
    for i in range(0, len("Hello World"), 2):
        print("Hello World"[i:i + 2])
else:
    for char in "Hello World":
        print(char)
