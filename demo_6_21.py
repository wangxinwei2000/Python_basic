# import random
# import functools
# import os
# import time
# list1=[1,2,3,4,5,6,7]
# t1=tuple(list1)
# print(list1)
# print(t1)
# list2=list(t1)
# print(list2)
# list3=list2[2::2]
# print(list3)
# print(list2[:3])
# print('========================================')
# Listy=['lily','Jack','Kai','PUA']
# while True:
#     name=input('请输入用户名')
#     if name not in Listy:
#         print("用户注册成功")
#         Listy.append(name)
#         break
#     else:
#         print('用户已存在,请重新输入')
# print(f'全体成员：{Listy}')
# Listy.append(['张三','李四'])
# Listy.extend(['小明','小红'])
# print(Listy)
# list1=[1,2,3,4,5,6,7]
# list1.insert(2,'淦')
# print(list1)
# del list1[2]
# print(list1)
# a=list1.pop(2)
# print(a)
# print(list1)
# list1=[1,4,6,7,3,9,10,45]
# print(list1.sort(reverse=True))
# print(list1)
# i=0
# while i<len(list1):
#     print(list1[i])
#     i=i+1
# for i in list1:
#     print(i)
# print('======================================')
# List2=[[1,2,3],[4,5,6],[7,8,9]]
# for i in List2:
#     print(i)
#     for j in i:
#        if j!=i[len(i)-1]:
#            print(j,end='   ')
#        else:
#            print(j)
# print('=========================')
# techer=['A','B','C','D','E','F','G','H']
# office=[[],[],[]]
# for i in techer:
#     num=random.randint(0,2)
#     office[num].append(i)
# print(office)
# print(tuple(office))
# print('A' in tuple(office))
# Tuple=(1,[3],3,2,5,2,7)
# print(Tuple.index(2))
# print(Tuple.count(11))
# Tuple[1][0]='张三'
# print(Tuple)
# diction={'name':'张三','年龄':28,'成绩': 98}
# print(diction)
# diction['name']='特朗普'
# print(diction)
# diction['id']='2087201681'
# print(diction)
# del diction['id']
# print(diction)
# # diction.clear()
# print(diction)
# print(diction.get('name'))
# print(diction['name'])
# print(diction.keys())
# print(diction.values())
# print(diction.items())
# for i in diction.values():
#     print(i)
# for value,key in diction.items():
#     print(f'{key}={value}')
# s1={1,2,3,4,5}
# print(type(s1))
# s2=set('张三')
# print(s2)
# print(s1)
# s1.add(996)
# print(s1)
# s1.update([12,45])
# print(s1)
# s1.remove(996)
# print(s1)
# s1.discard(12)
# print(s1)
# p1=s1.pop()
# print(p1)
# print(s1)
# print(1 in s1)
# print(max(s1))
# for i ,j in enumerate(s1,start=1):
#     print(f'下标为{i},数据为{j}')
# List=[(i,j) for i in range(1,4) for j in range(1,4)]
# print(List)
# for i in range(1,10):
#     if i%3!=0:
#         print(List[i-1],end=' ')
#     else:print(List[i-1],end='\n')
# ====================================字典合并
# list1=[59,75,66,90]
# list2=['name','age','score','phones']
# dict1={list2[i]:list1[i] for i in range(len(list1))}
# print(dict1)
# dict2={key:value for key,value in dict1.items() if value>=70}
# print(dict2)
# =======================================集合推导式
# set1={i for i in range(3,10)}
# print(set1)
# =======================================不定长参数
# def info_user(*args):
#     print(args)
#
# info_user('长江',6999)
# =======================================包裹关键字传递
# def info_user(**kwargs):
#     print(kwargs)
#
# info_user(name='Lily',age=29,score=99)
# =========================================拆包
# def info_user():
#     return 12,89
# print(info_user())
# a,b=info_user()
# print(a,b)
# dict1={'name':'张三','age':12}
# a,b=dict1
# print(a,b)
# print(dict1[a],dict1[b])
# ==================================变量值交换
# a,b=999,666
# a,b=b,a
# print(a,b)
# =================================学员管理系统
# info=[]
# def info_add():
#     person_name=input('请输入姓名：')
#     person_age=int(input('请输入年龄: '))
#     person_number=input('请输入学号: ')
#     dict={'name':person_name,'age':person_age,'number':person_number}
#     global info
#     for i in info:
#         if i['name']==dict['name']:
#             print('学生信息已经存在')
#             return
#     info.append(dict)
# def info_dete():
#     person_name=input('请输入你要删除的学员信息')
#     global info
#     for i in info:
#         if i['name']==person_name:
#             info.remove(i)
#             print('数据删除成功')
#             return
#     else:
#             print('数据不存在，无法删除')
# def info_modify():
#     person_name=input('请输入要修改的学员信息')
#     global info
#     for i in info:
#         if i['name']==person_name:
#             while True:
#                 t=input('请输入你要修改的信息类型：')
#                 if t=='name':
#                     new_name=input('请输入要修改的新姓名：')
#                     i['name']=new_name
#                 elif t=='age':
#                     new_age=int(input('请输入要修改的新年龄：'))
#                     i['age']=new_age
#                 elif t=='number':
#                     new_number=input('请输入要修改的新学号：')
#                     i['number']=new_number
#                 elif t=='finsh':
#                     return
#
# def info_search():
#     name=input('请输入要查询的学员信息')
#     global info
#     for i in info:
#         if i['name']==name:
#             print('学员信息为: 学员姓名：',i['name'],'学员年龄: ',i['age'],"学员学号：",i['number'])
# info_add()
# # info_add()
# # print(info)
# # info_dete()
# # print(info)
# # info_modify()
# # print(info)
# info_search()
# ========================================lambda
# fun1=lambda a:a**3
# fun2=lambda a,b,c=10:a*b*c
# print(fun1(6))
# print(fun2(12,34,10))
# fun3=lambda *args:args
# print(fun3(3,4))
# fun4=lambda **kwargs:kwargs
# print(fun4(name='张三',age=77))
# fun5=lambda a,b:a if a>b else b
# print(fun5(100,56))
# List1=[{'name':'Lily','age':19},{'name':'KAI','age':17}]
# List1.sort(key=lambda x:x['age'],reverse=True)
# print(List1)
# ===================================高阶函数
# print(abs(-999))
# print(round(1.9))
# def add(a,b):
#     return abs(a)+abs(b)
# print(add(-166,-88))
# def add2(a,b,f):
#     return f(a)+f(b)
# print(add2(-99,-10,abs))
# ===================================
# list2=[1,2,3,4,5,6,7]
# def fun(x):
#     return x**2
# def fun2(x,y):
#     return x*y
# def fun3(x):
#     return x%2==0
# result=map(fun,list2)
# print(result)
# print(list(result))
# result=functools.reduce(fun2,list2)
# print(result)
# result=filter(fun3,list2)
# print(result)
# print(list(result))

