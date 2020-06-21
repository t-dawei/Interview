1. 谈谈你对 python 的特点：
    语言 简洁、优雅
    高级语言，更加注重问题解决效率，而不用关心程序底层方面的细节
    解释型语言 ----> 边解释边运行 
    强动态语言 ---> 变量地址运行时才分配 不需要提前申请
    既支持面向对象也支持面向过程编程 ---->3
    丰富的库
    可拓展、可移植、可嵌入

2. python与其他语言的区别：
    优点：
        不用像C语言一样特别注重底层内存地址相关细节，python更加注重开发的效率
        代码简洁，少量代码就可以实现其他语言可能需要很多行代码才能实现的功能
        python的第三方库特别丰富，功能实现比其他语言要方便，特别在数据爬取和处理以及机器学习等方面有着很大的优势
    缺点：
        python是解释型语言，在运行速度方面就不如编译型语言快些


3. 谈谈面向对象编程和面向过程编程的区别：
    面向过程编程：
        分开考虑数据和函数
        将数据和函数按照业务逻辑顺序再组织在一起
        根据业务逻辑从上到下写代码

    面向对象编程：
        将数据和函数绑定到一起,进行封装
        减少重复代码的编写，更快更高效的开发程序

4. 什么是解释型语言和编译型语言：
    解释型语言指程序在执行时才翻译，每执行一次都要编译一次，效率较低
    编译型语言就是直接编译成机器可以执行代码，只需翻译一次，效率相对较高

5. python 的解释器种类和相关特点：
    CPython --> c语言开发 使用最广的解释器
    IPython ---> CPython 上的一个交互式的解释器
    JPython ---> python代码编译成java字节码
    IronPython --> 运行在微软NET平台上的解释器，把python代码编译成.net字节码
    PyPy ---> 采用动态编译 目标是提升执行效率

6. python3 与 python2 的区别：
    py2 print是个类 打印用空格隔开，py3 print 是个函数，打印加括号
    py2 中使用xrange， py3 中使用range 
    py2 字符串默认编码是ASCII（阿斯特码），py3 字符串默认编码是unicode
    py2 / 的结果是整型， py3 / 的结果是浮点型


7. python3 和 python2 中 int 和 long 类型的区别：
    python2 中有 int, long. python3 中只有 int
    pyhton2 中 int 类型最大数不能超过sys.maxint ,这个数与平台相关
    python2 可以在数据末尾加上L 来定义长整型
    python3 中整合了 int, long ,python3 中的int 相当于2中的long


8. 什么是PEP8：
    python 代码格式指南 

9. python 之禅：
    import this
    告诉大家如何写 规范的python代码

10. DosStrings：
    文档字符串， 解释程序 


11. python 类型注解：
    def foo(num: int) -> str:
        return str(num)

12. python 对象命名规范：
    类名首字母大写
    内部类使用额外的前导下划线
    变量：小写，由下划线连接各个单词
    常量：所有字母大写

13. python 中的注释方式：
    单行注释 #
    多行注释 ‘’‘ “”“

14. 列举几个规范代码风格的工具：
    pylint, flake8

15. 列举python3 中基本数据类型：
    6个
    str     不可变数据类型
    int     不可变数据类型
    set     可变
    list    可变
    tuple   不可变数据类型
    dict    可变

16. 如何区别可变数据类型和不可变数据类型
    从对象内存地址方向来说
    可变数据类型：在内存地址不变的情况下，值可改变（列表和字典是可变类型，但是字典中的 key 值必须是不可变类型）
    不可变数据类型：内存改变，值也跟着改变。（数字，字符串，布尔类型，都是不可变类型）可以通过 id() 方法进行内存地址的检测

17. python3 字符串格式化方法
    %s format fstring
    print(f'the a value is:{a}')
    print('the string value is %s %s' % (a,a))
    print('the string value is {}'.format(a))

18. 字符串常用方法：
    str.title() 
    ...

19. 按值传递与引用传递的含义和区别：
    按值传递：将参数视为原变量的一个副本， 该副本的改变对原始数据没有影响 
    按引用传递：将参数视为原变量的一个别名，两者都指向同一个内存地址 

20. python 函数参数是按值传递还是引用传递：
    解释器会查看对象引用（内存地址）指示的那个值的类型，如果变量指示一个可变的值，就会按引用调用语义。
    如果所指示的数据的类型是不可变的，则会应用按值调用语义

21. 利用正则分割字符串
    # ：& * 分割
    import re
    re.split(':|&|*'，string)
    re.split('[:&*]', string)

22. 求两个list的交集和差集
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    print(set(a)&set(b))
    print(set(a)^set(b))
    {3, 4, 5}
    {1, 2, 6, 7}

