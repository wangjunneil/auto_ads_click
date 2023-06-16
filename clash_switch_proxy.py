import random
import pyautogui
import requests

###################### 常量定义 ######################
CLASH_NODE_DATA = [
    {'name':'🇭🇰  香港', 'point':(1429, 319)},
    {'name':'🇭🇰  香港I', 'point':(1429, 382)},
    {'name':'🇹🇼  台湾', 'point':(1429, 319)},
    {'name':'🇹🇼  台湾I', 'point':(1429, 319)},
    {'name':'🇺🇸  美国', 'point':(1429, 319)},
    {'name':'🇺🇸  美国I', 'point':(1429, 319)},
    {'name':'🇸🇬  新加坡', 'point':(1429, 319)},
    {'name':'🇸🇬  新加坡I', 'point':(1429, 319)},
    {'name':'🇯🇵  日本', 'point':(1429, 319)},
    {'name':'🇯🇵  日本I', 'point':(1429, 319)},
    {'name':'🇲🇾 马来西亚', 'point':(1429, 319)},
    {'name':'🇮🇳 印度', 'point':(1429, 319)},
    {'name':'🇰🇷 韩国', 'point':(1429, 319)},
    {'name':'🇬🇧 英国', 'point':(1429, 319)},
    {'name':'🇦🇺 澳大利亚', 'point':(1429, 319)},
    {'name':'🇨🇦 加拿大', 'point':(1429, 319)},
    {'name':'🇦🇷 阿根廷', 'point':(1429, 319)},
    {'name':'🇵🇭 菲律宾 20倍消耗流量', 'point':(1429, 319)}
]
DEFAULT_NODE_ORDER = 0
#####################################################

def switch_proxy_order_point():
    '''
    通过 clash 内部API顺序切换代理
    '''
    node = CLASH_NODE_DATA[DEFAULT_NODE_ORDER]

    if DEFAULT_NODE_ORDER + 1 > 18:
        DEFAULT_NODE_ORDER = 0    

def switch_proxy_random_point():
    '''
    通过 pyautogui 坐标的方式切随机换代理
    '''
    # 点击托盘
    pyautogui.click(1683,1059)
    
    # 右击 clash 图标，弹出菜单
    pyautogui.rightClick(1684, 982)
    pyautogui.sleep(1)

    # 选中控制面板，打开
    pyautogui.click(1764,680)
    pyautogui.sleep(1)

    # 随机节点
    random_index = random.randrange(0, 9)
    random_node = CLASH_NODE_DATA[random_index]
    node_point = random_node['point']

    # 随机选择代理坐标点击
    pyautogui.click(node_point[0], node_point[1])
    pyautogui.sleep(1)

    # 关闭窗口
    pyautogui.click(1902, 19)
    pyautogui.sleep(10)