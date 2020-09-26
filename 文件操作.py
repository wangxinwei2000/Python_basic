# 主要按照分类标准来看，方便记忆：
#
# 是否可写
# w 仅可写，写覆盖
# a 仅可写，写追加
# w+ 可以读写，写覆盖
# r+ 可以读写，写覆盖
# a+ 可以读写，写追加
# 是否可读
# r 仅可读
# r+ 可以读写
# w+ 可以读写
# a+ 可以读写
# 不可读的打开方式： w a
# 如果不存在会创建新文件的打开方式：a a+ w w+

# 1.打开 open()
# f = open('test1.txt','w')
# print('你好，你好')
# f.write('你好！，你好')
# f.close()
# f = open('test1.txt','r')
# print(f.read())
# f.close()


# 2 f.read(num)#读取文件中所有的内容,num字节
# f = open('test1.txt','r')
# # f.write('\nHELLO')
# s1=f.read()
# print(s1)
# f.close()

# 3.f.readlines读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。
# f = open('test1.txt','r')
# print(f.readlines())
# # ['你好！，你好\n', 'HELLO']
# f.close()

# 4 f.readline()一次性读取一行
# f = open('test1.txt','r')
# print(f.readline())
# f.close()

# 5. f.seek(偏移量，起始量) 0：文件开头(开始) 1：当前位置  2：文件结尾
# f = open('test1.txt','r')
# f.seek(4)
# print(f.read())
# f.seek(0,0)
# print('*'*20)
# print(f.read())
# f.close()

# 6.文件备份
# old_name = input('请输入要备份的文件')
# index = old_name.rfind('.')
# new_name = old_name[:index] + '-备份-' + old_name[index:]
# print(new_name)
# f1 = open(old_name,'r')
# s=f1.read()
# print(s)
# f2 = open(new_name,'w')
# f2.write(s)
# f2.close()
# f1.close()

# 7.import os 模块
import  os
# os.rename(f1,f2)重命名
# os.remove(f1)删除
print(os.path.basename('test1.txt'))
print(os.path.dirname('test1.txt'))