# =============================文件管理
# f=open('text2.txt','a+')
# f.seek(0,0)
# print(f.read())
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')
#
# f.close()
# f=open('text2.txt','a+')
# f.seek(0,0)
# Str=input('\nplease input information: ')
# f.write(Str)
# f.close()
# =============================文件备份
# old_name=input('请输入要备份的文件: ')
# index=old_name.rfind('.')
# if index>0:
#     postfix=old_name[index:]
# new_name=old_name[:index]+'[备份]'+postfix
# old_f=open(old_name,'r')
# new_f=open(new_name,'w')
# while True:
#     con=old_f.read()
#     if len(con)==0:
#         print('Copying is finished')
#         break
#     new_f.write(con)
# # f=open('text1[备份].txt','rb')
# # print(f.read())
# old_f.close()
# new_f.close()
# ============================文件夹操作
# print(os.getcwd())
# os.mkdir('文件夹1')
# os.chdir('文件夹1')
# os.mkdir('文件夹1_2')
# os.rename('text2.txt','new_text2.txt')
# ============================批量重命名
# os.chdir('文件夹1')
# dir_list=os.listdir()
# print(dir_list)
# for i in dir_list:
#     new_name='NEW'+i
#     os.rename(i,new_name)
# ==========================创建对象
# class Person():
#     def __init__(self):
#         self.age=19
#     def Name(self,name):
#         self.name=name
#         print(name)
#     def Age(self):
#         print(f'Age is {self.age}')
#     def __str__(self):
#         return '创建了一个名为'+self.name+'的变量'
#     def __del__(self):
#         print('对象已经删除')
#
#
# one=Person()
# one.Name('张三')
# # one.age=18
# one.Age()
# print(one)
# del one
# ============================继承
# ==========================子类调用父类方法多继承

