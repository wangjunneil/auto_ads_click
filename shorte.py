import pyautogui

# skip_ad_img = pyautogui.locateOnScreen('img/shorte_skip_ad.png')
# if not skip_ad_img:
#     pyautogui.click(skip_ad_img)

pyautogui.click('img/shorte_skip_ad.png')


if not pyautogui.click(300,300):
    print('success')
else:
    print('failure')
