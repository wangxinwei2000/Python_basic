# b = "No"
from functools import reduce


def num_muti(n:int):
    global b
    b= 'OK'
    result =0
    for i in range(0,n):
        print(i,end='')
        result = result +i
    print()
    return result
def sum_num(List):
    result = 0
    for i in List:
        result =result+i
    return result
print(num_muti(10))
print(b)

num = [1,2,3,4,5,6,7,8]
num2 = {1,2,3,4,5,6,7,8}
print(sum_num(num))
print(sum_num(num2))
print(sum_num(range(1,9)))


# 可变参数
def result_sum(*args):
    result =0
    for arg in args:
        result+=arg
    return result
print(result_sum(13,324,123,1323))


# 递归
sum = 0
def Recursion(n):
    global sum
    sum = sum+n
    print(sum)
    n=n-1
    if n >=0:
        return Recursion(n)
    else:
        print(sum)
        return sum
print(f'result = {Recursion(8)}')

# 匿名函数
func = lambda a,b : a**b
print(func(2,3))
def Func(a,b,func):
    return func(a,b)
add = lambda a,b :a+b
subtract = lambda a,b :a-b
print(Func(34,56,subtract))

List = [12,323,13,123,132]
List.sort(reverse=False)
print(List)

List = [{'name':'张三','age':17,'height':190},{'name':'李四','age':18,'height':190},{'name':'王五','age':13,'height':190},{'name':'赵六','age':10,'height':190}]
List.sort(reverse=False,key=lambda ele :ele['age'])
print(List)


# filter 过滤使用
age = [12,31,1,4123,132,3214,143,41234,12313,134]
x=filter(lambda x : x>999,age)
for i in x:print(i)

# map
y=map(lambda x:x**2 if x>999 else x,age)
for i in y:print(i)

#reduce
z=reduce(lambda x,y:x+y,age)
print(f'result={z}')
sum =0
for i in age:sum=sum+i
print(f'result={sum}')

List = [{'name':'张三','age':17,'height':190},{'name':'李四','age':18,'height':190},{'name':'王五','age':13,'height':190},{'name':'赵六','age':10,'height':190}]
z = reduce(lambda x,y:x+y['age'],List,0)
print(f'result={z}')
print('*'*30)

# 高阶函数
# 闭包
def func(x):
    x=10+x
    print(x)
    def inner():
        nonlocal x
        y=10+x
        print(y)
        return x

    return inner
print(func(7)())

# 代码执行时常
print('*'*30)
import time
sum = 0
start = time.time()
for i in range(0,10000000):
    sum = sum +i
time.sleep(3)
end   = time.time()
print(sum)
print(end-start)




