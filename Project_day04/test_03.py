# # 练习1:判断奇偶,询问用户一个整数，判断它是奇数还是偶数
# num = int(input("请输入数字: "))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")
from scipy.cluster.vq import kmeans

# # 练习2:询问年份，判断是否为闰年。能被 4 整除但不能被 100 整除，或者能被 400 整除
# year = int(input("请输入年份: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year}年是闰年")
# else:
#     print(f"{year}年是平年")

# # 练习3:询问分数（0-100），输出等级：90-100：A;80-89：B;70-79：C;60-69：D;0-59：E
# score = int(input("请输入你的分数: "))
# if 90 <= score <= 100:
#     print("A")
# elif 80 <= score < 90:
#     print("B")
# elif 70 <= score < 80:
#     print("C")
# elif 60 <= score < 70:
#     print("D")
# else:
#     print("E")

# # 练习4:询问两个数字和一个运算符（+ - * /），输出结果除法保留两位小数;运算符不合法时输出“不支持的运算符”;除数为 0 时输出“除数不能为 0”
# num1 = float(input("请输入数字1: "))
# num2 = float(input("请输入数字2: "))
# op = input("请输入运算符(+ - * /): ")
#
# if op == "+":
#     result = num1 + num2
#     print(f"{num1} + {num2} = {result}")
# elif op == "-":
#     result = num1 - num2
#     print(f"{num1} - {num2} = {result}")
# elif op == "*":
#     result = num1 * num2
#     print(f"{num1} * {num2} = {result}")
# elif op == "/":
#     if num1 == 0:
#         print("除数不能为0")
#     else:
#         result = num1 / num2
#         print(f"{num1} / {num2} = {result:.2f}")

# # 练习5:询问三条边，判断能否组成三角形；如果能，再判断类型。规则：任意两边之和大于第三边。三边相等：等边三角形;两边相等：等腰三角形;否则：普通三角形
# a = int(input("请输入第一条边: "))
# b = int(input("请输入第二条边: "))
# c = int(input("请输入第三条边: "))
#
# if a + b > c and b + c > a and c + a > b:
#     print("能组成三角形")
#     if a == b == c:
#         print("类型: 等边三角形")
#     elif a == b or b == c or c == a:
#         print("类型: 等腰三角形")
#     else:
#         print("类型: 普通三角形")
# else:
#     print("不能组成三角形")

# # 练习6:计费规则：起步价 13 元，含 3 公里;超过 3 公里，每公里 2.3 元;超过 10 公里，超出部分每公里加收 50% 空驶费（即 3.45 元/公里）
# km = float(input("请输入公里数: "))
#
# if km <= 3:
#     fee = 13
# elif 3 < km <= 10:
#     fee = 13 + (km - 3) * 2.3
# else:
#     fee = 13 + 7 * 2.3 + (km - 10) * 3.45
#
# print(f"费用: {fee:.2f} 元")

# 练习7:程序随机生成 1-100 的整数，让用户猜一次，判断猜大了、猜小了还是猜对了
import random

answer = random.randint(1,100)
num = int(input("请输入你猜的数字(1-100): "))

if num < answer:
    print(f"猜小了,答案是{answer}")
elif num > answer:
    print(f"猜大了,答案是{answer}")
else:
    print("猜对了！")