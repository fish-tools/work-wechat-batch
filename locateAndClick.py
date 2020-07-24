import pyautogui
import time
from config import locateRate, clickInterval


def locateAndClick(clickBound1, clickBound2=None):
    coord = pyautogui.locateOnScreen(clickBound1)
    if coord is None and clickBound2 is not None:
        coord = pyautogui.locateOnScreen(clickBound2)
    if coord is None:
        return False

    x, y = pyautogui.center(coord)
    # print('原始坐标->', x, y)
    # 除以2得到正确的坐标，目前还不清楚为什么，反正这样能行。 不同屏幕可能要做测试调整
    pyautogui.click(x / locateRate, y / locateRate)
    time.sleep(clickInterval)
    return True
