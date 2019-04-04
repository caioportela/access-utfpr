import pyautogui as auto
import time

time.sleep(12)
auto.press('winleft')
time.sleep(0.5)
auto.press(['f','i','r','e','f','o','x'], interval=1)
auto.press('enter')
time.sleep(10)
auto.press(['i','n','t','r','a','n','e','t','.','p','b','.','u','t','f','p','r','.','e','d','u','.','b','r'], interval=1)
auto.press('return')
time.sleep(2)
auto.press('return')
time.sleep(2)
auto.hotkey('alt', 'f4')
