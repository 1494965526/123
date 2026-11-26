'''
l=[1,2,3,4,5]
l.append(6)
l.insert(0,0)
l.pop(2)
l.remove(4)
l[l.index(3)] = 10  # 找到值 3 的位置，并改成 10
l.__len__()
print(l)
print(l.__len__())
'''
'''
m=[1,2,3,4,5,6,7,8,9]
print(m[:3])
'''
'''
s=[87,95,49,34]
s.append(34)
p=sum(s)/len(s)
max(s)
min(s)
print(s)
'''
'''
print("请输入1.2.3.4")
a=int(input())
l=['睡觉']
while a!=4: 
    match a:
       case 1:
          print(l)      
       case 2:
          l.append(input())
          print(l)
       case 3:
          l.pop(int(input()))
          print(l)
    a=int(input())       
    if a==4:
       print("退出")
       break
    '''
'''
l=[1,2,3,2,4,5]
a=set(l)
print(sorted(a))

'''
