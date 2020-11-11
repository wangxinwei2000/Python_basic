import uuid#用来生成全局唯一id
import time
print(uuid.uuid1()) #32长度    每个字符有16个选择   16**32
# for i in range(1,1000):
#     print(uuid.uuid1())
#     time.sleep(0.4)
print(uuid.uuid3(uuid.NAMESPACE_DNS,'张三'))  #根据参数生成固定id
print(uuid.uuid3(uuid.NAMESPACE_DNS,'张三'))


print(uuid.uuid5(uuid.NAMESPACE_DNS,'张三'))   #根据参数生成固定id

print(uuid.uuid4())   #随机生成


