# from random import randint,choice
import random
import copy
List = [1,2,3,4,5,66,7,8,9,10]
List.insert(4,9)
print(List)
List.append('张三')
print(List)
List1=[111,222,333,444,555]
List.extend(List1)
print(List)
result = List.pop()
print(List,f'result = {result}')
result =List.pop(11)
print(List,f'result = {result}')
result = List.remove(111)
print(List,f'result = {result}')
# result = List.clear()
# print(List,f'result = {result}')
del List[1]
print(List,f'result = {result}')
print(List.index(4),List.count(6),34 in List)
List.sort(reverse=True)
print(List)
Str='aksjxnaowiqcwcv'
print(sorted(Str))

print('*'*34)
List2 = [2,3,4,45,2,31,43,45,653,234,4326,2341234,14324,1431]
List2.sort()
print(List2)
print(List2[-1])

print('*'*34)
List3 =['da','sda','','','asd','asd']
new_List3=[]
for word in List3:
    if word!='':
        new_List3.append(word)
print(new_List3)
List3 = new_List3
print(List3)
# i=0
# while i<len(List3)-1:
#     if List3[i]=='':
#         List3.remove(List3[i])
#         i-=1
#     i+=1
# print(List3)
print('*'*34)

rooms = [[],[],[]]
teachers = ['A','B','C','D','E','F','G','H','I']
for teacher in teachers:
    # n = randint(0,2)
    # room[n].append(teacher)
    room = random.choice(rooms)
    room.append(teacher)

print(rooms)

print('*'*34)
nums = [i for i in range(10)]
print(nums)
print('*'*34)
nums = [i for i in range(10) if i%2!=0]
print(nums)
print('*'*34)
nums = [(x,y) for x in range(5,9) for y in range(10,20) if y%x==0]
print(nums)


#浅拷贝
print('*'*34)
word = [1,2,3,4,[2,3,4]]
word1 = word.copy()
word[1]='A'
word[-1][0]='T'
print(word1)

# 深拷贝
print('*'*34)
word = [1,2,3,4,[2,3,4]]
word1 = copy.deepcopy(word)
word[-1][0]='T'

print(word1)

print('*'*34)
