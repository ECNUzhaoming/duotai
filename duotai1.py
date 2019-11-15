class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):  # 抽象方法，仅由约定定义
        print(self.name, '叫')  # 当子类没有重写talk方法的时候调用

    def animal_talk(obj):  # 多态
        obj.talk()


class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' % self.name)  # 重写talk方法


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


a = Dog('a')
Animal.animal_talk(a)
