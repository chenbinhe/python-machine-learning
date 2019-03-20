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