23. 列表展开
    l = [[1,2],[3,4],[5,6]]
    print([i for j in l for i in j])

24. 列表中字典排序
    d1 = [
        {'name'： 'alice', 'age'： 38},
        {'name'： 'bob', 'age'： 18},
        {'name'： 'Carl', 'age'： 28},
    ]
    print(sorted(d1, key=lambda x:x['age']))

25. 迭代器切片
    from itertools import islice
    gen = iter(range(10))
    for i in islice(gen, 0, 4):
        print(i)

26.下列代码的输出：
    a = (1,2,3,[4,5,6,7],8)
    a[3][0] = 2
    print(a)
    (1, 2, 3, [2, 5, 6, 7], 8)


27. 三种文件读取的区别和作用
    read() --> 读取整个文件或者根据大小读取
    readline() --> 读取一行
    readlines() ---> 读取整个文件 按行生产list

28. 简述with 语句的作用：
    对文件的访问
    不管是否发生异常都会自动释放资源， 比如自动关闭文件， 线程锁的获取和释放等
 
 29. python 连接mysql代码
    conn = pymysql.connect(host='localhost', 
    port=3306, user='root', 
    passwd='1234', db='user', charset='utf8mb4')#声明mysql连接对象
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)#查询结果以字典的形式
    cursor.execute(sql语句字符串)#执行sql语句
    conn.close()#关闭链接
   
30. python 中函数的装饰器是什么？有什么作用？举例说明。
    函数的装饰器还是函数
    他的功能是可以在不改变一个函数的代码前提下，给这个函数添加额外的功能
    比如适用于插入日志、性能测试、权限检验等

31. 怎么理解python 的垃圾回收机制
    引用计数机制：Python 采用了类似 Windows 内核对象一样的方式来对内存进行管理。每一个对象，都维护这一个对指向该对对象的引用的计数。
        对象被创建  a=14
        对象被引用  b=a
        对象被作为参数,传到函数中   func(a)
        对象作为一个元素，存储在容器中   List={a,”a”,”b”,2}

        当该对象的别名被显式销毁时  del a
        当该对象的引别名被赋予新的对象，   a=26
        一个对象离开它的作用域，例如 func函数执行完毕时，函数里面的局部变量的引用计数器就会减一（但是全局变量不会）
        将该元素从容器中删除时，或者容器被销毁时

        缺点：
        维护引用计数消耗资源，维护引用计数的次数和引用赋值成正比，而不像mark and sweep等基本与回收的内存数量有关。
        无法解决循环引用的问题。A和B相互引用而再没有外部引用A与B中的任何一个，它们的引用计数都为1，但显然应该被回收。
        循环引用的示例：
        list1 = []
        list2 = []
        list1.append(list2)
        list2.append(list1)

，系统会自动维护这些标签，并定时扫描，当某标签的引用计数变为 0 的时候，该对就会被回收
    标记-清除
        基本思路是先按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，遍历以对象为节点、以引用为边构成的图，把所有可以访问到的对象打上标记，然后清扫一遍内存空间，把所有没标记的对象释放。
    分代回收
        Python默认定义了三代对象集合，索引数越大，对象存活时间越长。

    这种思想简单点说就是：对象存在时间越长，越可能不是垃圾，应该越少去收集。
    这样的思想，可以减少标记-清除机制所带来的额外操作。分代就是将回收对象分成数个代，每个代就是一个链表（集合），代进行标记-清除的时间与代内对象
    从上面代码可以看出python里一共有三代，每个代的threshold值表示该代最多容纳对象的个数。默认情况下，当0代超过700,或1，2代超过10，垃圾回收机制将触发。
    0代触发将清理所有三代，1代触发会清理1,2代，2代触发后只会清理自己。


32. 列举python中的魔法函数
    __call__
    魔法函数可以把类的实例当作函数调用，示例如下：
    class Bar:
    def __call__(self, *args, **kwargs):
        print('in call')
    b = Bar()
    b()
    # in call
    
    __init__
    构造器，当一个实例被创建的时候调用的初始化方法
    __new__
    是对象实例化时第一个调用的方法，它只取下 cls 参数，并把其他参数传给 __init__ 
    __del__
    是对象的销毁器，当对象需要在销毁时做一些处理的时候这个方法很有用

33. 如何判断一个对象是方法还是函数
    在类内的def是方法，单独的def是函数
    
