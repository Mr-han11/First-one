import card_tool
# 无限循环，由用户用户决定什么时候退出
while True:

    # TODO 显示功能菜单
    card_tool.show_menu()
    action_str = input("请输入希望执行的操作：")
    print("您选择的操作是 【%s】" % action_str)
    # 1，2，3针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            card_tool.new_card()
        # 显示全部
        elif action_str == "2":
            card_tool.show_all()
        # 查询名片
        elif action_str == "3":
            card_tool.search_card()

    elif action_str == "0":
        break
    else:
        print("您输入的不正确，请重新选择")
