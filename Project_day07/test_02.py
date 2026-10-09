# # 元组(tuple) 基本操作  ------>  元素可以重复, 有序, 不可修改
# t1 = (80, 95, 78, 50, 76, 80, 85, 30)
#
# print(t1)
# print(type(t1))
#
# # 索引访问
# print(t1[0])
# print(t1[-1])
#
# # 切片
# print(t1[:5])
#
# # count() 统计元素的个数
# print(t1.count(80))
#
# # index() 获取元素的索引(第一个匹配到的索引)
# print(t1.index(80))
#
# # # 注意点: 如果定义单元素的元组, 单个元素后需要加上逗号, 比如(100,)
# t2 = ()
# print(t2)
# print(type(t2))
#
# t3 = (100,)
# print(t3)
# print(type(t3))
#
# # # -----------------------------元组(tuple) 组包 与 解包 ----------------------------
# t1 = (5, 2, 5, 7, 45, 23, 12)
#
#
# # 解包操作
# # 基础解包(变量数量与容器的元素个数一致)
# a,b,c,d,e,f,g = t1
# print(a,b,c,d,e,f,g)
#
# # * 扩展解包 (* 收集剩余的所有元素, 封装列表list中)
# first,second,*other,last = t1
# print(first,second)
# print(other)
# print(last)
#
# *other,last2,last1 = t1
# print(other)
# print(last2)
# print(last1)


# 案例1: a = 10, b = 20, 交换变量值并输出
a = 10
b = 20

# # 组包
# t = a,b
# # 解包
# b,a = t
# 合并
a,b = b,a

print(a)
print(b)

# 案例2: a = 100, b = 200, c = 300, 交换变量值, 将a,b,c赋给c,a,b, 并输出
a = 100
b = 200
c = 300

c,a,b = a,b,c
print(a)
print(b)
print(c)

