error_books = []

def show_menu():
    print("\n===== 孩子错题录入本 =====")
    print("1. 录入错题")
    print("2. 查看错题（按学科分组）")
    print("3. 删除错题")
    print("4. 退出程序")
    choice = input("请输入功能序号：")
    return choice

def add_error():
    """录入错题"""
    print("\n----- 录入新错题 -----")
    subject = input("请输入学科：")
    question = input("请输入错题题目：")
    reason = input("错误原因：")
    answer = input("正确答案：")
    # 构造错题字典，加入列表
    item = {
        "subject": subject,
        "question": question,
        "reason": reason,
        "answer": answer
    }
    error_books.append(item)
    print("✅ 错题录入成功！")

def view_error():
    """按学科分组查看错题"""
    if len(error_books) == 0:
        print("\n❌ 暂无错题记录！")
        return
    print("\n----- 错题本（按学科分组）-----")
    # 先收集所有学科，去重
    subjects = set()
    for item in error_books:
        subjects.add(item["subject"])
    
    # 按学科分组输出
    for sub in subjects:
        print(f"\n【{sub}】")
        idx = 1
        for item in error_books:
            if item["subject"] == sub:
                print(f"  {idx}. 题目：{item['question']}")
                print(f"     错因：{item['reason']}")
                print(f"     正解：{item['answer']}")
                idx += 1

def delete_error():
    """根据序号删除错题"""
    if len(error_books) == 0:
        print("\n❌ 暂无错题，无法删除！")
        return
    print("\n----- 删除错题 -----")
    # 先展示全部错题序号
    for i, item in enumerate(error_books):
        print(f"{i+1}.【{item['subject']}】{item['question']}")
    num_str = input("输入要删除错题的序号：")
    if not num_str.isdigit():
        print("❌ 请输入数字！")
        return
    num = int(num_str)
    if num < 1 or num > len(error_books):
        print("❌ 序号超出范围！")
        return
    del error_books[num - 1]
    print("✅ 删除成功！")

# 主循环
while True:
    select = show_menu()
    if select == "1":
        add_error()
    elif select == "2":
        view_error()
    elif select == "3":
        delete_error()
    elif select == "4":
        print("👋 程序退出，再见！")
        break
    else:
        print("❌ 输入无效,请选择1~4!")
        