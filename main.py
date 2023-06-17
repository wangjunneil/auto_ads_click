import pyautogui
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

from switch_proxy import *
from finger_printing import *
from jaskan_com import Jaskan

sys_platform = platform.platform().lower()
################# 常量定义 #################
BROWSER_LOCATION = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
DRIVER_LOCATION = 'D:\SeleniumDriver\chromedriver.exe'
if 'macos' in sys_platform:
    BROWSER_LOCATION = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    DRIVER_LOCATION = '/Users/wangjun/ToolLibrary/selenium_driver/chromedriver_chrome_114.0.5735.106/chromedriver'
###########################################

# 初始化
options = webdriver.ChromeOptions()
options.binary_location = BROWSER_LOCATION
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone 12 Pro"}) # 手机模式
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--headless') # 无界面模式
# options.add_argument("--auto-open-devtools-for-tabs") # 开发者模式

# 随机代理池
# proxy_address = get_proxy_from_pool()
# print(proxy_address)
# options.add_argument(f'--proxy-server=http://{proxy_address}')

# 随机 user-agent
user_agent = get_random_user_agent()
options.add_argument(f'--user-agent={user_agent}')
driver = webdriver.Chrome(service=Service(executable_path=DRIVER_LOCATION), options=options)


def open_website(address: str, jaskan: Jaskan):
    '''
    打开制定地址的站点
    '''
    # 首次使用referer地址打开
    # random_referer = get_random_referer()
    # driver.get(random_referer)
    # driver.maximize_window()

    # 从referer地址跳转到实际地址
    # driver.execute_script(f'window.location.href="{address}"')
    # WebDriverWait(driver, 10).until(lambda driver: driver.current_url == address)

    # 打开地址
    driver.get(address)
    driver.maximize_window()
    

    # 检查title是否404
    jaskan.check_404_refresh(1)

def execute_click(jaskan: Jaskan):
    '''
    执行广告点击
    '''
    # 首页
    jaskan.index()

    # 电视剧
    jaskan.tv()

    # # 电影
    jaskan.movie()  

    # # 随机影视分类
    jaskan.type()

    # # 详情
    jaskan.detail()
    
    # # 播放页面
    jaskan.play()


def check_404_refresh(driver: webdriver, retry: int):
    '''
    检查页面是否404并3次尝试刷新
    '''
    if retry > 3: 
        driver.quit()

    if driver.title == 'Service is not avaliable':
        driver.refresh()
        pyautogui.sleep(15)
        check_404_refresh(driver, retry + 1)


if __name__ == '__main__':
    try:
        # 切换代理
        switch_proxy_order_point()
        
        # 初始化站点对象
        jaskan = Jaskan(driver)

        # 打开站点
        open_website('https://www.jaskan.com', jaskan)
        # open_website('https://api.jaskan.com/myip', jaskan)

        # 执行点击
        execute_click(jaskan)

        pyautogui.sleep(10)
    except Exception as e:
        print(str(e))
    finally:
        # 关闭浏览器
        driver.quit()