34. 简述 python 中定义类方法的3种方法，有何区别：
    普通方法
    @classmethod
    @staticmethod
    区别：
        foo方法绑定对象A的实例，class_foo方法绑定对象A，static_foo没有参数绑定
        slef通常用作实例方法的第一参数，cls通常用作类方法的第一参数
        普通方法可通过实例a调用
        @classmethod 和 @staticmethod通过类对象或对象实例调用

    class Person(object):
    
    grade=6     # 类变量
    
    def __init__(self):
        self.name = "king"
        self.age=20
        
    def sayHi(self):    #加self区别于函数
        # 实例方法(self) 可以访问实例变量和类变量
        print ('Hello, your name is?',self.name)
        print(self.grade)

    def sayAge(self):
        print( 'My age is %d years old.'%self.age)
        
        
    @staticmethod     # 静态方法不能访问类变量和实例变量，也不能使用self
    def sayName():
        print ("my name is king") 
        
          
    @classmethod     #类方法可以访问类变量，但不能访问实例变量
    def classMethod(cls):  
        #print('cls:',cls)
        print('class grade:',cls.grade)        
        #print("class method")

    p = Person()
    p.sayHi()

        
35. 简述一下python中反射机制：
    一共有四个关键的函数，getattr, hasattr, setattr, delattr
    python的反射，它的核心本质其实就是利用字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员，一种基于字符串的事件驱动！
    
36. metaclass 的作用：
    即元类
    是类似创建类的模版，所有的类通过他new出来的
    使用元类创建类的单例模式


37. 当退出Python时是否释放所有内存分配
    那些具有对象循环引用或者全局命名空间引用的变量，在Python退出是往往不会被释放；
    另外不会释放C库保留的部分内容。
    

38. 命名空间的理解：
    在Python程序执行过程中，会有局部命名空间、全局命名空间和内建命名空间同时存在。局部命名空间记录函数内部的变量、传入函数的参数、嵌套函数等被命名的对象；全局命名空间记录模块的变量、函数、类及其它导入的模块等被命名的对象；内建命名空间记录Python自身提供的函数、模块等被命名的对象。

39. 正则表达式的基本知识以及常见的正则
    pass
    
40. pass 语句的作用
    占位符
    避免语法错误
    
41. python 中的== 和 is 区别
    == 值相等
    is 地址是否一致

42. python 中作用域
    当 Python 遇到一个变量的话它会按照这的顺序进行搜索
    本地作用域(Local)--->当前作用域被嵌入的本地作用域(Enclosing locals)--->全局/模块作用域(Global)--->内置作用域(Built-in)

43. 3元运算
    a = b if b > 1 else c

44. 列举5个python中的标准模块
    os
    pathlib
    urllib
    itertool
    time
    random
    re
    asyncio 异步库

45. python中最大递归次数，如何突破：
    默认的递归次数是1000
    可以通过设置修改限制：
    import sys
    sys.setrecursionlimit(1500)
    另外需要注意的是 sys.setrecursionlimit() 只是修改解释器在解释时允许的最大递归次数，此外，限制最大递归次数的还和操作系统有关。
 
 46. python 中的mro
     Python 是支持面向对象编程的，同时也是支持多重继承的。一般我们通过调用类对象的 mro()方法获取其继承关系。
 
 47. 新式类与旧式类的区别：
     Python 2.x 中默认都是经典类，只有显式继承了 object 才是新式类，Python 3.x 中默认都是新式类，经典类被移除，不必显式的继承 object。 新式类都从 object 继承，经典类不需要。 新式类的 MRO(method resolution order 基类搜索顺序)算法采用 C3 算法广度优先搜索，而旧式类的 MRO 算法是采用深度优先搜索。 新式类相同父类只执行一次构造函数，经典类重复执行多次。
     
48. isinstance 作用：
    判断一个对象是否为另一个对象的子类

49. 什么是断言，作用？
    在 Python 中是断言语句 assert 实现此功能，一般在表达式为 True 的情况下，程序才能通过。
    
50.  dir()是干什么用的：
    查看对象有什么属性和方法
    
51. 列举python中你知道的异常错误：
    AttributeError 对象属性错误
    NotImplementedError 未实现的方法
    TypeError 类型错误
    IndentationError 缩进错误

52. copy和deepcopy 的区别
    copy.copy()浅拷贝，只拷贝父对象，不会拷贝对象的内部的子对象。 
    copy.deepcopy()深拷贝，拷贝对象及其子对象
    
53. *args, **kwargs 含义及用法
    当我们不知道向函数传递多少参数时可用
    *args 传递列表
    **kwargs 传递字典
    
54. Python 中会有函数或成员变量包含单下划线前缀和结尾，和双下划线前缀结尾，区别是什么?
    "单下划线" 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量，以单下划线开头的代表不能直接访问的类属性，需通过类提供的接口进行访问
    "双下划线" 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据
    双下划线开头和结尾的代表 Python 里特殊方法专用的标识，如 __init__（）代表类的构造函数。
    

