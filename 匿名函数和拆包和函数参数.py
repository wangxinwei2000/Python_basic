fun = lambda x ,y : x**y
print(fun(2,3))
list1 =[1,2,3,34,452,2345]
print(max(list1))

def s1():
    return 34,89
a,b = s1()
print(a,b)


# >>>def square(x) :            # 计算平方数
# ...     return x ** 2
# ...
# >>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
# [1, 4, 9, 16, 25]
# >>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
# [1, 4, 9, 16, 25]

fun2 = lambda x:x**2
list2=map(fun2,list1)
print(list(list2))
func = lambda x,y : x if x>y else y
print(func(1,2))

# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比方说对一个序列求和，就可以用reduce实现：
#
# >>> from functools import reduce
# >>> def add(x, y):
# ...     return x + y
# ...
# >>> reduce(add, [1, 3, 5, 7, 9])
# 25
from functools import reduce
fun3 = lambda a,b : a+b
result = reduce(fun3,list1)
print(result)

# 函数参数
def uer_info(name , age , sx):
    print(f'姓名{name},年龄{age},性别{sx}')

uer_info('张三',sx='男',age=56)

# 缺省参数
def uer_info2(name,age = 78,gender ='男'):
    print(f'姓名{name},年龄{age},性别{gender}')

uer_info2('张三',gender='男',age=56)

# 不定长参数(包裹位置传递)
def user_info3(*args):
    print(args)

user_info3(787,123,21312,1231)

# （包裹关键字传递）
def user_info4(**kwargs):
    print(kwargs)
user_info4(name = 'TOM',age =18 ,id =110)
# 结果为：{'name': 'TOM', 'age': 18, 'id': 110}