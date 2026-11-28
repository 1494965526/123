
'''import math

def q(a,b,c):
     x1=(-b+math.sqrt(b**2-4*a*c))/2*a
     x2=(-b-math.sqrt(b**2-4*a*c))/2*a
     return x1,x2

a=float(input())
b=float(input())
c=float(input())

x1,x2=q(a,b,c)
print(x1,x2)

'''

'''
def mul(x,*args):
    for n in args:
        x=x*n

    return x

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')
        '''

def x(n,*args):
    d=n
    for b in args:
        d+=b
        return d

    return n+args
def y(a):
    if a%2==0:
        print("ou")
    else:
        print("ji")


n=int(input())
#m=int(input())





y(n)