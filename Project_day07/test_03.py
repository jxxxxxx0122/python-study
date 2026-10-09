# # 练习1： 字符串基础操作
# # 1.输出字符串长度
# # 2.输出全部大写
# # 3.输出全部小写
# # 4.输出 "Python" 在字符串中的起始索引
# # 5.把 "World" 替换成 "China"
# # 6.判断字符串是否以 "Hello" 开头
# # 7.去掉字符串两端的空格（先手动在两端加空格再测）
# s = "Hello, Python World"
#
# print(len(s))
# print(s.upper())
# print(s.lower())
# print(s.find("Python"))
# print(s.replace("World", "China"))
# print(s.startswith("Hello"))
#
# s2 = (" Hello ")
# print(s2.strip())


# # 练习 2：字符串切片与反转
# # 1.取出前 3 个字符
# # 2.取出后 3 个字符
# # 3.取出索引 2 到 6 的字符（含 2 不含 6）
# # 4.取出所有偶数索引位置的字符
# # 5.把字符串反转
# # 6.取出索引 1 到 8，步长为 2 的字符
# s = "abcdefghij"
#
# print(s[:3])
# print(s[-3:])
# print(s[2:6:])
# print(s[::2])
# print(s[::-1])
# print(s[1:8:2])


# # 练习 3：回文判断
# # 询问用户一个字符串，判断它是不是回文（正着读和倒着读一样）
# s = input("请输入文本: ")
#
# if s[::-1] == s:
#     print(f"{s} 是回文")
# else:
#     print(f"{s} 不是回文")



# # 练习 4：统计字符
# # 询问用户一个字符串，统计其中：大写字母个数、小写字母个数、数字个数、其他字符个数
# s = input("请输入文本: ")
#
# upper_count = 0
# lower_count = 0
# digit_count = 0
# other_count = 0
#
# for c in s:
#     if c.isupper():
#         upper_count += 1
#     elif c.islower():
#         lower_count += 1
#     elif c.isdigit():
#         digit_count += 1
#     else:
#         other_count += 1
#
# print(f"大写字母: {upper_count}")
# print(f"小写字母: {lower_count}")
# print(f"数字: {digit_count}")
# print(f"其他: {other_count}")



# # 练习 5：单词反转
# # 询问用户一句英文，把每个单词反转，但单词顺序不变
# s = input("请输入一句英文: ")
#
# words = s.split()
# reversed_words = [w[::-1] for w in words]
# result = " ".join(reversed_words)
#
# print(result)


# # 练习 6：元组基础
# # 1.输出元组长度
# # 2.输出第一个和最后一个元素
# # 3.输出索引 1 到 3 的元素（切片）
# # 4.判断 30 是否在元组中
# # 5.输出元组中最大值和最小值
# # 6.尝试修改第一个元素为 100，观察报错
# t = (10, 20, 30, 40, 50)
#
# print(len(t))
# print(t[0],t[-1])
# print(t[1:4:])
# print(30 in t)
# print(max(t))
# print(min(t))
# t[0] = 100


# # 练习 7：元组解包
# # 1.用解包把姓名、年龄、专业、成绩分别赋给变量
# # 2.输出格式化的信息
# # 3.计算该学生成绩是否及格（≥60）
# student = ("张三", 20, "计算机科学", 85.5)
#
# name,age,major,score = student
#
# print(f"姓名: {name}, 年龄: {age}, 专业: {major}, 成绩: {score}")
#
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")


# # 练习 8：综合应用
# # 1.把每个单词和它的长度组成元组，放入新列表
# # 2.输出长度大于 5 的单词
# # 3.用普通 for 循环找出最长的单词（
# words = ["apple", "banana", "cherry", "date", "elderberry"]
#
# word_tuples = [(w,len(w)) for w in words]
# print(word_tuples)
#
# long_words = [w for w in words if len(w) > 5]
# print(f"长度大于 5: {long_words}")
#
# longest_word = word_tuples[0][0]
# longest_length = word_tuples[0][1]
#
# for w, length in word_tuples:
#     if length > longest_length:
#         longest_word = w
#         longest_length = length
#
# print(f"最长单词: {longest_word}")



# 练习 9：根据所给成绩单, 完成：
# 1.计算每个学生的总分、各科平均分、然后一并输出出来
# 2.统计各科成绩的最低分、最高分、平均分, 并输出
# 3.查找成绩优秀(平均分大于90)的学生, 并输出
# 语数英
students = (
    ("S001", "张伟", 85, 92, 78),
    ("S002", "王芳", 92, 88, 95),
    ("S003", "李娜", 78, 85, 82),
    ("S004", "刘洋", 88, 79, 91),
    ("S005", "陈晨", 95, 96, 89),
    ("S006", "杨帆", 76, 82, 77),
    ("S007", "赵敏", 89, 91, 94),
    ("S008", "周杰", 75, 69, 92),
    ("S009", "吴桐", 86, 89, 98),
    ("S010", "徐静", 66, 59, 72)
)

print("=" * 60)
print("1. 每个学生的总分和平均分")
print("=" * 60)

for student in students:
    sid, name, chinese, math, english = student
    total = chinese + math + english
    avg = total / 3
    print(f"{sid} \t {name} \t 总分: {total} \t 平均分: {avg:.2f}")

print("\n" + "=" * 60)
print("2.各科成绩统计")
print("=" * 60)

chinese_scores = []
math_scores = []
english_scores = []

for student in students:
    chinese_scores.append(student[2])
    math_scores.append(student[3])
    english_scores.append(student[4])

subjects = [
    ("语文", chinese_scores),
    ("数学", math_scores),
    ("英语", english_scores),
]

for subject_name, scores in subjects:
    lowest = min(scores)
    highest = max(scores)
    avg = sum(scores) / len(scores)
    print(f"{subject_name}: \t 最低:{lowest} \t 最高:{highest} \t 平均分:{avg:.2f}")

print("\n" + "=" * 60)
print("3.平均分大于 90 的学生")
print("=" * 60)

for student in students:
    sid, name, chinese, math, english = student
    avg = (chinese + math + english) / 3
    if avg > 90:
        print(f"{sid} \t {name} \t 平均分: {avg:.2f}")