# class Fu(object):
#     def __init__(self):
#         self.KongFu='父亲古法'
#     def Show_master(self):
#         print(f'方法为{self.KongFu}')
# class Mu(object):
#     def __init__(self):
#         self.KongFu='母亲的古法'
#     def Show_master(self):
#         print(f'方法为{self.KongFu}')
#
# class Zi(Fu,Mu):
#     pass
#     def __init__(self):
#         self.KongFu='自造古法1.0'
#     def Show_master(self):
#         # self.__init__()
#         print(f'方法为{self.KongFu}')
#     def Fu_master(self):
#         Fu.__init__(self)
#         Fu.Show_master(self)
#     def Mu_master(self):
#         Mu.__init__(self)
#         Mu.Show_master(self)
# class Sun(Zi):
#     pass
#     def __init__(self):
#         self.KongFu='自造古法2.0'
#     def Show_SUN_master(self):
#         self.__init__()
#         print(f'方法为{self.KongFu}')
#     def Show_Fu_master(self):
#         Zi.__init__(self)
#         Zi.Show_master(self)

#
#
# one1=Zi()
# print(one1.KongFu)
# print(Zi.__mro__)
# one1.Show_master()
# one1.Fu_master()
# one1.Mu_master()
# print('=============================')
# one2=Sun()
# one2.Show_master()
# one2.Show_Fu_master()
# one2.Fu_master()
# ==========================================私有权限
# class Student(object):
#     def __init__(self):
#         self.__name='Lily'
#     def get_name(self):
#         return self.__name
#     def set_name(self,new_name):
#         self.__name=new_name
#
# print(Student().get_name())
# one=Student()
# print(one.get_name())
# one.set_name('刘能')
# print(one.get_name())
#=========================================== 多态
# class Amry_Dog(object):
#     def work(self):
#         print('警戒任务')
#
# class Drug_Dog(object):
#     def work(self):
#         print('追查毒品')
# class Dog(object):
#     def work_Mission(self,dog):
#         dog.work()
#
# one_1=Amry_Dog()
# one_2=Drug_Dog()
# one_3=Dog()
# one_3.work_Mission(one_1)
# one_3.work_Mission(one_2)
# ===============================制作模块
# from module_1 import *
# add(34,56)
# minus(34,78)
# ==================================time模块
# t1=time.time()
# print(t1)
# time.sleep(4)
# t1=time.time()
# print(t1)
# s=time.ctime(t1)
# print(s)
# s=time.localtime(t1)
# print(s)
# t=time.mktime(s)
# print(t)
# t1=time.strftime('%Y-%m-%d:%H:%M:%S')
# print(t1)

# ==========================================datetime
# import datetime
# import time
# print(datetime.time.hour)
# print(time.localtime().tm_hour)
# ==========================================random 的使用
# r1=random.random()
# print(r1)
# r2=random.uniform(2,4)
# print(r2)
# r3=random.randrange(start=10,stop=1000,step=9)
# print(r3)
# List1=[12,334,545,656,6544]
# r4=random.choice(List1)
# print(r4)
# List2=[1,2,3,4,5,6,7,8]
# random.shuffle(List2)
# print(List2)
# slice=random.sample(List2,5)
# print(slice)
# print(List2)
# ============================================hashilb库

