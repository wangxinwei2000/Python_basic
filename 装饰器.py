import time
def FUN(func):
    def MU(a,b):
        print('原函数执行')
        func(a,b)
        print('原函数执行完了')
    return MU

@FUN
def Zi(a,b):
    print(a+b)
    print('我是原函数')

# sf = FUN(Zi)
# sf()
Zi(89,90)
