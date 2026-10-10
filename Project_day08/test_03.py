# # 练习 1：字典基础操作
# student = {"name": "张三", "age": 20, "major": "计算机科学"}
#
# # 1.输出 name 对应的值
# print(student["name"])
#
# # 2.添加 "score": 85
#
# student["score"] = 85
# print(student)
#
# # 3.把 age 改成 21
# student["age"] = 21
# print(student)
#
# # 4.删除 major
# del student["major"]
# print(student)
#
# # 5.判断 "name" 是否在字典中
# print("name" in student)
#
# # 6.输出所有 key
# print(student.keys())
#
# # 7.输出所有 value
# print(student.values())
#
# # 8.输出字典长度
# print(len(student))
from Project_day07.test_03 import lowest

# # 练习 2：字典遍历
# scores = {"语文": 85, "数学": 92, "英语": 78}
#
# # 1.遍历所有 key，输出科目名
# for subject in scores.keys():
#     print(subject)
#
# # 2.遍历所有 value，输出分数
# for score in scores.values():
#     print(score)
#
# # 3.遍历所有 key-value 对，输出 "科目：分数"
# # 方式一:
# for subject in scores.keys():
#     print(f"{subject}: {scores[subject]}")
#
# # 方式二:
# for item in scores.items():
#     print(f"{item[0]}: {item[1]}")
#
# # 方式三:
# for k,v in scores.items():
#     print(f"{k}: {v}")



# # 练习 3：统计词频
# # 统计每个单词出现的次数，输出结果
# text = "apple banana apple cherry banana apple"
# words = text.split()
#
# counts = {}
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
#
# print(counts)




# # 练习 4：字典嵌套
# # 1.输出每个学生的姓名和总分
# # 2.输出每个学生的平均分（保留两位小数）
# # 3.输出平均分最高的学生姓名
# students = {
#     "S001": {"name": "张伟", "chinese": 85, "math": 92, "english": 78},
#     "S002": {"name": "王芳", "chinese": 92, "math": 88, "english": 95},
#     "S003": {"name": "李娜", "chinese": 78, "math": 85, "english": 82}
# }
#
# for sid,info in students.items():
#     total = info["chinese"] + info["math"] + info["english"]
#     print(f"{info["name"]}: {total}")
#
# for sid,info in students.items():
#     avg = (info["chinese"] + info["math"] + info["english"]) / 3
#     print(f"{info['name']}: {avg:.2f}")
#
# highest_name = ""
# highest_avg = 0
#
# for sid,info in students.items():
#     avg = (info["chinese"] + info["math"] + info["english"]) / 3
#     if avg > highest_avg:
#         highest_avg = avg
#         highest_name = info["name"]
#
# print(f"平均分最高: {highest_name}")



# # 练习 5：集合基础
# # 1.用 set() 把列表转成集合，输出去重结果
# # 2.输出集合长度
# # 3.判断 3 是否在集合中
# # 4.往集合添加 6
# # 5.从集合删除 1
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
#
# numbers = set(numbers)
# print(numbers)
#
# print(len(numbers))
#
# print(3 in numbers)
#
# numbers.add(6)
# print(numbers)
#
# numbers.remove(1)
# print(numbers)



# # 练习 6：集合运算
# # 1.输出交集（两个集合都有的元素）
# # 2.输出并集（两个集合所有元素）
# # 3.输出差集（a 有 b 没有的）
# # 4.输出对称差集（只在其中一个集合中的元素）
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
#
# print(a & b)
# print(a | b)
# print(a - b)
# print(a ^ b)



# # 练习 7：综合应用
# # 1.输出两个班级都有的学生（用集合）
# # 2.输出所有学生（去重，用集合）
# # 3.输出只在 A 班不在 B 班的学生
# # 4.输出两个班级学生总数（去重后）
# class_a = ["张三", "李四", "王五", "赵六"]
# class_b = ["王五", "赵六", "钱七", "孙八"]
#
# set_a = set(class_a)
# set_b = set(class_b)
#
# print(set_a & set_b)
# print(set_a | set_b)
# print(set_a - set_b)
#
# print(f"学生总数: {len(set_a | set_b)}")



