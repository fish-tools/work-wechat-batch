# 企微自动批量添加好友
> 本工具仅作为python代码学习之用，非法使用，作者不承担任何法律责任
## 前提
> 1.安装python3.0运行环境  
> 2.安装并登陆了企业微信

## 运行workWechatMain.py
程序主入口，执行程序，会自动操作打开微信，执行好友搜索，并添加好友。
```$xslt
# 启动搜索好友界面
start()

# 以下步骤可以循环输入参数执行
# memo='我是自定义请求备注，请加我好友吧'
foreach(mobile='137267598xx')
```

## 配置config.py
```$xslt
# 替换你的winodws企业微信安装目录，其他操作系统不管
workWechatOfwinPath = 'C:\\Programs\\企业微信.exe'
# 替换你的Mac企业微信安装目录，其他操作系统不管
workWechatOfMacPath = '/Applications/企业微信.app'
# 替换linux下的企业微信安装目录
workWechatOfLinuxPath = None

# locateOnScreen定位的坐标系数，需要除以此系数，得到屏幕的精确位置
locateRate = 2

# 每步操作的时间间隔s
clickInterval = 0.2
# 启动应用后间隔多久开始操作s
opInterval = 2
```


## 截图
>截图需要使用系统自带工具截图  
window下是win+print screen sysrq 
mac 下是 shift+cmd+4 截图   

工具的实现原理，是根据企微添加好友的顺序，模拟用户操作点击实现  
因此首先需要运行环境下企微新的截图，否则会因为执行环境分辨率的  
不同导致点击位置不正确，功能异常。

mac运行环境下的截图存放位置  
/images/workwechat/mac/addfriends

windows运行环境下的截图存放位置  
/images/workwechat/win/addfriends

linux运行环境下的截图存放位置  
/images/workwechat/linux/addfriends

**截图命名**
```$xslt

'''
操作按钮的位置截图文件名称
'''
# 组织架构未点击状态按钮截图
organizationButton = 'organization_button.png'
# 组织架构已点击状态按钮截图
organizationButton2 = 'organization_button_2.png'
# 新的联系人截图
newContactButton = 'new_contact_button.png'
# 添加按钮截图
addButton = 'add_button.png'
# 手机输入款截图
mobileInput = 'mobile_input.png'
# 添加好友按钮截图
addFriendButton = 'add_friend_button.png'
# 未找到好友联系人的确定按钮截图
notFoundFriendButton = 'no_found_friend_back_button.png'
# 清空手机输入框内容按钮截图
clearMobileInputButton = 'clear_mobile_input_button.png'
# 已经添加好友截图
alreadyAdded = 'already_added.png'
# 已经发送请求加好友截图
alreadySentRequest = 'already_sent_request.png'
# 清空加好哟备注信息截图
clearMemoInputButton = 'clear_memo_input_button.png'
# 发送好友按钮截图
sendFriendRequestButton = 'send_friend_request_button.png'

```

**联系作者**  
加微信交流：ToryLoveFish
