import pyautogui as auto
import time

x, y = 723, 693
time.sleep(10)
auto.press('winleft')
time.sleep(0.5)
auto.press(['f','i','r','e','f','o','x'], interval=1)
auto.press('enter')
time.sleep(7)
auto.press(['i','n','t','r','a','n','e','t','.','p','b','.','u','t','f','p','r','.','e','d','u','.','b','r'], interval=1)
auto.press('return')
time.sleep(2.5)
auto.moveTo(x, y, 0.2)
time.sleep(1)
auto.click()
time.sleep(1)
auto.hotkey('alt', 'f4')
