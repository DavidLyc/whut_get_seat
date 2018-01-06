from tool import screen_tool


def get_empty_floor(im_pixel):
    """
    6个自习室末尾数字的屏幕位置 [995, 540] [995, 750] [995, 960] [995, 1170] [995, 1380] [995, 1590]
    颜色信息
    红  255, 0, 0
    黄  251, 192, 51
    蓝  92, 132, 189
    灰  172, 172, 172
    """
    x = 995
    y_list = [540, 750, 960, 1170, 1380, 1590]
    for y in y_list:
        # 不是红色或灰色即可点击该自习室
        if im_pixel[x, y][0] not in (172, 255):
            screen_tool.press_screen(x, y)
            return True
    print("居然没有座位了...")
    return False


def get_free_seat(im_pixel):
    """
    从屏幕位置 290, 530开始扫描空位
    在 1060, 1670 结束扫描
    每次扫描间隔 8个像素
    空位rgb: 243, 243, 242
    暂时不考虑电脑抢座位抢不过人的情况...
    """
    for y in range(530, 1670, 8):
        for x in range(290, 1060, 8):
            if im_pixel[x, y][0] == 243:
                print('找到空位啦！')
                screen_tool.press_screen(x, y)
                screen_tool.press_confirm_button()
                return True
    print("居然没有座位了...")
    screen_tool.press_back_button()
    return False
