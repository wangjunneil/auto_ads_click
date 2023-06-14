
# 自动化点击 www.jaskan.com 站点的 Google Ads广告

import pyautogui

def ads_click_direct(points):
    '''
    按住ctrl点击给出的x,y坐标
    '''
    for point in points:
        pyautogui.keyDown('ctrl')
        pyautogui.click(point[0], point[1])
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

    # 输入命令，打开浏览器
    # pyautogui.press('brave')
    # pyautogui.press(f'brave {website}')
    pyautogui.typewrite(f'brave  {website}')
    pyautogui.press('enter')
    pyautogui.press('enter')
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
    ads_click_direct([(1898,12)])

def execute_click_ads():
    '''
    执行广告点击
    '''
    # 点击首页底部广告
    ads_click_direct([(515,940),(881,994),(1349,977)])

    # # 点击首页左侧广告
    ads_click_direct([(185,328),(185,531),(185,782)])

    # # 点击首页右侧广告
    ads_click_direct([(1708,329),(1708,528),(1708,780)])

    # 滑动浏览器滚动条
    pyautogui.click(1910,194)
    pyautogui.dragTo(1910,438, 2)
    ads_click_direct([(415,258),(934,340),(1336,428)])
    pyautogui.sleep(1)

    pyautogui.click(1910,438)
    pyautogui.dragTo(1910,561, 2)
    ads_click_direct([(444,367),(932,472),(1331, 456)])
    pyautogui.sleep(1)

    pyautogui.click(1910,561)
    pyautogui.dragTo(1910,705, 2)
    ads_click_direct([(412,265),(942,386),(1450,387)])
    pyautogui.sleep(1)

    # 搜索页面
    pyautogui.click(1529, 124)
    pyautogui.sleep(15)
    
    # 点击底部广告
    ads_click_direct([(515,940),(881,994),(1349,977)])

    # 点击首页左侧广告
    ads_click_direct([(185,328),(185,531),(185,782)])

    # 点击首页右侧广告
    ads_click_direct([(1708,329),(1708,528),(1708,780)])
    
    # 内容广告
    ads_click_direct([(420,595),(773,674),(1057,776)])
    
    # 侧栏广告
    ads_click_direct([(1400, 764),(1400,835),(1400,900)])
    
    
    # 电影分类
    pyautogui.click(882,127)
    pyautogui.sleep(15)
    
    # 点击底部广告
    ads_click_direct([(515,940),(881,994),(1349,977)])

    # 点击首页左侧广告
    ads_click_direct([(185,328),(185,531),(185,782)])

    # 点击首页右侧广告
    ads_click_direct([(1708,329),(1708,528),(1708,780)])
    
    # 内容广告
    pyautogui.click(1910,152)
    pyautogui.dragTo(1910,229, 2)
    ads_click_direct([(526,238),(1411,338),(629,627),(1495,586)])
    pyautogui.sleep(1)
    
    # 内容广告
    pyautogui.click(1910,228)
    pyautogui.dragTo(1910,398, 2)
    ads_click_direct([(476,264),(1411,429),(606,543),(1290,700)])
    pyautogui.sleep(1)
    
    
    # 搜索页面
    pyautogui.click(1426, 124)
    pyautogui.sleep(15)
    
    # 点击底部广告
    ads_click_direct([(515,940),(881,994),(1349,977)])

    # 点击首页左侧广告
    ads_click_direct([(185,328),(185,531),(185,782)])

    # 点击首页右侧广告
    ads_click_direct([(1708,329),(1708,528),(1708,780)])
    
    # 内容广告
    ads_click_direct([(420,595),(773,674),(1057,776)])
    
    # 侧栏广告
    ads_click_direct([(1400, 764),(1400,835),(1400,900)])


if __name__ == '__main__':
    import clash

    # 打开浏览器
    open_jaskan_com('https://www.jaskan.com')

    # 点击广告
    execute_click_ads()

    # 关闭浏览器
    close_jaskan_com()