# 综合大练习：学生成绩管理系统
# 1.输出: 班级总人数、所有学生的学号列表、所有学生的姓名列表
# 2.输出每个学生的学号、姓名、总分、平均分（保留两位小数）
# 3.输出各科的最低分、最高分、平均分(保留两位小数)、及格人数(>=60)
# 4.按平均分划分等级: 优秀(90及以上)、良好(80-89)、中等(70-79)、及格(60-69)、不及格(60以下)
# 5.给定一个学号，输出该学生的所有信息。如果学号不存在，提示“学号不存在”
# 6.分别找出语文、数学、英语最高分的学生姓名和分数
# 7.输出所有三科都 ≥60 的学生姓名
# 8.任意一科低于 60 分，就需要补考。输出需要补考的学生姓名和不及格的科目
students = {
    "S001": {"name": "张伟", "chinese": 85, "math": 92, "english": 78},
    "S002": {"name": "王芳", "chinese": 92, "math": 88, "english": 95},
    "S003": {"name": "李娜", "chinese": 78, "math": 85, "english": 82},
    "S004": {"name": "刘洋", "chinese": 88, "math": 79, "english": 91},
    "S005": {"name": "陈晨", "chinese": 95, "math": 96, "english": 89},
    "S006": {"name": "杨帆", "chinese": 76, "math": 82, "english": 77},
    "S007": {"name": "赵敏", "chinese": 89, "math": 91, "english": 94},
    "S008": {"name": "周杰", "chinese": 75, "math": 69, "english": 92},
    "S009": {"name": "吴桐", "chinese": 86, "math": 89, "english": 98},
    "S010": {"name": "徐静", "chinese": 66, "math": 59, "english": 72}
}
menu = """
=========== 学生成绩管理系统 ===========
=            1.基本信息统计           =
=            2.个人信息统计           =
=            3.各科成绩统计           =
=            4.成绩等级分布           =
=            5.查找个人信息           =
=            6.单科最高查询           =
=            7.及格学生信息           =
=            8.补考学生信息           =
=            9.退出管理系统
=====================================
"""
print("欢迎 ~")

while True:
    print(menu)
    choice = input("请输入需要进行的操作(1-9): ")

    match choice:
        case "1":
            print(f"班级总人数: {len(students)}")
            print(f"学号列表: {list(students.keys())}")

            names = []
            for sid,info in students.items():
                names.append(info["name"])
            print(f"姓名列表: {names}")
        case "2":
            for sid,info in students.items():
                total = info["chinese"] + info["math"] + info["english"]
                avg = total/3
                print(f"{sid} \t {info["name"]} \t 总分:{total} \t 平均分: {avg:.2f}")
        case "3":
            chinese_scores = []
            math_scores = []
            english_scores = []

            for sid,info in students.items():
                chinese_scores.append(info["chinese"])
                math_scores.append(info["math"])
                english_scores.append(info["english"])

            subjects = [
                ("语文",chinese_scores),
                ("数学",math_scores),
                ("英语",english_scores)
            ]
            for subject_name,scores in subjects:
                lowest = min(scores)
                highest = max(scores)
                avg = sum(scores) / len(scores)

                pass_count = 0
                for s in scores:
                    if s >= 60:
                        pass_count += 1

                print(f"{subject_name} \t 最低:{lowest} \t 最高:{highest} \t 平均:{avg:.2f} \t 及格{pass_count}人")

        case "4":
            grades = {"优秀": 0, "良好": 0, "中等": 0, "及格": 0, "不及格": 0}

            for sid,info in students.items():
                avg = (info["chinese"] + info["math"] + info["english"]) / 3

                if avg > 90:
                    grades["优秀"] += 1
                elif 80 <= avg < 90:
                    grades["良好"] += 1
                elif 70 <= avg < 80:
                    grades["中等"] += 1
                elif 60 <= avg < 70:
                    grades["及格"] += 1
                else:
                    grades["不及格"] += 1

            for level,count in grades.items():
                print(f"{level} \t {count}人")

        case "5":
            search_id = input("请输入学号: ")

            if search_id  in students:
                info = students[search_id]
                name = info["name"]
                total = info["chinese"] + info["math"] + info["english"]
                average = total / 3
                print(
                    f"{search_id} {name}  语文：{info['chinese']}  数学：{info['math']}  英语：{info['english']}  总分：{total}  平均分：{average:.2f}")
            else:
                print("学号不存在, 请重新输入！")

        case "6":
            max_chinese_name = ""
            max_chinese_score = 0
            for sid, info in students.items():
                if info["chinese"] > max_chinese_score:
                    max_chinese_score = info["chinese"]
                    max_chinese_name = info["name"]
            print(f"语文最高 \t {max_chinese_name} \t {max_chinese_score}")

            max_math_name = ""
            max_math_score = 0
            for sid, info in students.items():
                if info["math"] > max_math_score:
                    max_math_score = info["math"]
                    max_math_name = info["name"]
            print(f"数学最高 \t {max_math_name} \t {max_math_score}")

            max_english_name = ""
            max_english_score = 0
            for sid, info in students.items():
                if info["english"] > max_english_score:
                    max_english_score = info["english"]
                    max_english_name = info["name"]
            print(f"英语最高 \t {max_english_name} \t {max_english_score}")

        case "7":
            all_pass = []
            for sid, info in students.items():
                if info["chinese"] >= 60 and info["math"] >= 60 and info["english"] >= 60:
                    all_pass.append(info["name"])

            print(f"三科全部及格 \t {all_pass}")

        case "8":
            print("需要补考的学生：")
            for sid, info in students.items():
                failed_subjects = []

                if info["chinese"] < 60:
                    failed_subjects.append(f"语文（{info['chinese']}）")
                if info["math"] < 60:
                    failed_subjects.append(f"数学（{info['math']}）")
                if info["english"] < 60:
                    failed_subjects.append(f"英语（{info['english']}）")

                if len(failed_subjects) > 0:
                    print(f"{info['name']} \t {'、'.join(failed_subjects)}")
        case "9":
            print("Bye ~")
            break
        case _:
            print("非法输入，请重试！！！")

