import random
import pyautogui

# 点击托盘
pyautogui.click(1721,1059)
# 点击clash
pyautogui.rightClick(1745, 1020)
pyautogui.sleep(1)
pyautogui.click(1817,724)
pyautogui.sleep(2)

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

random_point = random.randrange(0, 9)
pyautogui.click(proxy_point[random_point][0], proxy_point[random_point][1])
pyautogui.sleep(1)

pyautogui.click(1902, 19)
pyautogui.sleep(10)