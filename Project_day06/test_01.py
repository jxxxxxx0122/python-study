# # # # 列表基本操作
# # 语法上可以存储不同类型的元素、可重复、有序、元素可修改
# # 定义
# s = [56, 45, 78, 34, 67, 88, "A", "Hello", True]
#
# print(type(s))
#
# # 访问列表元素
# # 获取
# print(s[3]) # 正向索引，从0开始
# print([-3]) # 反向索引，从最后一个元素向前，从-1开始
#
# # 修改
# s[5] = "ABC"
# print(s)
#
# # 注意: 如果指定的索引超出范围, 将会报错 list assignment index out of range
#
# # 删除
# del s[4]
# print(s)
#
# # 遍历
# for item in s:
#     print(item)


# # # # -----------------------------> 切片
# # 序列数据[开始索引:结束索引:步长]
# s = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# print(s[0:5:1])
# print(type(s[0:5:1]))
#
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[0:5:2])
# print(s[0:-2:1])
#
# print(s[::-1])
# print(s[::-2])


# # # # 列表的常见方法
# s = [23, 112, 33, 42, 78, 456, 33, 78, 53, 235]
# print(s)
#
# # # append(): 尾插元素
# s.append(188)
# print(s)
#
# # # insert(): 在指定索引之前插入元素
# s.insert(2,80)
# print(s)
#
# # # remove(): 移除列表中第一个匹配到的元素
# s.remove(33)
# print(s)
#
# # # pop():删除列表中指定索引位置的元素并返回(如果未指定, 默认删除最后一个)
# e = s.pop(1)
# print(e)
#
# e = s.pop()
# print(e)
#
# print(s)
#
# # # sort():排序
# s.sort()
# print(s)
#
# # # reverse:反转列表元素
# s.reverse()
# print(s)

# ------------------案例-------------------
# # 案例1: 将用户输入的10个数字, 存储到一个列表中, 并将列表中的数字进行排序, 输出其中的最小值、最大值和平均值
# num_list = []
#
# for i in range(10):
#     num = int(input("请输入数字: "))
#     num_list.append(num)
#
# print("数字列表: ",num_list)
#
# num_list.sort()
# print("排序后的数字列表: ",num_list)
#
# print("最小值: ",num_list[0])
# print("最大值: ",num_list[-1])
# print("平均值: ",sum(num_list)/len(num_list)) # sum() ---> 求和函数;  len() ---> 获取元素个数
# # min() ---> 获取最小值     max() ---> 获取最大值


# # 案例2: 合并两个列表中的元素, 并对合并的结果进行去重处理(去除列表中的重复元素)
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1.合并列表
# # # (1) for循环便利
# # for num in num_list2:
# #     num_list1.append(num)
#
# # # (2) 解包(将列表这一类容器解开成一个一个独立的元素);组包(将多个值合并到一个容器)
# # num_list = [*num_list1, *num_list2]
#
# # # (3) 直接 +
# num_list = num_list1 + num_list2
#
# print("合并后的原始列表: ",num_list)
#
# # 2.去重
# new_list = []
#
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
#
# print("去重后的列表: ",new_list)



# # 案例3:生成1-20的平方列表 ---> range(1,21)
# # 方式一: 传统方式
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
#
# print(num_list)
#
# # 方式二: 列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式1: [要插入的值/表达式 for i in 序列/列表]
# num_list = [i**2 for i in range(1,21)]
# print(num_list)


# 案例4:从一个数字列表中提取所有偶数, 并计算其平方, 组成一个新的列表
# 列表推导式 ---> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式2: [要插入的值/表达式 for i in 序列/列表 if 条件]
num_list = [12, 31, 41, 36, 543, 233, 44, 63, 111, 312, 123]
new_list = [i**2 for i in num_list if i % 2 == 0]
print(new_list)