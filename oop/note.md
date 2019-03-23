#oop  -python
- python面向对象编程
    - 基础
    - 公有私有
    - 组合 Minxi
    
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数
    
    
    
# 1.面向对象概述 ObjectOriented oo
- OOP思想
    - 世界皆是由一个个模型下面的具体事物构成，类，对象
    
- 几个名词
    OO :面向对象
    OOA :面向对象分析
    OOD :面向对象设计
    OOI :面向对象的实现
    OOP :面向对象的实现过程
    A - D - I顺序
    
- 类和对象
    - 类：抽象名词，代表一个集合，共性的事情
    - 对象：具体的事物，个体
    - 类和对象的关系
        - 一个对象，代表一类的某个个体
        - 类是抽象一个有共性的集体
        
- 类中的内容
    - 表明事物的特征，叫做 属性（变量）
    - 表明事物功能或动作，称为成员方法（函数）
    
    
# 2. 类的基本实现
-   类的命名
    - 遵守变量命名的规范
    - 大驼峰（由一个或多个单词构成，每个单词首字母大写，单词跟单词直接相连）
    - 尽量避开跟系统命名相似的命名
    
-   如何声明一个类
    - 必须用class
    - 类有属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，允许使用None
    案例 01.py
    
- 实例化类

    变量 = 类名（） #实例化一个对象
    
- 访问对象成员
    -使用.
        - obj.成员属性
        - obj.成员方法
        
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员检查
    
        #dict 前后各有两个下划线
        - obj.__dict__
        
    - 类所有的成员
        #dict 前后各有两个下划线
        class_name.__dict__
        
    
    
 #3. anaconda基本使用
 - anaconda 主要是一个虚拟环境管理器
 - 还是一个安装包管理器
 - conda list： 显示anaconda安装的表
 - conda env list : 显示anaconda的虚拟环境列表
 - canda create -n xxx python=3.7: 创建python版本为3.7的虚拟环境，名字为xxx，可以用这个环境跑专门的项目
 - canda activate xxx ：激活这个环境，以备使用
 ## 要让代码在新激活的环境下跑，用file---settings---project interpreter--点一下那个设置图标小齿轮---选conda env，下existing env,再点图标...将创建的环境设为运行环境，选anaconda3/envs/xxx/bins/python3.7
 ## 这里原环境在    /home/username/anaconda3/bin/python3.7   这里python/python3/python3.7区别不大均可选
        
        
# 4. 类和对象成员分析
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类在定义时开辟一个存储空间，存储成员时使用的时与类关联的一个对象,称为类实例，类实例只有一个
- 对象在定义时会额外开辟一个内存空间，只是拷贝了类实例的值，真实属性存储还在类实例中
    class Student():
        name = "xxx"
        age = 18
    a = Student()

- 对象访问一个成员时，如果对象没有该成员，尝试访问类中的同名成员。如果对象中有此成员，则一定使用此成员     
- 创建对象的时候，类中的成员不会放入对象中，而是得到一个空对象，成员为空
- 通过对象对类中成员的重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类的成员

# 5.self   
    class A():
    name = "dada"
    age  = 18

    #注意say的写法，参数有一个self
    def say(self):
        self.name = "aaaa"
        self.age  = 200 
        print("My name is {0}".format(self.name))
        print("My age is{0}".format(self.age))
        
- self 在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中
- self 并不是关键字，只是一个用于接受对象的普通参数，理论上可用任何变量名代替
- 类里的方法如果没有定义self，则这个方法只能类调用。无self称为绑定类的方法
- 使用绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__.成员名，访问在类里定义的成员
        
        
# 6.面向对象三大特性
- 封装
- 继承
- 多态

        
## 6.1 封装
- 封装就是对对象的成员进行访问控制
- 封装的三个级别
    - public 公开
    - protected 受保护的
    - private 私有的
    - public protected private不是关键字

- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中


    class Person():
        #name 是公有
        name = "chenb"
        
        #age 是私有
        __age = 18
- 私有
    - 私有是最高级别的封装，只能在当前类或对象中访问
    - 在成员前面添加两个下划线即可
    - Python的私有不是真私有，是一种称为name mangling的改名策略，其实不是真是不是__age去访问
      可以使用_classname_attributename访问，如上方可用_Person_age访问
      可用Person.__dict__看到，__age其实被改成_Person_age存进去的    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
