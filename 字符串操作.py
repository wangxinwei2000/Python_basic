str='123456789'
try:
    print(str.index('8'))
except:
    print('数据不存在')

print(str[: : -1])
str = sorted(str,reverse=True)
str = ''.join(str)
print(type(str))
print(str)
print(str.ljust(19,"+"))

name,age = '杨向阳',19
print(f'name={name},age={age}')
print('name=%s,age=%d'% (name,age))
print('name={},age={}'.format(name,age))
i=0
while i<len(str):
    print(str[i],end=' ')
    i+=1
i=0
str = list(str)
while i<len(str)/2:
    temp = str[i]
    str[i] = str[len(str)-i-1]
    str[len(str)-i-1] = temp
    i+=1
print(str)
str = ''.join(str)
print(str)


Str='uxuycywgcwhbecuy'
print(Str.count('u'))



