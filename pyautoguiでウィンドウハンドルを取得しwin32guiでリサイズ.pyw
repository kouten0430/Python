import pyautogui
import win32gui

window = pyautogui.getWindowsWithTitle('メモ帳')[0]

hwnd=window._hWnd

win32gui.MoveWindow(hwnd,-10,0,242,1030,True)