import time

scale = 50

print("执行开始".center(scale // 2, "-"))
start = time.perf_counter()

for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)

print("\n" + "执行结束".center(scale // 2, '-'))

# 文本进度条的不同设计函数
# 设计名称  趋势    设计函数
# Linear    Constant    f(x) = x
# Early Pause   Speeds up   f(x) = x + (1 - sin(x ** 2 + T / 2)) / -8
# Late Pause    Slows down  f(x) = x + (1 - sin(x ** 2 + T // 2)) / 8
# Slow Wavy5684 Constant    f(x) = x + sin(x ** 5) / 20
# Fast Wavy Constant    f(x) = x + sin(x ** 20) / 80
# Power Speeds up   f(x) = (x + (1 - x) * 0.03) ** 2
# Inverse Power Slows down  f(x) = 1 + (1 - x) ** 15 * -1
# Fast Power    Speeds up   f(x) = (x + (1 - x) / 2) ** 8
# InverseFast   Power Slows down f(x) = 1 + (1 - x) ** 3 * -1
