# # 练习1: 用循环计算 1 + 2 + 3 + ... + 100，输出结果
# total = 0
# for i in range(1,101):
#     total += i
#
# print(f"1 + 2 + 3 + ... + 100 = {total}")

# # 练习2: 用嵌套 for 循环打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} x {i} = {j * i}",end="\t")
#     print()

# # 练习3: 程序随机生成 1-100 的整数，让用户反复猜，直到猜对。
# # 猜大了提示“猜大了”
# # 猜小了提示“猜小了”
# # 猜对了提示“猜对了，你用了 X 次”
# import random
#
# answer = random.randint(1,100)
# count = 0
#
# while True:
#     guess = int(input("请输入你猜的数字: "))
#     count += 1
#
#     if guess > answer:
#         print("猜大了")
#     elif guess < answer:
#         print("猜小了")
#     else:
#         print(f"猜对了, 你用了{count}次")
#         break

# # 练习4: 打印 1 到 20 之间的所有偶数，用 continue 跳过奇数
# for num in range(1, 21):
#     if num % 2 == 0:
#         print(num)
#     else:
#         continue

# # 练习5: 询问用户一个大于 1 的整数，判断它是不是素数。
# # 素数：只能被 1 和自身整除的数
# n = int(input("请输入一个整数: "))
#
# if n <= 1:
#     print(f"{n}不是素数")
# else:
#     is_prime = True
#     for i in range(2,int(n ** 0.5)+1):
#         if n % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print(f"{n} 是素数")
#     else:
#         print(f"{n} 不是素数")


# # 练习6: 询问用户行数，打印对应层数的星号金字塔
# # # 嵌套写法
# rows = int(input("请输入行数: "))
#
# for i in range(1,rows + 1):
#     for j in range(rows - i):
#         print(" ",end="")
#     for k in range(2 * i - 1):
#         print("*",end="")
#     print()

# # # 字符串乘法
# rows = int(input("请输入行数: "))
#
# for i in range(1, rows + 1):
#     spaces = " " * (rows - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)

# 练习7: 用户名密码登录, 正确的用户名和密码为admin/666888、zhangsan/123456、sanjin/580231, 5次登录机会，输入错五次，不允许再操作了
users = {
    "admin": "666888",
    "zhangsan": "123456",
    "sanjin": "580231"
}

max_count = 5
counts = 0

while counts < max_count:
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    if username in users and password == users[username]:
        print(f"欢迎, {username}!")
        break
    else:
        counts += 1
        remaining = max_count - counts
        if remaining > 0:
            print(f"用户名或密码错误, 还剩{remaining}次机会！")
        else:
            print("错误次数已达 5 次, 不允许操作")