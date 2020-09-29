import random
a = random.randint(10,100)#生成[0,100]整数
print(a)
a = random.random()
print(a)  #[0,1)

a = random.randrange(0,100)
print(a)  #[0,100)整数

a = random.choice(['a','b','c','d','e'])
print(a)#随机抽取列表中得一个数据

a = random.sample(['a','b','c','d','e'],2)
print(a)#随机抽取n个数据
