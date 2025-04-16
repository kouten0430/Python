import win32com.client
import win32gui
import pyautogui
import time

shell = win32com.client.Dispatch("WScript.Shell")

shell.Run(fr"C:\Users\wrfmf\Documents\雑庫\py\pyw")

time.sleep(1)

window = pyautogui.getWindowsWithTitle('pyw')[0]

hwnd=window._hWnd

win32gui.MoveWindow(hwnd,-10,0,242,1030,True)