# import hashlib
# password='123456'
# list1=[]
# sha256=hashlib.sha256(password.encode('utf-8'))
# list1.append(sha256.hexdigest())
# pwd=input('请输入密码')
# sha256=hashlib.sha256(password.encode('utf-8'))
# pwd=sha256.hexdigest()
# print(pwd)
# print(list1)
# for i in list1:
#     if i==pwd:
#         print('location is sucessful')
# =====================================================进程和线程
# from multiprocessing import Process
# from time import sleep
# m=1
# def test1(s,name):
#     global m
#     while True:
#         sleep(s)
#         m+=1
#         print('这是任务1.。。。。。。。。。。',os.getegid(),'=========',os.getppid(),name)
#
#
# def test2(s, name):
#     global m
#     while True:
#         sleep(s)
#         m += 1
#         print('这是任务1.。。。。。。。。。。', os.getegid(), '=========', os.getppid(), name)
# number=1
# if __name__=='__main__':
#     p1=Process(target=test1,name='任务1',args=(1,'aa'))
#     p1.start()
#     p2=Process(target=test2,name='任务2',args=(2,'bb'))
#     p2.start()
#     while True:
#         number+=1
#         if number==100:
#             p1.terminate()
#             p2.terminate()
#             break
#     print('=====================================')
#     print('*'*20)
# from multiprocessing import Process
# from time import sleep
# import os
# n=1
# List=[]
# def test1(s):
#     global n
#     while True:
#         List.append(n)
#         print(List)
#         n=n+1
#         sleep(s)
#         print("this is test_1==============","进程码：",os.getpid(),"父进程码：",os.getppid(),'===',n)
# def test2(s):
#     global n
#     while True:
#         List.append(n)
#         print(List)
#         n=n+1
#         sleep(s)
#         print("this is test_2==============","进程码：",os.getpid(),"父进程码：",os.getppid(),'===',n)
# if __name__=='__main__':
#     number=1
#     print(os.getpid())
#     p1=Process(target=test1,name='任务1',args=(1,))
#     p1.start()
#     p2=Process(target=test2,name='任务2',args=(2,))
#     p2.start()
#     print(p1.name)
#     print(p2.name)
#     while True:
#         sleep(0.2)
#         number=number+1
#         if number>100:
#             p1.terminate()
#             p2.terminate()
#             break
#     print('=======FINISH+++++++++++++++++++++')
# import time
# import os
# from multiprocessing import Process, Pool
# import random
# def task(task_name):
#     print('任务开始了',task_name)
#     start=time.time()
#     time.sleep(random.random()*2)
#     end=time.time()
#     str= '任务完成{}！用时{}，进程码{}'.format(task_name,(end-start),os.getpid())
#     print(str)
#     return str
# container=[]
# def callback_func(n):
#     container.append(n)
# if __name__=='__main__':
#     pool=Pool(5)
#     tasks=['听音乐','吃饭','洗衣服','打游戏','散步','看孩子','做饭']
#     for task1 in tasks:
#         pool.apply(task,args=(task1,))
#     pool.close()
#     pool.join()
#     print('OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     print(container)
#============================================================队列
# from multiprocessing import Queue
# from time import sleep
# q=Queue(5)
# q.put('A')
# q.put('B')
# q.put('C')
# q.put('D')
# q.put('E')
# print(q.qsize())
# if not q.full():
#     q.put('F',timeout=3)
# else:
#     print('队列已满')
# while True:
#     if not q.empty():
#         sleep(2)
#         print(q.get())
#     else:
#         print('队列已空')
#         break
# ================================================队列通讯
# 写数据进程执行的代码:
# from multiprocessing import Process, Queue
# import os
# import time
# import random
#
#
#
# def write(q):
#   print('正在执行 write: %s' % os.getpid())
#   for value in ['A', 'B', 'C']:
#     print('正在下载' ,value)
#     q.put(value)
#     time.sleep(1)
#
# # 读数据进程执行的代码:
# def read(q):
#    print('正在执行 read: %s' % os.getpid())
#    while True:
#        try:
#           value = q.get(timeout=2)
#           print('Get %s from queue.' % value)
#           time.sleep(1)
#        except:
#            print('函数执行完毕')
#            break
#
# if __name__ == '__main__': #父进程创建Queue， 并传给各个子进程：
#     q = Queue(5)
#     pw = Process(target = write, args = (q, ))
#     pr = Process(target = read, args = (q, ))# 启动子进程pw， 写入:
#     pw.start()
#     pw.join()# 启动子进程pr， 读取:
#     pr.start()# 等待pw结束:
#     pr.join()# pr进程里是死循环， 无法等待其结束， 只能强行终止:
#     # pr.terminate()
#     print('===================================')

