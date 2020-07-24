import platform
import subprocess
from config import opInterval
import time


def call(window=None, mac=None, linux=None):
    print(platform.system())
    if platform.system() == 'Windows' and window is not None:
        subprocess.Popen(window)
    elif platform.system() == 'Linux' and linux is not None:
        print('not support current system' + platform.system())
        exit(0)
    elif platform.system() == 'Darwin' and mac is not None:
        print('Mac系统')
        # 调起企业微信
        subprocess.call(['/usr/bin/open', mac])
    else:
        print('not support current system' + platform.system())
        exit(0)
    time.sleep(opInterval)
