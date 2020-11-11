import json

Tuple = (1,2,3,4,5,6)
for i in Tuple:
    print(i,f'index={Tuple.index(i)},count={Tuple.count(i)}',end='\n')
Dict ={'name':'张三','age':18,'sex':'男'}
for key in Dict.keys():
    print(Dict.get(key,''))
Dict['name']='王五'
print(Dict)
Dict['height']=190
print(Dict)
# del Dict['height']
Dict.pop('height')
print(Dict)
# Dict.clear()
# print(Dict)
Dict2 = {'weight':89}
print(Dict2.update(Dict))
print(Dict2)
print(Dict2.values())
print(Dict2.keys())
for i in Dict2.items():
    a,b=i
    print(a,b)
Dict3 = Dict2.copy()
print(Dict3)
Dict4 = {k:v for k,v in Dict3.items() }
print(Dict4)


name ={'张三','李四','王五','赵六'}
for i in name:
    print(i)
name1 = {23,1231,123,123}
name.update(name1)
print(name)

print('*'*34)
nums = [2,2,3,4,54,3,5,6,23,3,0]
nums= set(nums)
nums = list(nums)
nums.sort(reverse=False)
print(nums)

# eval 可以执行字符串里的代码
# str  = input('please input str: ')
# print(f'result = {eval(str)}')

# Json的使用，把列表元组字典转化成JSON字符串
Dict ={'name':'张三','age':18,'sex':'男'}
m = json.dumps(Dict)
print(type(m))
print(m)
m = json.loads(m)  #将loads 可以将json字符串转化成为python中的数据
print(m)