# ========================================多线程
# import os
# import threading
# import time
#
#
# def write(n):
#   print('正在执行 write: %s' % os.getpid())
#   for value1 in ['A', 'B', 'C']:
#     print('正在下载' ,value1)
#     time.sleep(n)
# def read(n):
#    print('正在执行 read: %s' % os.getpid())
#    for value in ['a', 'b', 'c']:
#        print('正在听', value)
#        time.sleep(n)
#        # time.sleep(n)
#
# if __name__ == '__main__':
#     t1=threading.Thread(target=write,name='aa',args=(1,))
#     t1.start()
#     t2=threading.Thread(target=read,name='bb',args=(1,))
#     t2.start()
#     n=1
#     while True:
#                # time.sleep(5)
#                # print(n)
#                n+=1
#                if n>10:
#                    print('程序终止')
#                    break
# ===============================================================多线程2
# import os
# import threading
# import time
#
# money=0
# lock=threading.Lock()
# def task1():
#     global money
#     lock.acquire()
#     for i in range(1000000):
#         money+=1
#     print('---------------->>money1的值为: ',money)
#     lock.release()
# def task2():
#     global money
#     lock.acquire()
#     for i in range(1000000):
#         money+=1
#     print('---------------->>money2的值为: ',money)
#     lock.release()
#
# if __name__ == '__main__':
#     th1=threading.Thread(target=task1)
#     th2=threading.Thread(target=task2)
#     th1.start()
#     th2.start()
#     th1.join()
#     th2.join()
#     print('程序终止')
# =================================================死锁----一定要避免死锁
# 解决：1.重构 2.使用timeout
# import os
# from threading import Thread,Lock
# import time
# lockA= Lock()
# lockB= Lock()
# def run1(fun):
#         if lockA.acquire():
#             print(fun+'获得A锁')
#             time.sleep(0.1)
#             if lockB.acquire(timeout=3):#等待3s，若无法执行则直接释放锁
#                 print(fun+'又获得了A锁和B锁')
#                 lockB.release()
#             lockA.release()
# def run2(fun):
#         if lockB.acquire():
#             print(fun+'获得B锁')
#             time.sleep(0.1)
#             if lockA.acquire(timeout=3):
#                 print(fun+'又获得了B锁和A锁')
#                 lockA.release()
#             lockB.release()
# if __name__ == '__main__':
#     t1=Thread(target=run1,args=('方法一',))
#     t2=Thread(target=run2,args=('方法二',))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#=============================================================生产者与消费者
# import threading
# import queue
# import time
# import random
# def produce(q):
#     i=0
#     while i<10:
#         num=random.randint(1,100)
#         q.put(num)
#         print(f"生产者生产了数据{num}")
#         time.sleep(1)
#         i+=1
#     q.put(None)
#     q.task_done()
# def consume(q):
#     while True:
#         item=q.get()
#         if item is None:
#             break
#         print(f"消费者获取{item}")
#         time.sleep(4)
#     q.task_done()
# if __name__ == '__main__':
#     q=queue.Queue(10)
#     arr=[]
#     th =threading.Thread(target=produce,args=(q,))
#     th.start()
#     tc=threading.Thread(target=consume,args=(q,))
#     tc.start()
#     th.join()
#     tc.join()
#     print("END")
# ===========================================================协程
# import time
# import gevent
# from greenlet import greenlet
# from gevent import monkey
# monkey.patch_all()
# def task1():
#     for i in range(3):
#         print('A',i)
#         time.sleep(1)
# def task2():
#     for i in range(3):
#         print('B',i)
#         time.sleep(1)
# def task3():
#     for i in range(3):
#         print('C',i)
#         time.sleep(1)
# if __name__ == '__main__':
#     ga=gevent.spawn(task1)
#     gb=gevent.spawn(task2)
#     gc=gevent.spawn(task3)
#     ga.join()
#     gb.join()
#     gc.join()
# =======================================================
# import gevent
# import requests
# from gevent import monkey
# def download(url):
#     response=requests.get(url)
#     content=response.text
#     print('网站{}，源码长度为{}'.format(url,len(content)))
# if __name__ == '__main__':
#     urls=['http://www.baidu.com','http://www.qq.com','http://www.163.com']
#     g1=gevent.spawn(download,urls[0])
#     g2=gevent.spawn(download,urls[1])
#     g3=gevent.spawn(download,urls[2])
#     gevent.joinall([g1,g2,g3])
# ===================================================================
# from gevent import monkey
#
# monkey.patch_all(select=False)
# import requests
# import gevent
#
#
# def f(url):
#     print('GET: %s' % url)
#     data = requests.get(url).text
#     print('%d bytes received from %s.' % (len(data), url))
#
#
# g1=gevent.spawn(f, 'https://www.python.org/')
# g2=gevent.spawn(f, 'https://www.yahoo.com/')
# g3=gevent.spawn(f, 'https://github.com/')
# gevent.joinall([
#    g1,g2,g3
# ])
# print("End of File")
# ===================================================djingo的使用
# import django
from Pack_oneself import *
print(model_1.add(78,90))
