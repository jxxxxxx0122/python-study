# # 综合练习1
# # 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
# # 具体功能如下：
# # 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# # 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# # 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# # 4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# # 5.退出购物车
#
# shopping_cart = {}
#
# menu = """
# =========== 购物车 ===========
# =        1.添加购物车         =
# =        2.修改购物车         =
# =        3.删除购物车         =
# =        4.查询购物车         =
# =        5.退出购物车         =
# =============================
# """
# print("欢迎使用 ~~~")
#
# while True:
#
#     print(menu)
#
#     choice = input("请输入需要进行的操作(1-5): ")
#
#     match choice:
#         case "1":
#             goods_name = input("请输入商品名称: ")
#
#             if  goods_name in shopping_cart:
#                 print("商品已存在，请重新输入 ！")
#                 continue
#
#             goods_price = float(input("请输入价格: "))
#             goods_num = int(input("请输入数量: "))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品添加完毕 ~")
#         case "2":
#             goods_name = input("请输入要修改的商品名称: ")
#             if goods_name not in shopping_cart:
#                 print("商品不存在, 请重新输入！！！")
#                 continue
#
#             goods_price = float(input("请输入新的价格: "))
#             goods_num = int(input("请输入新的数量: "))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品修改完毕 ~~~")
#         case "3":
#             goods_name = input("请输入要删除的商品名称: ")
#             if goods_name not in shopping_cart:
#                 print("商品不存在, 请重新输入！！！")
#             else:
#                 del shopping_cart[goods_name]
#             print("商品已删除 ~~~")
#         case "4":
#             for name,info in shopping_cart.items():
#                 print(f"商品名称: {name}, 商品价格: {info['price']}, 商品数量: {info['num']}")
#         case "5":
#             print("Bye ~~~")
#             break
#         case _:
#             print("非法输入，请重新选择！！！")

