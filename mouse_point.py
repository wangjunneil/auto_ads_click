# 获取当前鼠标坐标的辅助工具，用于模糊定位Ads具体位置

import os,time
import pyautogui as pag
import platform

cmd = 'cls'
sys_platform = platform.platform().lower()
if 'macos' in sys_platform:
	cmd = 'clear'

try:
	while True:
		print ("Press Ctrl-C to end")
		# 返回鼠标的坐标
		x,y = pag.position() 
		posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)

  		# 打印坐标
		print(posStr)
		time.sleep(0.2)

		# 清楚屏幕
		os.system(cmd)  
except KeyboardInterrupt:
		print ('end....') 