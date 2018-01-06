"""
手机屏幕截图的代码
"""
import subprocess
import os
import sys
from PIL import Image

# SCREENSHOT_WAY 是截图方法，经过 check_screenshot 后，会自动递减，不需手动修改
SCREENSHOT_WAY = 3


def get_screenshot():
    """
    获取屏幕截图，目前有 0 1 2 3 四种方法
    """
    global SCREENSHOT_WAY
    if 1 <= SCREENSHOT_WAY <= 3:
        process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
        binary_screenshot = process.stdout.read()
        if SCREENSHOT_WAY == 2:
            binary_screenshot = binary_screenshot.replace(b'\r\n', b'\n')
        elif SCREENSHOT_WAY == 1:
            binary_screenshot = binary_screenshot.replace(b'\r\r\n', b'\n')
        f = open('seat.png', 'wb')
        f.write(binary_screenshot)
        f.close()
    elif SCREENSHOT_WAY == 0:
        os.system('adb shell screencap -p /sdcard/seat.png')
        os.system('adb pull /sdcard/seat.png .')


def check_screenshot():
    """
    检查获取截图的方式
    """
    global SCREENSHOT_WAY
    if os.path.isfile('seat.png'):
        try:
            os.remove('seat.png')
        except Exception:
            pass
    if SCREENSHOT_WAY < 0:
        print('暂不支持当前设备')
        sys.exit()
    get_screenshot()
    try:
        Image.open('./seat.png').load()
        print('采用方式{}获取截图'.format(SCREENSHOT_WAY))
    except Exception:
        SCREENSHOT_WAY -= 1
        check_screenshot()


def drag_to_bottom():
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
        x1=200,
        y1=800,
        x2=200,
        y2=200,
        duration=120
    )
    print("页面滑动到底部")
    os.system(cmd)


def press_menu_button():
    """
    点击微信右上角菜单键
    """
    press_screen(1050, 70)


def press_refresh_button():
    """
    点击刷新按钮
    """
    press_screen(100, 1700)
    print("刷新页面")


def press_screen(x, y):
    """
    根据 x,y 坐标点击屏幕
    """
    cmd = 'adb shell input tap {x} {y}'.format(x=x, y=y)
    print("adb shell input tap {x} {y}", x, y)
    os.system(cmd)


def press_confirm_button():
    # 点击确认按键
    press_screen(700, 1800)


def press_back_button():
    # 返回上一个页面
    press_screen(70, 135)
