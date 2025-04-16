import tkinter as tk
import pyautogui
import win32gui
import pyperclip
import ctypes
import time
import win32con

def close_window():
    root.destroy()

ウィンドウ幅=0
ウィンドウ高さ=0

"""
desktop_hwnd=win32gui.GetDesktopWindow()
desktop_rect=win32gui.GetWindowRect(desktop_hwnd)
デスクトップ幅=desktop_rect[2]
デスクトップ高さ=desktop_rect[3]

表示位置X=(デスクトップ幅//2)-(ウィンドウ幅//2)
表示位置Y=(デスクトップ高さ//2)-(ウィンドウ高さ//2)
"""

root = tk.Tk()

root.geometry(f"{ウィンドウ幅}x{ウィンドウ高さ}+-999+-999")

root.after(1, close_window)

root.mainloop()