# # 综合练习2
# # 学生成绩管理系统
# # 1.输出: 班级总人数、所有学生的学号列表、所有学生的姓名列表
# # 2.输出每个学生的学号、姓名、总分、平均分（保留两位小数）
# # 3.输出各科的最低分、最高分、平均分(保留两位小数)、及格人数(>=60)
# # 4.按平均分划分等级: 优秀(90及以上)、良好(80-89)、中等(70-79)、及格(60-69)、不及格(60以下)
# # 5.给定一个学号，输出该学生的所有信息。如果学号不存在，提示“学号不存在”
# # 6.分别找出语文、数学、英语最高分的学生姓名和分数
# # 7.输出所有三科都 ≥60 的学生姓名
# # 8.任意一科低于 60 分，就需要补考。输出需要补考的学生姓名和不及格的科目
# students = {
#     "S001": {"name": "张伟", "chinese": 85, "math": 92, "english": 78},
#     "S002": {"name": "王芳", "chinese": 92, "math": 88, "english": 95},
#     "S003": {"name": "李娜", "chinese": 78, "math": 85, "english": 82},
#     "S004": {"name": "刘洋", "chinese": 88, "math": 79, "english": 91},
#     "S005": {"name": "陈晨", "chinese": 95, "math": 96, "english": 89},
#     "S006": {"name": "杨帆", "chinese": 76, "math": 82, "english": 77},
#     "S007": {"name": "赵敏", "chinese": 89, "math": 91, "english": 94},
#     "S008": {"name": "周杰", "chinese": 75, "math": 69, "english": 92},
#     "S009": {"name": "吴桐", "chinese": 86, "math": 89, "english": 98},
#     "S010": {"name": "徐静", "chinese": 66, "math": 59, "english": 72}
# }
#
# menu = """
# ================ 成绩管理系统 ===============
# =               1.基本信息统计              =
# =               2.个人信息统计              =
# =               3.单科信息查询              =
# =               4.成绩等级分布              =
# =               5.查询个人信息              =
# =               6.单科最高查询              =
# =               7.及格学生信息              =
# =               8.补考名单查询              =
# =               9.退出管理系统              =
# ==========================================
# """
# print("欢迎使用学生成绩管理系统 ~~~")
#
# while True:
#     print(menu)
#
#     choice = input("请输入要执行的操作(1-9): ")
#
#     match choice:
#         case "1":
#             print(f"班级总人数: {len(students)}")
#             print(f"学号列表: {list(students.keys())}")
#
#             names = []
#
#             for sid, info in students.items():
#                 names.append(info["name"])
#             print(f"姓名列表: {names}")
#
#         case "2":
#             for sid,info in students.items():
#                 total = info["chinese"] + info["math"] + info["english"]
#                 avg = total / 3
#                 print(f"学号:{sid}, 姓名:{info["name"]}, 总分:{total}, 平均分:{avg:.2f}")
#
#         case "3":
#             chinese_scores = []
#             math_scores = []
#             english_scores = []
#
#             for sid, info in students.items():
#                 chinese_scores.append(info["chinese"])
#                 math_scores.append(info["math"])
#                 english_scores.append(info["english"])
#
#             subjects = [
#                 ("语文",chinese_scores),
#                 ("数学",math_scores),
#                 ("英语",english_scores)
#             ]
#
#             for subject_name,scores in subjects:
#                 lowest = min(scores)
#                 highest = max(scores)
#                 avg = sum(scores)/len(scores)
#
#                 pass_count = 0
#                 for s in scores:
#                     if s >= 60:
#                         pass_count += 1
#
#                 print(f"{subject_name}, 最高分:{highest}, 最低分:{lowest}, 平均分:{avg:.2f}, 及格人数:{pass_count}")
#
#         case "4":
#             grades = {"优秀": 0, "良好": 0, "中等": 0, "及格": 0, "不及格": 0}
#
#             for sid, info in students.items():
#                 avg = (info["chinese"] + info["math"] + info["english"]) / 3
#
#                 if avg > 90:
#                     grades["优秀"] += 1
#                 elif 80 <= avg < 90:
#                     grades["良好"] += 1
#                 elif 70 <= avg < 80:
#                     grades["中等"] += 1
#                 elif 60 <= avg < 70:
#                     grades["及格"] += 1
#                 else:
#                     grades["不及格"] += 1
#
#             for level, count in grades.items():
#                 print(f"{level} \t {count}人")
#         case "5":
#             search_id = input("请输入学号: ")
#
#             if search_id in students:
#                 info = students[search_id]
#                 name = info["name"]
#                 total = info["chinese"] + info["math"] + info["english"]
#                 average = total / 3
#                 print(
#                     f"{search_id} {name}  语文：{info['chinese']}  数学：{info['math']}  英语：{info['english']}  总分：{total}  平均分：{average:.2f}")
#             else:
#                 print("学号不存在, 请重新输入！")
#
#         case "6":
#             max_chinese_name = ""
#             max_chinese_score = 0
#             for sid, info in students.items():
#                 if info["chinese"] > max_chinese_score:
#                     max_chinese_score = info["chinese"]
#                     max_chinese_name = info["name"]
#             print(f"语文最高 \t {max_chinese_name} \t {max_chinese_score}")
#
#             max_math_name = ""
#             max_math_score = 0
#             for sid, info in students.items():
#                 if info["math"] > max_math_score:
#                     max_math_score = info["math"]
#                     max_math_name = info["name"]
#             print(f"数学最高 \t {max_math_name} \t {max_math_score}")
#
#             max_english_name = ""
#             max_english_score = 0
#             for sid, info in students.items():
#                 if info["english"] > max_english_score:
#                     max_english_score = info["english"]
#                     max_english_name = info["name"]
#             print(f"英语最高 \t {max_english_name} \t {max_english_score}")
#
#         case "7":
#             all_pass = []
#             for sid, info in students.items():
#                 if info["chinese"] >= 60 and info["math"] >= 60 and info["english"] >= 60:
#                     all_pass.append(info["name"])
#
#             print(f"三科全部及格 \t {all_pass}")
#
#         case "8":
#             print("需要补考的学生：")
#             for sid, info in students.items():
#                 failed_subjects = []
#
#                 if info["chinese"] < 60:
#                     failed_subjects.append(f"语文（{info['chinese']}）")
#                 if info["math"] < 60:
#                     failed_subjects.append(f"数学（{info['math']}）")
#                 if info["english"] < 60:
#                     failed_subjects.append(f"英语（{info['english']}）")
#
#                 if len(failed_subjects) > 0:
#                     print(f"{info['name']} \t {'、'.join(failed_subjects)}")
#         case "9":
#             print("Bye Bye ~~~~")
#             break
#         case _:
#             print("非法输入, 请重新输入 ！！！")



