
# 自动化点击 www.jaskan.com 站点的 Google Ads广告

import pyautogui
import proxy

# 广告坐标定义
ADS = {
    'FOOTER': [671, 970],
    'LEFT': [189, 408],
    'RIGHT': [1704, 381],
    'INNER': [
        {'scroll_from': [1910,186], 'scroll_to': [1910,433],'XY': [967,306]},
        {'scroll_from': [1910,433], 'scroll_to': [1910,571],'XY': [967,306]},
        {'scroll_from': [1910,571], 'scroll_to': [1910,704],'XY': [967,265]},
        {'scroll_from': [1910,704], 'scroll_to': [1910,831],'XY': [967,312]}
    ]
}


def ads_click_direct(point):
    """
    点击给出的坐标位置
    Args:
        points (_type_): _description_
    """
    pyautogui.keyDown('ctrl')
    pyautogui.click(point[0], point[1])
    pyautogui.keyUp('ctrl')

    pyautogui.sleep(2)

# 模拟按下 Win+R 键
pyautogui.hotkey('win', 'r')

# 等待运行面板打开
pyautogui.sleep(1)

# 输入命令，打开浏览器
pyautogui.press('brave')
pyautogui.sleep(0.5)

# 模拟按下回车键
pyautogui.press('enter')

# 等待浏览器打开
pyautogui.sleep(1)

# 输入网址
pyautogui.typewrite('https://www.jaskan.com')
pyautogui.press('enter')
pyautogui.press('enter')

# 等待网页加载
pyautogui.sleep(30)


# # 点击首页底部广告
ads_click_direct(ADS['FOOTER'])

# # 点击首页左侧广告
ads_click_direct(ADS['LEFT'])

# # 点击首页右侧广告
ads_click_direct(ADS['RIGHT'])

# # 滑动浏览器滚动条
pyautogui.click(1910,186)
pyautogui.dragTo(1910,433, 3)
ads_click_direct((569,255))
ads_click_direct((1322,254))
ads_click_direct((565,403))
ads_click_direct((1322,413))
pyautogui.sleep(1)

pyautogui.click(1910,433)
pyautogui.dragTo(1910,571, 3)
ads_click_direct((438,288))
ads_click_direct((438,449))
ads_click_direct((1468,276))
ads_click_direct((1468,465))
pyautogui.sleep(1)

pyautogui.click(1910,571)
pyautogui.dragTo(1910,704, 3)
ads_click_direct((429,178))
ads_click_direct((429,341))
ads_click_direct((1472,185))
ads_click_direct((1472,368))
pyautogui.sleep(1)

# 搜索页面
pyautogui.click(1263, 125)
pyautogui.sleep(15)

ads_click_direct((596,377))
ads_click_direct((404,559))
ads_click_direct((1114,370))
ads_click_direct((969,548))
ads_click_direct((1395, 763))
ads_click_direct((1390, 751))
ads_click_direct((861, 941))

# # 关闭浏览器
pyautogui.sleep(10)
ads_click_direct((1898,12))