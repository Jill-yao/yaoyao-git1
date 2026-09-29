#BMI计算器

height=float(input('身高(cm):'))
weight=float(input('体重(kg):'))

BMI=weight/(height/100)**2

print(f'{BMI= :.1f}')

if 18.5<=BMI<24:
    print("你的身材很棒！")
elif 30>BMI>24:
    print('你有些肥胖')

elif BMI>=30:
    print('你重度肥胖了')
else:
    print('你的身材不够标准哟！')





    