55. 装饰器代码示例：
    1. 什么是装饰器
        在不改变原函数的基础下，给函数添加一些装饰功能
    # 修饰函数
    def set_func(func):

        print('进入修饰函数')
        def test_func():
            print('我是修饰函数')
            func()

        return test_func

    # 原函数
    @set_func
    def demo():
        print(f'原函数')

    demo()

56. 迭代器代码示例：
    1. 什么是迭代器
        python中一种可以记录遍历位置的对象
        迭代器有两个重要的方法：iter() 和 next()
        迭代器对象通常通过for来遍历元素

    代码：
    list = [1, 2, 4]
    it = iter(list)
    print(next(it))
    print(next(it))

57. 生产器：
    1. 什么是生产器
        python中使用了yield关键字的函数称为生产器

    g = (1, 2, 3)

58. 取整
    四舍五入：
        round(3.3) == 3
    向上取整：
        import math
        math.ceil(3.3) == 4
    向下取整
        1. int(3.3) == 3
        2.  import math
            math.floor(3.3) == 3
    百分比保留小数点后两位         print('%.2f%%' % ((count/len(str2)) * 100))

59. 开方
    1. pow(4, 0.5)
    2. 4 ** 0.5
    3. import math
        math.sqrt(4)

60. 字符与阿斯特码转化
    # 将字符转化为asci
    ord()
    # 将asci转化为字符
    chr()


python中的线程和进程，以及使用场景，你知道协程吗？
GIL是什么，为什么会有GIL，去掉会怎样，有了GIL为什么还要给程序加锁？
即全局解释器所（global interpreter lock），每个线程在执行时候都需要先获取GIL，保证同一时刻只有一个线程可以执行代码，即同一时刻只有一个线程使用CPU，也就是说多线程并不是真正意义上的同时执行

python 多线程示例 读写
    消费者-生产者模式

用lambda来实现：

    def sum(x,y):
      return x+y
    
    p = lambda x,y:x+y
    print(p(4,6))


二进制：
    a = 10
    bin(a)

    int(a, 2)

字符串方法：
    1. 大小写、首字母大写、判断大小写
        string.capitalize()
        string.islower()
        string.isupper()
        string.lower()
        string.upper()
        string.swapcase() # 大小写反转

    2. 统计不同字符个数
        string.count(str, beg=0, end=len(string))

    3. 特定字符开头和结尾
        string.endswith(obj, beg=0, end=len(string))
        string.startswith(obj, beg=0,end=len(string))

    4. 字符查找
        string.find(str, beg=0, end=len(string)) # 不在返回-1
        string.index(str, beg=0, end=len(string)) # 不在异常
        string.rfind(str, beg=0,end=len(string) )
        string.rindex( str, beg=0,end=len(string))

    5. 字符或者字母
        string.isalnum()
        string.isalpha()
        string.isdigit()

    6. 去除空格
        string.lstrip()
        string.rstrip()
        string.strip([obj])

    6. list 转化为字符串

    7. 最大小字符串
        max(str)
        min(str)

    8. 字符串替换
        string.replace(str1, str2,  num=string.count(str1))

    9. 字符串分割
        string.split(str="", num=string.count(str))

list 方法：
    1. 增加元素
        list.append(obj)
        list.extend(seq)
        list.insert(index, obj)

    2. 删除元素
        list.pop([index=-1]) # 默认最后一个
        list.remove(obj) # 第一个匹配

    3. 统计元素次数
        list.count(obj)

    4. 反转
        list.reverse()

    5. 排序
        list.sort(key=None, reverse=False)

    6. 清空
        list.clear()

    7. 复制
        list.copy()


dict 方法：
    1. 添加
        dict.fromkeys(seq，val)
        dict.update(dict2)

    2. 删除
        pop(key[,default])
        popitem() # 最后一对键值对

    3. key、value、键值对
        dict.keys()
        dict.values()
        dict.items()

    4. 获取值
        dict.get(key, default=None)

    5. 浅复制
        dict.copy()

    6. 清空
        dict.clear()


set 方法：
    1. 添加元素
        add()
        update(set)

    2. 删除
        pop()   # 随机删除
        remove(item) # 指定删除 不在异常
        set.discard(value) # 指定删除

    3. 清空
        clear()

    4. 浅复制
        copy()

    5. 集合差集
        set.difference(set) #方法是直接在原来的集合中移除元素，没有返回值。
        set.difference_update(set) #方法是直接在原来的集合中移除元素，没有返回值。

    6. 集合并集
        set.union(set1, set2...)

    7. 集合交集
        intersection()
        intersection_update()

    8. 判断是否有交集
        set.isdisjoint(set)

    9. 判断是否为子集
        set.issubset(set)
        set.issuperset(set)

    10. 移除两个集合中重复的元素
        set.symmetric_difference(set)
        set.symmetric_difference_update(set)





