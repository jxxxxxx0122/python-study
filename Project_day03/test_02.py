# 定义字符串的三种方式
s1 = "Hello" #双引号定义
s2 = 'Python' #单引号定义
s3 = """
Hello:
    Welcome to Python !
    Nice to meet you !
"""  #三引号定义

print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))


#转义字符 --->  \'  \"  \n  \t
msg = 'It\'s a good day.'
print(msg)

msg2 = "It's a good day."
print(msg2)

msg3 = "Hello的意思是\"您好\""
print(msg3)

msg4 = 'Hello的意思是\"您好\"'
print(msg4)

print("\tWelcome to Python ! \n\tNice to meet you !") #\n 换行   \t 制表符，相当于按了Tab缩进


# 字符串的拼接
s1 = "Hello ""World""!"
print(s1)

msg1 = "It's a good day"
msg2 = "Let's talk about Python."
print("I said:" + msg1 + "," + msg2)

# 案例 ---> str(int数字) ---> 将int类型的数字转为字符串
name = "三金"
age = 22
hobby = "Python"
print("Hello, My name is " + name + ", I am " + str(age) + " years old. " + "I like " + hobby + ".")

# 字符串格式化 ---> 方式一：%s 占位符
name = "三金"
age = 22
hobby = "Python"
print("Hello, My name is %s, I am %s years old. I like %s" % (name, age, hobby))

# 字符串格式化 ---> 方式二： f"..{变量名/表达式}.."
# -------------------> 最推荐的方式
name = "三金"
age = 22
hobby = "Python"
print(f"Hello, My name is {name}, I am {age} years old. I like {hobby}" )


# 输入与输出
# ---> 获取键盘上的数据 --> input(...)
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Your name is {name}, your age is {age}")

#案例：银行卡ATM取款
#总金额
total = 10000

# 1.输入密码
password = input("Enter your password: ")
print(f"Right ! Your password is {password}")

# 2.输入取款金额
num = int(input("Enter a number: "))

# 3.计算余额并输出 ---> num 需要用 int(..) 转换为 int 类型才可以进行计算
print(f"The balance is: {total - int(num)}")