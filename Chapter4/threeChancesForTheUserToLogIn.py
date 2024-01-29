# 用户登录的三次机会
# 给用户三次输入用户名和密码的机会,要求如下:
# 1)如输入第一行输入用户名为'Kate',第二行输入密码为'666666',输出'登录成功!',退出程序;
# 2)当一共有3次输入用户名或密码不正确输出"3次用户名或者密码均有误!退出程序.".
# 初始化用户名和密码
correct_username = 'Kate'
correct_password = '666666'

# 给用户三次输入机会
for i in range(3):
    # 获取用户输入
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    
    # 检查用户名和密码
    if username == correct_username and password == correct_password:
        print("登录成功!")
        break  # 退出循环
    else:
        # 如果已经是第三次尝试，输出错误信息并退出
        if i == 2:
            print("3次用户名或者密码均有误!退出程序.")
        else:
            # 提示用户还有几次机会
            print(f"用户名或密码错误!你还有{2 - i}次机会。")






