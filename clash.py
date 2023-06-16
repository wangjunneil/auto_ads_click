# 自动化切换代理的操作

import random
import pyautogui

# 点击托盘
pyautogui.click(1683,1059)

# 右击 clash 图标，弹出菜单
pyautogui.rightClick(1684, 982)
pyautogui.sleep(1)

# 选中控制面板，打开
pyautogui.click(1764,680)
pyautogui.sleep(2)

# 控制面板上手动代理的坐标
proxy_point = [
    (1429, 319),
    (1429, 382),
    (1429, 445),
    (1429, 504),
    (1429, 565),
    (1729, 251),
    (1729, 319),
    (1729, 381),
    (1729, 441),
    (1729, 505)
]

# 随机选择代理坐标点击
random_point = random.randrange(0, 9)
pyautogui.click(proxy_point[random_point][0], proxy_point[random_point][1])
pyautogui.sleep(1)

# 关闭窗口
pyautogui.click(1902, 19)
pyautogui.sleep(10)