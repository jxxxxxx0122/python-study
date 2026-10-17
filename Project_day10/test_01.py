# # 注意: 函数定义的时候并不会执行, 只有在调用函数的时候, 函数体的逻辑才会运行; 函数必须先定义, 后调用; 函数中通过缩进来描述归属关系
# # 函数定义
# from Project_day07.test_03 import math
#
#
# def out_line():
#     print("-----------------------------------------------")
#     print("-----------------------------------------------")
#
# # 函数调用
# out_line()



# # 函数的参数与返回值
# # 函数1: 计算圆的面积 -- 半径
# def circle_area(radius):
#     area = 3.14 * (radius ** 2)
#     return area
#
# area = circle_area(10)
# print(area)


# # 函数2: 长方形的面积
# def rectangle_area(l,w):
#     """
#     根据长方形的长度和宽度, 计算长方形的面积
#     :param l: 长度
#     :param w: 宽度
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
#
# print(rectangle_area(10,5))
#
# help(rectangle_area)

# # 函数3: 计算圆的面积, 周长 -- 半径 ------> 如果返回值有多个, 多个返回值之间逗号分隔 -----> 多个返回值会封装到元组之中
# def circle_area_len(r):
#     """
#     根据圆的半径, 计算圆的面积和周长
#     :param r: 半径
#     :return: 圆的面积, 圆的周长
#     """
#     return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)
#
# al = circle_area_len(10)
# print(al)
# print(type(al))

# area, len = circle_area_len(10) # 解包
# print(area)
# print(len)


# # 函数的嵌套调用
# def function_a():
#     print("a ... before")
#     function_b()
#     print("a ... after")
#
# def function_b():
#     print("b ... before")
#     function_c()
#     print("b ... after")
#
# def function_c():
#     print("c ... ")
#
# function_a()
#
# print("调用完毕！")


# # ------------------------------- 案例 ------------------------------
# # 1.定义一个函数: 根据传入的底和高计算三角形面积
# def triangle_area(b,h):
#     """
#     根据传入的底和高计算三角形面积
#     :param b: 底长
#     :param h: 高
#     :return: 三角形面积
#     """
#     area = (b*h)/2
#     return area
#
# area = triangle_area(3,4)
# print(area)
#
# # 2.定义一个函数: 计算传入的字符串中元音字母的个数(aeiouAEIOU)
# def str_aeiou(s):
#
#     num = 0
#     for w in s:
#         if w in 'aeiouAEIOU':
#             num += 1
#
#     return num
#
# print(str_aeiou("Hello world ok"))
#
# # 3.定义一个函数: 计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)并返回
# def calc_score(score_list):
#     highest_score = max(score_list)
#     lowest_score = min(score_list)
#     avg_score = sum(score_list) / len(score_list)
#
#     return highest_score, lowest_score, avg_score
#
# s_list = [345, 657, 578, 333, 675, 566]
# max_score, min_score, avg_score = calc_score(s_list)
# print(f"最高分{max_score}, 最低分{min_score}, 平均分{avg_score:.2f}")


# # ----------------------- 函数 - 变量的作用域 ----------------------------
# # ======== 注意: 尽量避免在函数中使用全局变量, 因为会使代码难以维护和调试
# # 全局变量  ----------->  在函数外部 或 函数的内部都是可以访问的
# num = 100
#
# # 定义函数
# def circle_area(r):
#     # 局部变量  ------>  只能在函数内部使用
#     pi = 3.14
#     area = pi * r * r
#
#     global num # ------->global关键字: 声明使用全局变量, 并且可修改全局变量的值
#     num = 10000
#     print("num = ",num)
#
#     return area
#
# # 调用函数
# c_area = circle_area(10)
# print(c_area)
#
# print("num = ",num)
#
#
# # -------------------------- 函数 - 传参方式 --------------------------
# # 定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name":name, "age":age, "gender":gender, "city":city}
#
# # 传参方式一: 位置参数
# stu = reg_stu("张三", 18, "男", "北京")
# print(stu)
#
# # 传参方式二: 关键字参数
# stu = reg_stu(name="王五", age=20, gender="男", city="北京")
# print(stu)
#
# stu = reg_stu(age=28, name="李静", city="上海", gender="女")
# print(stu)
#
# # 传参方式三: 位置参数 + 关键字参数 ---> 位置参数在前, 关键字参数在后
# stu = reg_stu("徐雅", 26, city="西安", gender="女")
# print(stu)


