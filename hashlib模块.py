import hashlib
import hmac
x = hashlib.md5()
code=input('请输入密码：')
x.update(code.encode('utf-8'))
print(x.hexdigest())

code1=x.hexdigest()


x1=hashlib.md5()
code2=input('请输入密码: ')
x1.update(code2.encode('utf-8'))
print(x1.hexdigest())
if x1.hexdigest() == code1:
    print('密码正确')
else:
    print('密码错误')