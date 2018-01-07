from tool import screen_tool
from run import get_seat_auto
import time


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
    y_list = [540, 960, 1170, 1380, 1590]
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
    每次扫描间隔 9个像素
    空位rgb: 243, 243, 242
    """
    for y in range(530, 1670, 9):
        for x in range(290, 1060, 9):
            if im_pixel[x, y][0] == 243 \
                    and im_pixel[x, y][1] == 243 \
                    and im_pixel[x, y][2] == 242:
                screen_tool.press_screen(x, y)
                screen_tool.press_confirm_button()
                # 休眠 0.3s 判断抢座是否成功
                time.sleep(0.3)
                im_pixel = get_seat_auto.get_image_pixel()
                if im_pixel[x, y][0] not in range(180, 230):
                    print('找到空位啦！')
                    return True
    print("居然没有座位了...")
    screen_tool.press_back_button()
    return False
