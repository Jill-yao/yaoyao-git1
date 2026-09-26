import schedule 
import time
import winsound
import win32api
import win32con

def  baby_remind():
    winsound.Beep(800, 300)
    time.sleep(0.2)
    winsound.Beep(1000,300)
    time.sleep(0.2)
    winsound.Beep(1200, 400)

    win32api.MessageBox(0,"5分钟时间到!","宝宝定时提醒",win32con.MB_OK |win32con.MB_TOPMOST)
    print("提醒弹窗弹出",time.ctime())

schedule.every(5).minutes.do(baby_remind)

print("宝宝闹钟启动!每5分值弹窗+响铃,不要关闭终端窗口,Ctrl+C退出")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\n定时器已停止")

