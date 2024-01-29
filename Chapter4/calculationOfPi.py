# 实例6:圆周率的计算
# 这是"实例"题,与课上讲解实例相同,请作答检验学习效果.
# 求解圆周率可以采用蒙特卡罗方法,在一个正方形中撒点,根据在1/4圆内点的数量占总撒点数的比例计算圆周率值.
# 请以123作为随机数种子,获得用户输入的撒点数量,编写程序输出圆周率的值,保留小数点后6位.
import random
import random
random.seed(123)

def calculate_pi(num_points):
    points_inside_circle = 0
    total_points = num_points

    for _ in range(total_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

    pi = 4 * (points_inside_circle / total_points)
    return round(pi, 6)

num_points = int(input())
pi_value = calculate_pi(num_points)
print("{:.6f}".format(pi_value))