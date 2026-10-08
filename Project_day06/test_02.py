# # 练习1：列表基础操作（考察增删改查）
# # 1.在末尾添加 "orange"
# # 2.在索引 1 的位置插入 "grape"
# # 3.删除 "banana"
# # 4.把 "cherry" 改成 "pear"
# # 5.输出最终的列表
# # 6.输出列表长度
# fruits = ["apple", "banana", "cherry"]
#
# fruits.append("orange")
# fruits.insert(1,"grape")
# fruits.remove("banana")
# fruits[2] = "pear"
#
# print(fruits)
# print(len(fruits))

# # 练习2：切片（考察切片语法）
# # 1.取出前 3 个元素
# # 2.取出后 3 个元素
# # 3.取出索引 2 到 6 的元素（含 2 不含 6）
# # 4.取出所有偶数索引位置的元素（0, 2, 4, ...）
# # 5.把列表反转
# # 6.取出索引 1 到 8，步长为 2 的元素
# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# print(nums[:3])
# print(nums[-3:])
# print(nums[2:6:])
# print(nums[::2])
# print(nums[::-1])
# print(nums[1:8:2])


# # 练习3：列表方法（考察常用方法）
# # 1.输出最高分和最低分
# # 2.输出 92 出现的次数
# # 3.输出 78 第一次出现的索引
# # 4.把列表升序排序
# # 5.把列表降序排序
# # 6.反转列表
# # 7.清空列表
# scores = [85, 92, 78, 92, 88, 95, 78]
#
# print("最高分: ",max(scores))
# print("最低分: ",min(scores))
# print(f"92分出现了 {scores.count(92)} 次")
# print(f"78第一次在索引 {scores.index(78)} ")
#
# scores.sort()
# print(scores)
#
# scores.sort(reverse=True)
# print(scores)
#
# scores.reverse()
# print(scores)
#
# scores.clear()
# print(scores)


# # 练习4：列表推导式（考察推导式）
# # 1.生成 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]（1 到 10 的平方）
# # 2.从 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 中取出所有偶数
# # 3.从 ["hello", "world", "python", "code"] 中取出长度大于 4 的字符串
# # 4.把 [1, 2, 3, 4, 5] 变成 ["1", "2", "3", "4", "5"]（转成字符串）
# num_list1 = [i**2 for i in range(1,11)]
# print(num_list1)
#
# num_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list1 = [i for i in num_list2 if i % 2 == 0]
# print(new_list1)
#
# num_list3 = ["hello", "world", "python", "code"]
# new_list2 = [i for i in num_list3 if len(i) > 4]
# print(new_list2)
#
# num_list4 = [1, 2, 3, 4, 5]
# new_list3 = [str(n) for n in num_list4]
# print(new_list3)


# # 练习5：综合应用（考察去重 + 统计）
# # 1.输出去重后的列表（保持原顺序）
# # 2.输出去重后列表的长度
# # 3.输出原列表中有哪些重复数字（只输出重复的，不重复的不输出）
# numbers = [3, 7, 2, 9, 3, 7, 5, 2, 8, 9, 1]
#
# new_list4 = []
# for n in numbers:
#     if n not in new_list4:
#         new_list4.append(n)
#
# print(new_list4)
#
#
# print(len(new_list4))
#
# new_list5 = []
# for n in numbers:
#     if numbers.count(n) > 1 and n not in new_list5:
#         new_list5.append(n)
#
# print(new_list5)


# # 练习6：合并如下三个列表, 并对合并后的列表进行元素的去重, 然后排好序(升序)后输出
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
#
# new_list6 = list1 + list2 + list3
# print("合并后的列表: ", new_list6)
#
# new_list7 = []
# for i in new_list6:
#     if i not in new_list7:
#         new_list7.append(i)
#
# new_list7.sort()
# print(new_list7)


# # 练习7：将如下列表中能被 3 或 5 整除的元素提出来, 并获取这些数字对应的平方, 组成一个新的列表
# list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# result = [i**2 for i in list4 if i % 3 == 0 or i % 5 == 0]
# print(result)



# 练习8：将如下列表中的正数提取出来, 封装为一个新的列表
list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]

result2 = [i for i in list5 if i > 0]
print(result2)