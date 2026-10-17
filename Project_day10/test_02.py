# """
# 练习1: 定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
# 具体规则如下:
# 1.优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 2.积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
# """
#
#
# def calc_order_cost(*args, coupon=0, score=0, express=0.0):
#     """
#     根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
#     :param args: 商品信息（商品名、价格、数量）
#     :param coupon: 优惠券
#     :param score: 积分
#     :param express: 运费
#     :return:
#     """
#     # 1.计算总金额
#     total_price = [goods[1] * goods[2] for goods in args]
#     total_cost = sum(total_price)
#
#     # 2.计算优惠券金额
#     if total_cost >= 5000 and coupon < total_cost:
#         total_cost -= coupon
#
#     # 3.计算积分抵扣金额
#     if total_cost >= 5000 and score // 100 <= total_cost:
#         total_cost -= score // 100
#
#     # 4.添加运费
#     total_cost += express
#
#     return total_cost
#
# # 测试
# total = calc_order_cost(("鼠标", 188, 2),("手机", 6999, 1), ("键盘", 388, 1), coupon=100, score=2000, express=9.9)
# print(total)



# """
# 练习2: 成绩处理流水线
# 给定成绩列表, 完成:
# 1.boost(scores)：每个成绩加 5 分，最高不超过 100
# 2.passed(scores)：只保留 ≥60 的成绩
# 3.average(scores)：计算平均分，保留两位小数
# 4.report(scores)：调用上面三个函数，输出处理前后的结果
# """
# scores = [85, 92, 58, 76, 95, 63, 88, 45, 72, 90]
#
# def boost(scores):
#     return list(map(lambda n: min(n + 5, 100), scores))
#
# def passed(scores):
#     return list(filter(lambda n: n >= 60, scores))
#
# def average(scores):
#     if len(scores) == 0:
#         return 0
#     return sum(scores) / len(scores)
#
# def report(scores):
#     print(f"原始成绩: {len(scores)} 人, 平均分: {average(scores):.2f}")
#
#     boosted = boost(scores)
#     print(f"加分后: {len(boosted)} 人, 平均分: {average(boosted):.2f}")
#
#     passed_scores = passed(scores)
#     print(f"及格人数: {len(passed_scores)} 人")
#     print(f"及格成绩: {passed_scores}")
#     print(f"及格平均分: {average(passed_scores):.2f}")
#
# report(scores)




# """
# 练习3: 灵活的参数
# 写一个函数 create_student(name, *scores, **info)：
#     name：学生姓名（必选）
#     *scores：若干科成绩（可变位置参数）
#     **info：其他信息，如班级、性别（可变关键字参数）
# 要求：
#     1.输出学生姓名
#     2.输出所有成绩和总分
#     3.输出所有附加信息
# """
# def create_student(name, *scores, **info):
#     print(f"姓名: {name}")
#     print(f"成绩: {scores}, 总分: {sum(scores)}")
#
#     info_parts = []
#     for key, value in info.items():
#         info_parts.append(f"{key} = {value}")
#     print(f"附加信息: {', '.join(info_parts)}")
#     print("---")
#
# create_student("张伟", 86, 67, 89, age=20, 班级="高一二班")


# """
# 练习4: 默认参数陷阱
# 阅读下面代码，写出输出并解释原因
# 然后修改这个函数，让它每次调用都返回新列表，不累积之前的结果
# """
# def add_item(item, lst=[]):
#     lst.append(item)
#     return lst
#
# print(add_item("苹果")) # ['苹果']
# print(add_item("香蕉")) # ['苹果', '香蕉']
# print(add_item("橙子")) # ['苹果', '香蕉', '橙子']
#
# def new_add_item(item, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(item)
#     return lst
#
# print(new_add_item("苹果"))
# print(new_add_item("香蕉"))
# print(new_add_item("橙子"))




"""
# 练习5: 排序综合
# 给定学生列表
#     1.按总分降序排序，输出姓名和总分
#     2.按语文成绩升序排序，输出姓名和语文
#     3.按数学成绩降序排序，数学相同则按英语降序，输出姓名、数学、英语
# """

