import pyautogui
import time
# from PIL import Image
time.sleep(5)
addButtonImg = pyautogui.screenshot(imageFilename='images/add_button.png', region=(0, 0, 570, 100))
# addButtonImg.save('images/add_button.png')


coords = pyautogui.locateOnScreen('images/add_button.png')
x, y = pyautogui.center(coords)
print(x, y)
