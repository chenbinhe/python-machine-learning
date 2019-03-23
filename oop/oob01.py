# 定义一个学生类，用来形容学生

#定义一个空的类，注意缩进，与class平齐为外部操作
class Student():
    #空类必须有pass，类下面不允许为空
    pass

#定义一个学生对象
binhe = Student()


class PythonStudent():
    #属性不允许为空用None占位，不允许不赋值，也可以给个默认值
    name = None
    age  = 18
    course = "python"

    def doHomework(self):
        print("doing homework")

        #函数末尾有return语句
        return None

# 实例化一个PythonStudnet对象
shishi = PythonStudent()
print(shishi.name)
print(shishi.age)

#注意这里没有传入参数
shishi.doHomework()


class A():
    name = "dada"
    age  = 18

    #注意say的写法，参数有一个self
    def say(self):
        self.name = "aaaa"
        self.age  = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def sayagain(s):
        print("My name is {0}".format(s.name))
        print("My age is {0}".format(s.age))


# 此时，A为类实例
print(A.name)
print(A.age)

print("*"*20)

# id可以鉴别一个变量是否和另一个变量
print(id(A.name))
print(id(A.age))

print("*"*20)

#定义了一个对象
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
# 对象里属性 的id和类实例里的是一样的，A.name 与a.name是一个变量print(A.name)
print(A.age)

print("*"*20)

print(id(A.name))
print(id(A.age))

print("*"*20)
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print("*"*20)

print(A.__dict__)
print(a.__dict__)

# 说明类实例的属性和其对象的实例的属性在 对象的属性没有重新赋值之前 是同一个变量，有相同存储地址,且a里面的成员为空

print("*"*20)
a.name = "yaoyao"
a.age  = 16
print(a.__dict__)

print("*"*20)

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("*"*20)

YY = A()
print(A.name)
YY.sayagain()
YY.say()
# 对象调用类中的函数会，自动传入第一个参数，这里syaagain没有对属性进行修改，所以属性不变，say改变了属性，所以会打印改变后的值
# 如果先调用say，则sayagain会打印出新的属性


class Teacher():
    name = "tt"
    age = 19
    def say(self):
        self.name = "mm"
        self.age = 17
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def sayagain():
        print(__class__.name)
        print(__class__.age)
        print("Hello nice to meet you again")

t = Teacher()
t.say()
#如果t.sayagain 就挂，因为只能类来访问
Teacher.sayagain()

print("*"*20)

class B():
    name = "lll"
    age = 18

    def __init__(self):
        self.name = "aaa"
        self.age  = 200

    def say(self):
        print(self.name)
        print(self.age)

class C():
    name = "bbb"
    age  = 90


a = B()
a.say()
#A.say()将出错，但可以用A.say(a)
B.say(a)
B.say(B)
B.say(C)#传进来，有name,age就可以出来
#以上鸭子模型，不管是不是一个类型，可以传入就可通过