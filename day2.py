"""L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

print(L[2][1])"""


'''a=(175/80.5)**2
if a<18.5:
    print("qin")
elif 18.5<a<25:
    print("zhengchang")
elif 25<a<28:
    print("guo zhong")
elif 28<a<32:
    print("fei pang")
else:
    print("fei pang zhong")'''


'''h=175
w=80.5
b=(h/w)**2
if b<18.5:
    print("过轻")
elif 18.5<b<25:
    print("正常")
elif 25<b<28:
    print("过重")
elif 28<b<32:
    print("肥胖")
else:
    print("严重肥胖")'''


'''sum=0
for x in range(101):
    sum =sum + x
print(sum)
'''
'''
L = ['Bart', 'Lisa', 'Adam']
for L in L:
    print('hello,',L)
    '''
'''
a = 100
while a > 0:
    a += 1
    print(a)
'''
'''
d = {1,2,3}
s = set(1,[2,3])'''

'''
n1=255
n2=1000
print(hex(n1),hex(n2))'''
'''
score = int(input("请输入数字："))

match score:
    case n if n < 0 or n > 100:
        print("输入错误")
    case n if n >= 90:
        print("优秀")
    case n if n >= 80:
        print("良好")
    case n if n >= 70:
        print("中等")
    case n if n >= 60:
        print("及格")
    case n if n >= 0:
        print("不及格")
    case _:
        print("输入错误")
        '''

'''
a = int(input("请输入数字："))
if a % 2 == 0:
    print("偶数")
else:
    print("奇数")
    '''
'''
a="1"
b="2"
c=input("请输入账号：")
d=input("请输入密码：")

if c==a:
  print("账号正确")
else:
    print("账号错误")
if d==b:
    print("密码正确")
else:
    print("密码错误")
if c==a and d==b:
    print("登录成功")
    '''

'''
a=input("请输入数字：")
b=input("请输入数字：")
c=(a,b)
if a==b:
    print("相等")
d=max(c)
print("最大值为：",d)
'''

'''
import random
a = random.choice([1, 3])
b = int(input("请输入数字："))
match (a, b):
    case (a, b) if a == b:
        print("相等")
    case (1, 2) | (2, 3) | (3, 1):
        print("你输了")
    case _:
        print("你赢了")
print("电脑出的是：", a)
'''