# students = [
#     ("张伟", 85, 92, 78),
#     ("王芳", 92, 88, 95),
#     ("李娜", 78, 88, 82),
#     ("刘洋", 88, 79, 91),
#     ("陈晨", 95, 96, 89),
# ]
# # 1.按总分降序
# print("按总分降序: ")
# sorted_by_total = sorted(students, key=lambda s: sum(s[1:]), reverse=True)
# for s in sorted_by_total:
#     print(f"{s[0]} 总分: {sum(s[1:])}")
#
# # 2.按语文成绩升序
# print("\n按语文升序: ")
# sorted_by_chinese = sorted(students, key=lambda s: s[1])
# for s in sorted_by_chinese:
#     print(f"{s[0]} 语文: {s[1]}")
#
# # 3.按数学成绩降序排序，数学相同则按英语降序
# print("\n按数学成绩降序排序，数学相同则按英语降序: ")
# sorted_by_math_english = sorted(students, key=lambda s: (s[2], s[3]), reverse=True)
# for s in sorted_by_math_english:
#     print(f"{s[0]} 数学：{s[2]} 英语：{s[3]}")



"""
练习6: 综合大练习——班级成绩分析
给定一个班级的成绩字典
写一个函数 analyze(students)，完成：
    1.输出每个学生的总分和平均分
    2.输出总分最高的学生姓名和总分
    3.输出每科的最高分和对应学生姓名
    4.输出平均分 ≥85 的学生名单（用 filter）
    5.输出按平均分降序排列的姓名列表（用 sorted + lambda）
"""
students = {
    "张伟": {"chinese": 85, "math": 92, "english": 78},
    "王芳": {"chinese": 92, "math": 88, "english": 95},
    "李娜": {"chinese": 78, "math": 85, "english": 82},
    "刘洋": {"chinese": 88, "math": 79, "english": 91},
    "陈晨": {"chinese": 95, "math": 96, "english": 89},
    "杨帆": {"chinese": 76, "math": 82, "english": 77},
}

def analyze(students):
    # 1.每个学生的总分和平均分
    print("=" * 50)
    print("1.每个学生的总分和平均分")
    print("=" * 50)
    for name, info in students.items():
        total = info["chinese"] + info["math"] + info["english"]
        average = total / 3
        print(f"{name} 总分: {average}")

    # 2.总分最高
    print("=" * 50)
    print("2.总分最高")
    print("=" * 50)
    highest_name = ""
    highest_total = 0
    for name, info in students.items():
        total = info["chinese"] + info["math"] + info["english"]
        if total > highest_total:
            highest_name = name
            highest_total = total
    print(f"总分最高: {highest_name} {highest_total}")

    # 3.每科的最高分和对应学生
    print("=" * 50)
    print("3.每科的最高分和对应学生")
    print("=" * 50)

    subjects = [
        ("语文", "chinese"),
        ("数学", "math"),
        ("英语", "english")
    ]
    for subject_name, key in subjects:
        highest_score = 0
        highest_student = ""
        for name, info in students.items():
            if info[key] > highest_score:
                highest_score = info[key]
                highest_student = name
        print(f"{subject_name}最高: {highest_score} {highest_student}")

    # 4.平均分 ≥85 的学生
    print("=" * 50)
    print("4.优秀学生(平均分 ≥85 的学生)")
    print("=" * 50)
    names = list(students.keys())
    averages = list(map(lambda name: sum(students[name].values()) / 3, names))
    excellent = list(filter(lambda name: sum(students[name].values()) >= 85, names))
    print(f"优秀学生: {excellent}")

    # 5.按平均分降序
    print("=" * 50)
    print("5.按平均分降序")
    print("=" * 50)
    sorted_names = sorted(students.keys(), key=lambda name: sum(students[name].values()), reverse=True)
    print(f"按平均分排序：: {sorted_names}")

analyze(students)