import ctypes
import win32gui
import time
import pyautogui

"""
pyautogui.press('win') 
pyautogui.press('win') 
"""

user32 = ctypes.WinDLL('user32', use_last_error=True)

user32.keybd_event(0x5B, 0, 0, 0)
time.sleep(0.03) 
user32.keybd_event(0x5B, 0, 2, 0)
time.sleep(0.03) 
user32.keybd_event(0x5B, 0, 0, 0)
time.sleep(0.03) 
user32.keybd_event(0x5B, 0, 2, 0)
time.sleep(0.03) 

hwnd = win32gui.GetForegroundWindow()

win32gui.MoveWindow(hwnd,-10,0,242,1030,True)