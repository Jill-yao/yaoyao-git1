chinese = int(input("请输入语文作业用时(分钟):"))
math =int(input("请输入数学作业用时(分钟):"))
english = int(input("请输入英语作业用时(分钟):"))

total = chinese + math + english

print(f"语文:{chinese}分钟")
print(f"数学:{math}分钟")
print(f"英语:{english}分钟")
print(f"三科作业总共耗时:{total}分钟")
