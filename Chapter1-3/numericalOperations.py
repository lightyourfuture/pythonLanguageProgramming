# 数值运算
# 描述
# 获得用户输入的一个字符串，格式如下：
# M OP N
# 其中，M和N是任何数字，OP代表一种操作，表示为如下四种：+, -, *, /（加减乘除）
# 根据OP，输出M OP N的运算结果，统一保存小数点后2位。
# 注意：M和OP、OP和N之间可以存在多个空格，不考虑输入错误情况。

# Get user input
input_str = input()

# Replace all "/", "*", and "-" with " / ", " * ", and " - " respectively
input_str = input_str.replace("/", " / ").replace("*", " * ").replace("-", " - ")

# Split the input string into components
components = input_str.split()

# Check if the first component is a negative number
if components[0] == '-':
    components[0] += components[1]
    components.pop(1)

# Check if the third component is a negative number
if len(components) > 2 and components[2] == '-':
    components[2] += components[3]
    components.pop(3)

M, OP, N = components

# Convert M and N to floats
try:
    M = float(int(M, 0))  # 0 as base means to interpret the base from the string as 10, 16 or 8
except ValueError:
    M = float(M)

try:
    N = float(int(N, 0))  # 0 as base means to interpret the base from the string as 10, 16 or 8
except ValueError:
    N = float(N)

# Perform the operation and print the result
if OP == '+':
    result = M + N
elif OP == '-':
    result = M - N
elif OP == '*':
    result = M * N
elif OP == '/':
    result = 1.0 * M / N

# Print the result, rounded to 2 decimal places
print(f"{result:.2f}")
