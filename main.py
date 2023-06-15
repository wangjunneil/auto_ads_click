import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

################# 常量定义 #################
BROWSER_LOCATION = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
DRIVER_LOCATION = 'D:\SeleniumDriver\chromedriver.exe'
###########################################

# 初始化
options = webdriver.ChromeOptions()
options.binary_location = BROWSER_LOCATION
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--headless') # 无界面模式
# options.add_argument(f'--proxy-server=http://183.221.242.103:9443')
driver = webdriver.Chrome(service=Service(executable_path=DRIVER_LOCATION), options=options)


def ads_click_direct(points):
    '''
    按住ctrl点击给出的x,y坐标
    '''
    for point in points:
        pyautogui.keyDown('ctrl')
        pyautogui.click(point[0], point[1])
        pyautogui.keyUp('ctrl')
        pyautogui.sleep(1)

def open_website(address: str):
    '''
    打开制定地址的站点
    '''
    # 打开地址
    driver.get(address)
    driver.maximize_window()

    # 检查title是否404
    check_404_refresh(driver, 1)

def execute_click():
    '''
    执行广告点击
    '''
    # ..... 站点首页 ..... 
    ads_frame_click()

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

    # ..... 电影页面 ..... 
    # pyautogui.click(882,127)
    driver.execute_script('location.href=https://www.jaskan.com/vodtype/1.html')
    pyautogui.sleep(15)

    ads_frame_click()
    ads_click_direct([(420,595),(773,674),(1057,776)])
    ads_click_direct([(1400, 764),(1400,835),(1400,900)])

    # ..... 搜索页面 ..... 
    pyautogui.click(1529, 124)
    pyautogui.sleep(15)

    ads_frame_click()
    ads_click_direct([(420,595),(773,674),(1057,776)])
    ads_click_direct([(1400, 764),(1400,835),(1400,900)])

    # ..... 详情页面 ..... 

    # ..... 播放页面 ..... 

def check_404_refresh(driver, retry: int):
    '''
    检查页面是否404并3次尝试刷新
    '''
    if retry > 3: 
        driver.quit()

    if driver.title == 'Service is not avaliable':
        driver.refresh()
        pyautogui.sleep(15)
        check_404_refresh(driver, retry + 1)

def ads_frame_click():
    '''
    通用页面级的ad广告位置点击
    '''
    # 点击首页底部广告
    ads_click_direct([(515,940),(881,994),(1349,977)])

    # # 点击首页左侧广告
    ads_click_direct([(185,328),(185,531),(185,782)])

    # # 点击首页右侧广告
    ads_click_direct([(1708,329),(1708,528),(1708,780)])


if __name__ == '__main__':
    # 打开站点
    open_website('https://www.jaskan.com')

    # 执行点击
    # execute_click()

    pyautogui.sleep(30)
    # 关闭浏览器
    driver.quit()