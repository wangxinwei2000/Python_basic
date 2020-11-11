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

print('*'*45)
def cal_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        result  = func(*args,**kwargs)
        end   = time.time()
        print(f'项目用时:{end - start}')
        return result
    return inner

@cal_time
def sum_add(n):
    sum = 0
    for i in range(0,n):
        sum = sum +i
    print(sum)
    return sum
@cal_time
def add(x,y):
    return x+y
print(sum_add(10000000))
print('*'*45)
print(add(x=67,y=90))

#
print('*'*45)
def can_play(func):
    def inner(name,game,*args,**kwargs):
        x = kwargs.get('t',19)
        if x >22:
            print("can't play game")
        else:
            func(name,game,*args,**kwargs)

    return inner
# @cal_time
@can_play
def play_game(name,game,*args,**kwargs):
    print(f'{name} play  {game}')

play_game('张三','斗地主',t=49)