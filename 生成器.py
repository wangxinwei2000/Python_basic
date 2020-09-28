from collections.abc import Iterable
gen = (x for x in range(1,100))
print(isinstance(gen,Iterable))
print(next(gen))
print(next(gen))

def fibonacci(n):
    a,b=0,1
    count=0
    res = []
    while True:
        if count>n:
            break
        yield a+b
        res.append(a+b)
        a,b=b,a+b
        count+=1
print('*'*10)
gen = fibonacci(100)
for i in gen:
    print(i)
