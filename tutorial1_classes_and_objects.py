class Dog:  # 定义类
    # 构造函数，首先传入self
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    # 定义一个行为，首先传入self
    def bark(self):
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOF"')
        else:
            print(self.name, 'says "woof woof"')

    def walk(self):
        print(self.name, 'is walking')

    # 描述自己
    def __str__(self):
        return "I'm a dog named " + self.name


# 继承 IS-A关系
# Class ServiceDog inherits attributes and methods from class Dog.


class ServiceDog(Dog):  # 定义一个子类，可以从头开始定义，也可以利用(超类)
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)  # 调用超类Dog的构造函数
        self.handler = handler  # 添加子类ServiceDog的新属性
        self.is_working = True

    def bark(self):  # 覆盖超类的行为
        if self.is_working:
            print(self.name, 'says, "I can\'t bark, I\'m working"')
        else:
            Dog.bark(self)


class Person:
    def __init__(self, name):
        self.name = name

    # 描述自己
    def __str__(self):
        return "I'm a person and my name is " + self.name


# 继承 IS-A关系
class DogWalker(Person):
    # 省略constructor，subclass默认采用superclass Person的constructor
    def walk_the_dogs(self, dogs):
        for dog_name in dogs:
            dogs[dog_name].walk()


# 组合 HAS-A关系
class Hotel:
    def __init__(self, name):
        self.name = name
        self.kennel = {}  # 使用字典来组合一组Dog对象

    def check_in(self, dog):  # 提供狗对象，办理入住
        if isinstance(dog, Dog):
            self.kennel[dog.name] = dog
            print(dog.name, 'is checked into', self.name)
        else:
            print('Sorry, only Dogs are allowed in', self.name)

    def check_out(self, name):  # 提供狗的名字属性，返回狗对象
        if name in self.kennel:
            dog = self.kennel[name]
            print(dog.name, 'is checked out of', self.name)
            del self.kennel[dog.name]
            return dog
        else:
            print('Sorry,', name, 'is not boarding at', self.name)
            return None

    def hire_walker(self, walker):
        if isinstance(walker, DogWalker):
            self.walker = walker  # 组合 HAS-A关系
        else:
            print('Sorry,', walker.name, 'is not a Dog Walker')

    def walking_service(self):  # 委托（delegation）
        if self.walker is not None:
            self.walker.walk_the_dogs(self.kennel)


# 实例化对象
tom = Dog('Tom', 12, 38)
jackson = Dog('Jackson', 9, 12)
jerry = ServiceDog('Jerry', 10, 40, 'ZZ')
jay = DogWalker('Jay')
hotel = Hotel('Doggie Hotel')

# 调用对象的属性
print(tom.age)
print(jackson.age)

# Polymorphism：调用不同类的对象的相同名字的方法
tom.bark()
jackson.bark()
jerry.bark()

# 调用__str__方法输出对象描述
print(tom)
print(jackson)
print(jerry)

# 测试IS-A关系
print(isinstance(jerry, Dog))
print(isinstance(tom, ServiceDog))

hotel.check_in(tom)
hotel.check_in(jackson)
hotel.check_in(jerry)

hotel.hire_walker(jay)
hotel.walking_service()  # 委托（delegation），Hotel不会遛狗，但是DogWalker有此行为

hotel.check_out(tom.name)
hotel.check_out(jackson.name)
hotel.check_out(jerry.name)
