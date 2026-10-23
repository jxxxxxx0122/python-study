"""
封装: 将数据(属性)和操作数据的方法绑定在一起, 形成一个独立的单元(类), 保护数据不被外部访问, 通过访问修饰符实现封装
    1.私有属性: 在属性名前加双下划线__
    2.私有方法: 在方法名前加双下划线
注意事项: Python中是没有真正的私有机制;
"""
from ensurepip import version

# class Car:
#     def __init__(self, brand, model, color, owner):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.__owner = owner
#
#     def start(self):
#         print(f"{self.brand} {self.model} 正在启动...")
#
#     def run(self):
#         print(f"{self.brand} {self.model} 正在行驶...")
#
#     def stop(self):
#         print(f"{self.brand} {self.model} 停止行驶...")
#
#     def __control_fuel(self):
#         print(f"{self.brand} {self.model} 正在控制油门... ")
#
#     def get_owner(self):
#         return self.__owner[0:1] + "**"
#
# if __name__ == '__main__':
#     car = Car("Audi", "A6", "黑色", "三金")
#     # print(car.brand)
#     # print(car.model)
#     # print(car.color)
#     print(car._Car__owner)
#     car._Car__control_fuel()
#
#     # car.start()
#     # car.run()
#     # car.stop()
#     # print(car.get_owner())




"""
继承: 描述的是两个类之间的关系, 子类继承父类, 就可以获取到父类之中的属性和方法(非私有)
"""
# class Car:
#     def __init__(self, brand, model, color, owner):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.__owner = owner
#
#     def start(self):
#         print(f"{self.brand} {self.model} 正在启动...")
#
#     def run(self):
#         print(f"{self.brand} {self.model} 正在行驶...")
#
#     def stop(self):
#         print(f"{self.brand} {self.model} 停止行驶...")
#
#     def __control_fuel(self):
#         print(f"{self.brand} {self.model} 正在控制油门... ")
#
#     def get_owner(self):
#         return self.__owner[0:1] + "**"
#
#
# # 燃油车
# class FuelCar(Car):
#     pass
#
# # 电车
# class ElectricCar(Car):
#     pass
#
# if __name__ == '__main__':
#     c1 = FuelCar("BMW", "X5", "黑色", "张三")
#     c1.start()
#     c1.run()
#     c1.stop()
#     print(c1.get_owner())
#     print(c1.brand)
#     print(c1.model)
#     print(c1.stop())




"""
继承 - 重写
"""
# class Car:
#     def __init__(self, brand, model, color, owner):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.__owner = owner
#
#     def start(self):
#         print(f"{self.brand} {self.model} 正在启动...")
#
#     def run(self):
#         print(f"{self.brand} {self.model} 正在行驶...")
#
#     def stop(self):
#         print(f"{self.brand} {self.model} 停止行驶...")
#
#     def __control_fuel(self):
#         print(f"{self.brand} {self.model} 正在控制油门... ")
#
#     def get_owner(self):
#         return self.__owner[0:1] + "**"
#
#     def charge(self):
#         print(f"{self.brand} {self.model} 正在补充燃料...")
#
# # 燃油车
# class FuelCar(Car):
#     def charge(self):
#         # 方式一: super().方法名()
#         # super().charge()
#
#         # 方式二: 类名.方法名(self)
#         # Car.charge(self)
#
#         print(f"{self.brand} {self.model} 正在加油...")
#
# # 电车
# class ElectricCar(Car):
#     def charge(self):
#         print(f"{self.brand} {self.model} 正在充电...")
#
# if __name__ == '__main__':
#     c1 = FuelCar("BMW", "X5", "黑色", "张三")
#     c1.charge()
#
#     c2 = ElectricCar("Tesla", "Model Y", "白色", "李四")
#     c2.charge()




"""
多继承
注意事项: 一个类继承了多个父类时, 默认优先使用第一个父类中的同名属性或方法, 可以使用 类名.__mro__属性 或 类名.mro() 方法查看调用顺序
"""
# class Car:
#     def __init__(self, brand, model, color, owner):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.__owner = owner
#
#     def start(self):
#         print(f"{self.brand} {self.model} 正在启动...")
#
#     def run(self):
#         print(f"{self.brand} {self.model} 正在行驶...")
#
#     def stop(self):
#         print(f"{self.brand} {self.model} 停止行驶...")
#
#     def get_owner(self):
#         return self.__owner[0:1] + "**"
#
#     def charge(self):
#         print(f"{self.brand} {self.model} 正在补充燃料...")
#
#
# # 小米智驾
# class XiaomiAiDriving:
#     """小米AI智能驾驶"""
#     def __init__(self, version="V1.0"):
#         self.version = version
#
#     def run(self):
#         print(f"欢迎使用小米AI智能驾驶系统{self.version} 正在行驶...")
#
# # 澎湃汽车
# class PengPaiCar(Car, XiaomiAiDriving):
#     def __init__(self, brand, model, color, owner, version="V1.0"):
#         Car.__init__(self, brand, model, color, owner)
#         XiaomiAiDriving.__init__(self, version)
#
#     def run(self):
#         Car.run(self)
#         XiaomiAiDriving.run(self)
#
#
# if __name__ == '__main__':
#     c = PengPaiCar("XiaoMi", "Su 7", "璀璨洋红", "三金")
#     print(c.__dict__)
#
#     # print(PengPaiCar.__mro__)
#     # print(PengPaiCar.mro())
#
#     c.run()




"""
多态: 是指同一个方法, 具有不同的形态, 行为, 表现
"""
# class Car:
#     def __init__(self, brand, model, color, owner):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.__owner = owner
#
#     def start(self):
#         print(f"{self.brand} {self.model} 正在启动...")
#
#     def run(self):
#         print(f"{self.__owner} {self.brand} {self.model} 正在行驶...")
#
#     def stop(self):
#         print(f"{self.brand} {self.model} 停止行驶...")
#
#     def get_owner(self):
#         return self.__owner[0:1] + "**"
#
#     def charge(self):
#         print(f"{self.brand} {self.model} 正在补充燃料...")
#
# # 燃油车
# class FuelCar(Car):
#     def charge(self):
#         print(f"{self.brand} {self.model} 正在加油...")
#
# # 电车
# class ElectricCar(Car):
#     def charge(self):
#         print(f"{self.brand} {self.model} 正在充电...")
#
#
# # 补充燃料函数
# def handle_charge(car: Car): # 函数参数类型声明 --- 指定的是父类型
#     car.charge()
#
#
# # 测试代码
# if __name__ == '__main__':
#     handle_charge(FuelCar("BMW", "X5", "白色", "张三"))
#     handle_charge(ElectricCar("BYD", "汉", "黑色", "李四"))

"""
鸭子类型
    Python中关注的是对象的行为(它有什么方法), 而不是对象的类型(它是什么类)
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'Dog: {self.age} 岁的 {self.name} 正在游泳...')

class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'Duck: {self.age} 岁的 {self.name} 正在游泳...')

class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'Pig: {self.age} 岁的 {self.name} 正在游泳...')


def go_swimming(duck):
    duck.swimming()


# 测试代码
if __name__ == '__main__':
    go_swimming(Dog("旺财", 4))
    go_swimming(Duck("唐老鸭", 2))
    go_swimming(Pig("佩奇", 1))