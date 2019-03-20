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
 ## 这里原环境在    /home/username/anaconda3/bin/python3.7
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
