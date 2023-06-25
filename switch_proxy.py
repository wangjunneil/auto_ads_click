import random
import pyautogui
import requests
import sys

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
    {'name':'🇹🇷 土耳其', 'point':(1429, 319)},
    {'name':'🇵🇭 菲律宾 20倍消耗流量', 'point':(1429, 319)}
]
#####################################################

def __current_index() -> (int):
    index_file = open(f'{sys.path[0]}/data/nodeindex', 'r')
    current_index = int(index_file.readline())
    index_file.close()
    return current_index

def __write_index(current_index:int):
    PROXYS = __get_valid_proxys()
    
    index_file = open(f'{sys.path[0]}/data/nodeindex', 'w')
    if current_index + 1 == len(PROXYS):
        index_file.write(str(0))
    else:
        last_index = current_index + 1
        index_file.write(str(last_index))
    index_file.close()
    
def __get_valid_proxys() -> (list):
    response = requests.get('http://127.0.0.1:54663/proxies')
    result_json = response.json()
    PROXYS = result_json['proxies']['🚀 手动切换']['all']
    return PROXYS

def switch_proxy_order_point():
    '''
    通过 clash 内部API顺序切换代理
    '''
    # 读取当前索引号
    current_index = __current_index()

    # 获取代理节点名称
    PROXYS = __get_valid_proxys()
    node_name = PROXYS[current_index]
    
    # 检查节点是否可用
    # response = requests.get(f'http://127.0.0.1:54663/proxies/{node_name}/delay?timeout=5000&url=https://www.jaskan.com')
    # if "An error occurred in the delay test" in response.text:
    #     switch_proxy_order_point()

    # 切换本地 clash 代理
    requests.put('http://127.0.0.1:54663/proxies/🚀 节点选择', json={'name':node_name})

    # 写入下一个索引号
    __write_index(current_index)

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

def get_proxy_from_pool() -> str:
    response = requests.get('http://192.168.2.201:5000/get')
    result_json = response.json()
    return result_json['proxy']



# response = requests.get('http://127.0.0.1:54663/proxies')
# result_json = response.json()
# print(result_json['proxies']['🚀 手动切换']['all'])