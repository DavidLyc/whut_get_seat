from PIL import Image
from tool import screen_tool, image_tool
import time


def yes_or_no(prompt, true_value='y', false_value='n', default=True):
    # 检查是否已经为启动程序做好了准备
    default_value = true_value if default else false_value
    prompt = '{} {}/{} [{}]: '.format(prompt, true_value, false_value, default_value)
    i = input(prompt)
    if not i:
        return default
    while True:
        if i == true_value:
            return True
        elif i == false_value:
            return False
        prompt = 'Please input {} or {}: '.format(true_value, false_value)
        i = input(prompt)


def get_image_pixel():
    # 获得截屏像素
    screen_tool.get_screenshot()
    image = Image.open('./seat.png')
    im_pixel = image.load()
    return im_pixel


def main():
    op = yes_or_no('请确保手机已打开ADB并连接了电脑，然后打开我去图书馆微信端网页再使用本程序，确定开始？')
    if not op:
        print('bye')
        return
    screen_tool.check_screenshot()
    while True:
        screen_tool.drag_to_bottom()
        screen_tool.press_menu_button()
        screen_tool.press_refresh_button()
        # 休眠 0.3s 确保页面刷新完成
        time.sleep(0.3)
        # 找到没有满座的教室并点击
        if image_tool.get_empty_floor(get_image_pixel()):
            time.sleep(0.6)
            # 找到空位并点击，成功后退出程序
            if image_tool.get_free_seat(get_image_pixel()):
                return


if __name__ == '__main__':
    main()
