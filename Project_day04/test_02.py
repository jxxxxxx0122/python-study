# # if条件判断 ---> 判断条件的结果一定要是bool值;不要忘记判断条件后的冒号(:);if语句里面的代码块，需要前方4个空格(Tab键)的缩进来描述代码的层级关系
# score = int(input("Your Score: "))
# if score > 680:
#     print("Welcome to Qing Hua !")
#     print("Have a good day! ")


# # 案例: 模拟账号登录,账号:18888888888;密码:666888
# ok_account = "18888888888"
# ok_password = "666888"
#
# account = input("请输入账号: ")
# password = input("请输入密码: ")
#
# if account == ok_account and password == ok_password:
#     print("登录成功 ~")
#     print("进入首页 ~")
#
# if account != ok_account or password != ok_password:
#     print("登录失败 ~")
#     print("账号或密码错误 ~")


# # if...else 优化
# ok_account = "18888888888"
# ok_password = "666888"
#
# account = input("请输入账号: ")
# password = input("请输入密码: ")
#
# if account == ok_account and password == ok_password:
#     print("登录成功 ~")
#     print("进入首页 ~")
# else:
#     print("登录失败 ~")
#     print("账号或密码错误 ~")


# # 案例: 判断输入的年份是闰年还是平年;非整百年份，且能被4整除的年份是闰年;整百年份必须能被400整除才是闰年
# year = int(input("请输入年份"))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year} 年是闰年")
# else:
#     print(f"{year} 年是平年")
#

# elif 多个条件判断 : 判断输入的数字是正数、负数还是0
num = float(input("请输入数字: "))

if num > 0:
    print(f"{num}是正数")
elif num < 0:
    print(f"{num}是负数")
else:
    print(f"{num}是0")