# 综合练习3
# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下:
# 1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中
# 2.修改学生信息:要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息
# 3.删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息
# 4.查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出
# 5.列出所有学生:遍历所有学生信息并输出
# 6.统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名
# 7.退出系统

students = {}

menu = """
# # # # # # # #【菜单】# # # # # # # 
#           1.添加学生信息           #
#           2.修改学生信息           #
#           3.删除学生信息           #
#           4.查询学生信息           #
#           5.列出所有学生           #
#           6.统计班级成绩           #
#           7. 退出系统             #
# # # # # # # # # # # # # # # # # # 
"""

print("欢迎使用 ~~~")

while True:
    print(menu)

    choice = input("请输入要执行的操作(1-7): ")

    match choice:
        case "1":
            students_name = (input("请输入学生姓名: "))
            if students_name in students:
                print("学生已存在, 请重新输入！！！")
                continue

            chinese_scores = int(input("请输入语文成绩: "))
            math_scores = int(input("请输入数学成绩: "))
            english_scores = int(input("请输入英语成绩:"))

            students[students_name] = {"chinese": chinese_scores, "math": math_scores, "english": english_scores}
            print(f"添加【{students_name}】成功")
        case "2":
            students_name = input("请输入要修改成绩的学生姓名: ")
            if students_name not in students:
                print("学生不存在, 请重新输入！！！")
                continue

            chinese_scores = int(input("请输入新的语文成绩: "))
            math_scores = int(input("请输入新的数学成绩: "))
            english_scores = int(input("请输入新的英语成绩: "))
            students[students_name] = {"chinese": chinese_scores, "math": math_scores, "english": english_scores}
            print(f"学生【{students_name}】成绩修改完毕 ~~~")

        case "3":
            students_name = input("请输入要删除的学生姓名: ")
            if students_name not in students:
                print("学生不存在, 请重新输入 ！！！")
            else:
                del students[students_name]
                print(f"学生【{students_name}】已删除 ~")
        case "4":
            students_name = input("请输入要查询的学生姓名: ")
            if students_name in students:
                student_info = students[students_name]
                print(f"姓名【{students_name}】, 语文:{student_info["chinese"]}, 数学:{student_info["math"]}, 英语:{student_info["english"]}")
            else:
                print("学生不存在, 请重新输入！！！")
        case "5":
            for name,score in students.items():
                print(f"姓名:【{name}】, 语文:{score["chinese"]}, 数学:{score["math"]}, 英语:{score["english"]}")
        case "6":
            if len(students) == 0:
                print("当前没有学生信息, 无法统计！！！")
            else:
                chinese_score = []
                math_score = []
                english_score = []
                names = list(students.keys())

                for name, info in students.items():
                    chinese_score.append(info["chinese"])
                    math_score.append(info["math"])
                    english_score.append(info["english"])

                subjects = [
                    ("语文", chinese_score),
                    ("数学", math_score),
                    ("英语", english_score)
                ]

                for subject_name, scores in subjects:
                    highest = max(scores)
                    lowest = min(scores)
                    avg = sum(scores)/len(scores)

                    highest_index = scores.index(highest)
                    lowest_index = scores.index(lowest)
                    highest_name = names[highest_index]
                    lowest_name = names[lowest_index]

                    print(f"{subject_name}: \n 最高分:{highest}【{highest_name}】 \n 最低分:{lowest}【{lowest_name}】 \n 平均分:{avg:.2f}")

        case "7":
            print("Bye ~")
            break
        case _:
            print("非法输入, 请重试 ！！！")