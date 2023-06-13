
# 自动化点击 www.jaskan.com 站点的 Google Ads广告

import pyautogui

def ads_click_direct(x:int, y:int):
    '''
    按住ctrl点击给出的x,y坐标
    '''
    pyautogui.keyDown('ctrl')
    pyautogui.click(x, y)
    pyautogui.keyUp('ctrl')

    pyautogui.sleep(2)

def open_jaskan_com(website: str):
    '''
    运行浏览器，输入网址并打开
    '''
    # 模拟按下 Win+R 键
    pyautogui.hotkey('win', 'r')

    # 等待运行面板打开
    pyautogui.sleep(1)

    # 输入命令，打开浏览器 TODO 直接在打开网址
    # pyautogui.press('brave')
    pyautogui.press(f'brave {website}')
    pyautogui.sleep(0.5)

    # # 模拟按下回车键
    # pyautogui.press('enter')

    # # 等待浏览器打开
    # pyautogui.sleep(2)

    # # 输入网址
    # pyautogui.typewrite(website)
    # pyautogui.press('enter')
    # pyautogui.sleep(1)
    # pyautogui.press('enter')

    # 等待30秒网页加载
    pyautogui.sleep(30)

def close_jaskan_com():
    '''
    关闭浏览器
    '''
    pyautogui.sleep(10)
    ads_click_direct(1898,12)

def execute_click_ads():
    '''
    执行广告点击
    '''
    # 点击首页底部广告
    ads_click_direct(671, 970)

    # 点击首页左侧广告
    ads_click_direct(189, 408)

    # 点击首页右侧广告
    ads_click_direct(1704, 381)

    # TODO pyautogui.scroll(-10) 向下滑动
    # 滑动浏览器滚动条
    pyautogui.click(1910,186)
    pyautogui.dragTo(1910,433, 2)
    ads_click_direct(569,255)
    ads_click_direct(1322,254)
    ads_click_direct(565,403)
    ads_click_direct(1322,413)
    pyautogui.sleep(1)

    pyautogui.click(1910,433)
    pyautogui.dragTo(1910,571, 2)
    ads_click_direct(438,288)
    ads_click_direct(438,449)
    ads_click_direct(1468,276)
    ads_click_direct(1468,465)
    pyautogui.sleep(1)

    pyautogui.click(1910,571)
    pyautogui.dragTo(1910,704, 2)
    ads_click_direct(429,178)
    ads_click_direct(429,341)
    ads_click_direct(1472,185)
    ads_click_direct(1472,368)
    pyautogui.sleep(1)

    # 搜索页面
    pyautogui.click(1263, 125)
    pyautogui.sleep(15)

    ads_click_direct(596,377)
    ads_click_direct(404,559)
    ads_click_direct(1114,370)
    ads_click_direct(969,548)
    ads_click_direct(1395, 763)
    ads_click_direct(1390, 751)
    ads_click_direct(861, 941)


if __name__ == '__main__':
    import clash

    # 打开浏览器
    open_jaskan_com('https://www.jaskan.com')

    # 点击广告
    execute_click_ads()

    # 关闭浏览器
    close_jaskan_com()