# # -------------------------- 函数 - 默认参数 -----------------------------
# # 定义函数
# def reg_stu(name, age, gender="男", city="北京"):
#     print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 调用函数
# stu = reg_stu("李默", 20)
# print(stu)
#
# stu = reg_stu("孙飞", 28, "女")
# print(stu)
#
# stu = reg_stu("马飞", 22, city="上海")
# print(stu)



# # -------------------------- 函数 - 不定长参数(位置参数 *args --> 元组) ----------------------------
# # 需求: 根据传入的数据, 计算这批数据的最小值、最大值、平均值
#
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, round(avg_data,1)
#
# # 调用函数
# print(calc_data(2, 5, 7, 10, 45))
#
# print(calc_data(2, 5, 7, 10, 45, 67, 87, 13, 456))

# # -------------------------- 函数 - 不定长参数(关键字参数 **kwargs --> 字典) --------------------------
# def calc_data(*args, **kwargs):
#     """
#     根据传入的数据, 计算这批数据的最小值、最大值、平均值
#     :param args: 不定长位置参数
#     :param kwargs: 不定长关键字参数
#         round: 保留的小数位个数
#         print: 是否打印输出
#     :return: 最小值、最大值、平均值
#     """
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#
#     if kwargs.get("round") is not None:
#         avg_data = round(avg_data, kwargs.get("round"))
#
#     if kwargs.get("print"):
#         print(f"计算出来的最小值: {min_data}, 最大值: {max_data}, 平均值: {avg_data}")
#
#     return min_data, max_data, avg_data
#
# # 调用函数
# print(calc_data(2, 5, 7, 10, 45, round=3, print=False))
#
# print(calc_data(2, 5, 7, 10, 45, 67, 87, 13, 456, round=4, print=True))



# # --------------------------- 函数 - 参数类型 ------------------------
# # 加
# def add (x, y):
#     return x + y
#
# # 减
# def sub (x, y):
#     return x - y
#
# # 乘
# def mul (x, y):
#     return x * y
#
# # 除
# def div (x, y):
#     return x / y
#
# # 计算
# def calc(x, y, oper):
#     return oper(x, y)
#
# print(calc(10, 20, add))



# # -------------------------- 函数 - 匿名函数 ----------------------------
# # 1.打印一个分隔线
# # def out_line():
# #     print("-------------------------------------")
#
# out_line = lambda : print("-------------------------------------------")
# out_line()
#
# # 2.计算两数之和
# # def add(x, y):
# #     return x + y
#
# add = lambda x, y : x + y
#
# # 按照每一个元素的字符个数, 从小到大排序
# data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
# print(data_list)
#
# data_list.sort(key=lambda item : len(item))
# print(data_list)


# ------------------------------------- 案例 -------------------------------------------
# # 案例1: 计算n的阶乘
# # 递归调用(先层层递进, 再逐层回归): 指的是在函数中自己调用自己的情况  --------> 一定得有终结点
# """
# jc(10) = 10 * jc(9)
# jc(9) = 9 * jc(8)
# jc(8) = 8 * jc(7)
# jc(7) = 7 * jc(6)
# jc(6) = 6 * jc(5)
# jc(5) = 5 * jc(4)
# jc(4) = 4 * jc(3)
# jc(3) = 3 * jc(2)
# jc(2) = 2 * jc(1)
# jc(1) = 1
# """
#
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jc(n - 1)
#
# result = jc(10)
# print(result)
