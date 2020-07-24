import pyautogui
from openApp import call
from locateAndClick import locateAndClick
from config import workWechatOfwinPath, workWechatOfMacPath, workWechatOfLinuxPath, clickInterval
import time
import platform

'''
操作按钮的位置截图文件名称
'''

organizationButton = 'organization_button.png'
organizationButton2 = 'organization_button_2.png'
newContactButton = 'new_contact_button.png'
addButton = 'add_button.png'
mobileInput = 'mobile_input.png'
addFriendButton = 'add_friend_button.png'
notFoundFriendButton = 'no_found_friend_back_button.png'
clearMobileInputButton = 'clear_mobile_input_button.png'
alreadyAdded = 'already_added.png'
alreadySentRequest = 'already_sent_request.png'
clearMemoInputButton = 'clear_memo_input_button.png'
sendFriendRequestButton = 'send_friend_request_button.png'

'''
根据操作系统获取对应的图片
'''


def getLocateImg(fileName=None):
    if fileName is None:
        return None

    if platform.system() == 'Windows':
        return 'images/workwechat/win/addfriends/{}'.format(fileName)
    elif platform.system() == 'Linux':
        return 'images/workwechat/linux/addfriends/{}'.format(fileName)
    elif platform.system() == 'Darwin':
        return 'images/workwechat/mac/addfriends/{}'.format(fileName)
    else:
        print('not support current system' + platform.system())
        exit(0)


def start():
    call(window=workWechatOfwinPath, mac=workWechatOfMacPath, linux=workWechatOfLinuxPath)

    # 第一：点击组织结构按钮
    locateAndClick(clickBound1=getLocateImg(organizationButton), clickBound2=getLocateImg(organizationButton2))

    # 第二：点击添加新联系人按钮
    locateAndClick(clickBound1=getLocateImg(newContactButton))

    # 第三：点击添加按钮
    locateAndClick(clickBound1=getLocateImg(addButton))


def inputMobile(mobile=None):
    # 第四：点击手机号码输入框
    ok = locateAndClick(clickBound1=getLocateImg(clearMobileInputButton))
    if not ok:
        ok = locateAndClick(clickBound1=getLocateImg(mobileInput))
    if not ok:
        return

    # 第五：输入手机号码
    pyautogui.typewrite(message=mobile, interval=0.1)
    time.sleep(len(mobile)*0.1 + 0.5)


'''
搜索好友并检查状态
NET_WORK_ERROR  网络错误
IS_FRIEND 已经添加好友
CAN_ADD_FRIEND 可以添加好友
NOT_FOUND_FRIEND 未查找到联系人
ALREADY_SENT_REQUEST 已经发生过请求
'''


def search():
    # 第六：回车搜索
    pyautogui.press('enter')

    # 第七：等待查询结果，为了防止网络异常，重试2次
    time.sleep(1)
    okAddButton = pyautogui.locateOnScreen(getLocateImg(addFriendButton))
    okAlreadFriend = pyautogui.locateOnScreen(getLocateImg(alreadyAdded))
    okNotFound = pyautogui.locateOnScreen(getLocateImg(notFoundFriendButton))
    okAlreadySentRequest = pyautogui.locateOnScreen(getLocateImg(alreadySentRequest))
    print('okAddButton=', okAddButton, 'okAlreadFriend=', okAlreadFriend, 'okNotFound=',
          okNotFound, 'okAlreadySentRequest=', okAlreadySentRequest)
    # 第一次不OK，等待查询3s再试试
    if okAddButton is None and okAlreadFriend is None and okNotFound is None and okAlreadySentRequest is None:
        time.sleep(3)
        okAddButton = pyautogui.locateOnScreen(getLocateImg(addFriendButton))
        okAlreadFriend = pyautogui.locateOnScreen(getLocateImg(alreadyAdded))
        okNotFound = pyautogui.locateOnScreen(getLocateImg(notFoundFriendButton))

    # 3种状态还查询不到，则返回网络错误处理
    if okAddButton is None and okAlreadFriend is None and okNotFound is None and okAlreadySentRequest is None:
        return 'NET_WORK_ERROR'

    if okAlreadFriend is not None:
        return 'IS_FRIEND'
    if okAddButton is not None:
        return 'CAN_ADD_FRIEND'
    if okNotFound is not None:
        return 'NOT_FOUND_FRIEND'
    if okAlreadySentRequest is not None:
        return 'ALREADY_SENT_REQUEST'


def handleSearchResult(result=None):
    print('handleSearchResult result', result)
    if result is None:
        return
    # 清除
    if result == 'NET_WORK_ERROR' \
            or result == 'IS_FRIEND' \
            or result == 'ALREADY_SENT_REQUEST':
        locateAndClick(clickBound1=getLocateImg(clearMobileInputButton))

    if result == 'NOT_FOUND_FRIEND':
        locateAndClick(clickBound1=getLocateImg(notFoundFriendButton))

    # 弹出添加好友发送请求界面
    if result == 'CAN_ADD_FRIEND':
        locateAndClick(clickBound1=getLocateImg(addFriendButton))
        time.sleep(clickInterval)


'''
发送加好友请求
'''


def sendAddFriendRequest(memo):
    okClearMemoInputButton = pyautogui.locateOnScreen(getLocateImg(clearMemoInputButton))
    okSendFriendRequestButton = pyautogui.locateOnScreen(getLocateImg(sendFriendRequestButton))
    print('sendAddFriendRequest ', 'okClearMemoInputButton=', okClearMemoInputButton,
          'okSendFriendRequestButton=', okSendFriendRequestButton, 'memo=', memo)
    # 输入加好友备注，并发送请求
    if okClearMemoInputButton is not None and okSendFriendRequestButton is not None:
        # 自定义备注，则先清理备注内容，再输入
        if memo is not None:
            locateAndClick(clickBound1=getLocateImg(clearMemoInputButton))
            time.sleep(clickInterval)
            # 输入新的备注
            pyautogui.typewrite(message=memo, interval=0.1)
            sleepSec = len(memo) * 0.1 + 0.5
            time.sleep(sleepSec)
        # 发送添加好友请求
        locateAndClick(clickBound1=getLocateImg(sendFriendRequestButton))
        return True

    return False


# 以下步骤可以循环输入参数执行
def foreach(mobile=None, memo=None):
    # 输入手机号码
    inputMobile(mobile=mobile)
    # 搜索
    searchResult = search()
    # 处理搜索结果
    handleSearchResult(result=searchResult)
    # 发送加好友请求
    sendAddFriendRequest(memo=memo)
