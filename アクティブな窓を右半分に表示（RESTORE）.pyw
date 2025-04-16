import tkinter as tk
import win32gui
import pyautogui
#import pygetwindow as gw
import win32con

def close_dummy():
	dummy.destroy()
dummy_width=0
dummy_height=0
dummy = tk.Tk()
dummy.geometry(f"{dummy_width}x{dummy_height}+-999+-999")
dummy.after(1, close_dummy)
dummy.mainloop()

pyautogui.sleep(0.1)

hwnd = win32gui.GetForegroundWindow()

"""
window_title = win32gui.GetWindowText(hwnd)
window = gw.getWindowsWithTitle(window_title)[0]
window.restore()
"""

win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

win32gui.MoveWindow(hwnd,950,0,980,1030,True)