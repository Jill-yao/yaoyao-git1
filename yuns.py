#print(321+12)
#print(321-12)
#print(321*12)
#print(321/12)
#print(321//12)
#print(321%12)
#print(321**12)

#print(2+3*5)
#print((2+3)*5)
#print((2+3)*5**2)
#print(((2+3)*5)**2)

#赋值运算符 =
#a = 10
#b = 3
#a += b
#a*=a+2
#print(a)

#比较运算符
flag0=1==1
flag1=3>2
flag2 = 2<1
flag3= flag1 and flag2
flag4= flag1 or flag2
flag5= not flag0

#print('flag0=',flag0)
#print("flag1=",flag1)
#print('flag2=',flag2)
#print('flag3=',flag3)
#print('flag4=',flag4)
#print('flag5=',flag5)
#print(flag1 and not flag2)
#print(1>2 or 2==3)

#输入圆的半径  计算圆的面积 和周长
r=float(input ("请输入圆的半径"))
p=2*3.1416*r
s=3.1416*r**2
print(f'周长：{p:.2f}')
print(f'面积：{s:.2f}')



