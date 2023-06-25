import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

class Jaskan:
    
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def index(self):        
        self.__ads_frame_click()

        pyautogui.click(1910,250)
        pyautogui.dragTo(1910,530, 2)
        self.__ads_click_direct([(417,206),(815,274),(1472,387)])
        pyautogui.sleep(1)

        # pyautogui.click(1910,502)
        # pyautogui.dragTo(1910,632, 2)
        # self.__ads_click_direct([(464,271),(909,276),(1413, 286)])
        # pyautogui.sleep(1)

        # pyautogui.click(1910,632)
        # pyautogui.dragTo(1910,764, 2)
        # self.__ads_click_direct([(533,314),(993,260),(1453,414)])
        # pyautogui.sleep(1)

    def tv(self) -> None:
        self.driver.execute_script('window.location.href="https://www.jaskan.com"')
        self.driver.find_element(By.LINK_TEXT, '电视剧').click()
        self.check_404_refresh(1)
        self.__vignette()

        # 页面广告点击
        pyautogui.sleep(3)
        self.__ads_frame_click()

    def movie(self) -> None:
        self.driver.execute_script('window.location.href="https://www.jaskan.com"')
        self.driver.find_element(By.LINK_TEXT, '电影').click()
        self.check_404_refresh(1)
        self.__vignette()

        # 页面广告点击
        pyautogui.sleep(3)
        self.__ads_frame_click()

    def type(self) -> None:
        self.driver.execute_script('window.location.href="https://www.jaskan.com"')
        VOD_TYPES = ['动作','科幻','恐怖','灾难','战争','犯罪','爱情','喜剧','剧情','悬疑','动漫']
        random_index = random.randrange(0, 10)
        self.driver.find_element(By.LINK_TEXT, VOD_TYPES[random_index]).click()
        self.check_404_refresh(1)
        self.__vignette()

        # 页面广告点击
        pyautogui.sleep(3)
        self.__ads_frame_click()

    def detail(self) -> None:
        items = self.driver.find_elements(By.CLASS_NAME, 'vodlist_item')
        random_index = random.randrange(0, len(items))
        items[random_index].click()
        self.check_404_refresh(1)
        self.__vignette()

        # 页面广告点击
        self.__ads_frame_click()

    def play(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, '.playbtn.o_play').click()
        self.check_404_refresh(1)
        self.__vignette()

        # 页面广告点击
        self.__ads_frame_click()

    def check_404_refresh(self, retry: int) -> None:
        '''
        检查页面是否404并3次尝试刷新
        '''
        if retry > 3: 
            self.driver.quit()

        if self.driver.title == 'Service is not avaliable':
            self.driver.refresh()
            pyautogui.sleep(15)
            self.check_404_refresh(retry + 1)

    # ==============================

    def __vignette(self):
        '''
        中转页
        '''
        # 若是中转页
        if 'google_vignette' in self.driver.current_url:
            # 中间位置广告点击
            # ads_click_direct()
            
            # 点击中转页右上角让其进入正常页面
            pyautogui.click(1389, 129)
            pyautogui.sleep(10)

    def __ads_click_direct(self,points):
        '''
        按住ctrl点击给出的x,y坐标
        '''
        for point in points:
            pyautogui.keyDown('ctrl')
            # pyautogui.keyDown('command')
            pyautogui.click(point[0], point[1])
            pyautogui.keyUp('ctrl')
            # pyautogui.keyUp('command')
            pyautogui.sleep(1)

    def __ads_frame_click(self):
        '''
        通用页面级的ad广告位置点击
        '''
        # 点击首页底部广告
        self.__ads_click_direct([(515,940),(881,994),(1349,977)])

        screenWidth, screenHeight = pyautogui.size()
        if screenWidth > 1440:
            # 点击首页左侧广告
            self.__ads_click_direct([(185,328),(185,531),(185,782)])

            # 点击首页右侧广告
            self.__ads_click_direct([(1708,329),(1708,528),(1708,780)])    