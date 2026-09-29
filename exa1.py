a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and b+c>a and a+c>b:
    p = a+ b + c 
    h = p / 2
    s =( h * (h - a)*(h -b)*(h-c))**0.5
    print (f'周长：{p}')
    print (f'周长：{s}')
else:
    print('不能构成三角形')
  