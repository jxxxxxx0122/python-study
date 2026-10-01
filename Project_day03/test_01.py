#变量 ----->python是动态类型语言，一个变量可以存储不同类型的数据（但在项目开发中，推荐变量只存储一种类型的数据）
num = 2026.9
print(num)

num = num + 1
print(num)

num = "ok"
print(num)

num = True
print(num)

a = True
print(a)

#案例
base = 20.7 #基础播放量
incr = 50 #每月增加的播放量
print("未来第一个月的播放总量： ",base + incr)
print("未来第二个月的播放总量： ",base + incr + incr)

#案例-升级：一次性定义多个变量
base,incr =  20.7,50
print("未来第一个月的播放总量： ",base + incr)
print("未来第二个月的播放总量： ",base + incr + incr)


#标识符----->命名规则：字母，数字，下划线；不能以数字开头；不能使用关键字


#案例 -----> 变量值交换
a = 10
b = 50
c = a
a = b
b = c
print(a,b,c)

a = 100
b = 200
c = 300
a,b,c = c,a,b
print(a,b,c)


# 常见数据类型 ---> type() 获取指定的字面量或变量的类型
print("Hello")
print(type("Hello")) #str

print(type(10)) #int
print(type(3.14)) #float
print(type(True)) #bool
print(type(False)) #bool
print(type(None)) #NoneType

num = -100
print(type(num))

# 常见数据类型 ---> isinstance(数据, 类型) --> bool值 --> 判定数据是否是指定的类型，如果是：True，否则：False
print(isinstance(num,int)) #True
print(isinstance(num,float)) #False
print(isinstance(num,bool)) #False