# # while 循环 : 判断语句结果是bool值
#
# i = 0
# while i < 10:
#     print("Hello Python!")
#     i += 1
# else:
#     print("Goodbye!")


# # 案例: 计算1-100之间的所有偶数之和
# total = 0 #记录累加之和
# i = 1 #循环开始数字
#
# while i <= 100:
#     if i % 2 == 0:
#         total += i
#     i += 1
#
# print(f"Total: {total}")



# # for 循环 : 轮询遍历机制
# msg = input("请输入需要遍历的字符串: ")
#
# for s in msg:
#     print(f"元素: {s}")
# else:
#     print("遍历结束！")

# # while循环: 用于在某个条件满足时一直循环，循环的次数通常是未知的，只知道循环开始/结束的条件。(关注的是循环的条件)
# # for循环: 用于对一个已知的数据集进行遍历或已知次数的循环。(关注的是遍历每一个元素)


# range语句: 生成指定规则的数字序列;
# range(end) -> 从0开始，到end结束(不含end本身)
# range(start,end) -> 从start开始，到end结束的数字序列(不含end本身)
# range(start,end,step) -> 从start开始，到end结束，step步长(不含end本身)


# # 案例: 计算1-100之间的所有奇数之和
# total = 0

# # 原始
# for i in range(1,101):
#     if i % 2 == 1:
#         total += i

# # 简化
# for i in range(1,101,2):
#     total += i
#
# print(f"1-100之间的奇数累加之和: {total}")


# # 案例: 计算100-500之间所有3的倍数的数字之和
# total = 0
#
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
#
# print(f"100-500之间所有3的倍数的数字之和: {total}")


# 嵌套循环
# # 案例: 根据输入的长方形长度 m , 宽度 n , 打印一个长方形
# # # print("*") : 自带换行效果 , 每一次执行都会输出新的一行中
# # # print("*", end="") : end表示的是每一次输出以什么结束; 默认 \n , 表示换行
#
# # 1.接收键盘录入 m , n
# m = int(input("请输入长方形的长: "))
# n = int(input("请输入长方形的宽: "))
#
# # 2.打印长方形
# for j in range(n): # 控制行
#     for i in range(m): # 控制列
#         print("*", end="  ")
#     print() # 控制换行


# # # 案例: 打印99乘法表
# for i in range(1,10): # 外层循环 -> 控制行
#     for j in range(1,i+1): # 内层循环 -> 控制列
#         print(f"{j} x {i} = {j * i}",end="\t")
#     print() # 控制换行


# # 案例:登录模拟 ------> break 与 continue 的使用
# # break : 只能出现在循环中, 表示结束、跳出循环的含义(break跳出循环时, while后面的else中的代码将不会执行)
# # continue : 只能够出现在循环中, 表示中断本次循环, 直接进入下一次循环

# 1.正确的用户名和密码: admin/666888 ; zhangsan/123456 ; sanjin/580231
# 2.输入用户名和密码进行登录, 直到登录成功, 程序结束运行; 如果登录失败, 则继续输入用户名和密码进行登录
# 3.输入的用户名和密码不能为空
# 4.登录成功: 输出“登录成功, 进入首页~”
# 5.登录失败: 输出“用户名或密码错误, 请重新输入！”

while True:
    # 1.接收输入的用户名和密码
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    # 2.校验空值
    if username == "" or password == "":
        print("输入的用户名和密码不能为空!")
        continue

    # 3.校验正确性
    if username == "admin" and password == "666888":
        print("登录成功, 进入首页~")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功, 进入首页~")
        break
    elif username == "sanjin" and password == "580231":
        print("登录成功, 进入首页~")
        break
    else:
        print("用户名或密码错误, 请重新输入！")