import tkinter as tk
import pyautogui
import win32gui
import pyperclip

def close_window():
	dummy.destroy()

dummy_window_width=0
dummy_window_height=0

dummy = tk.Tk()

dummy.geometry(f"{dummy_window_width}x{dummy_window_height}+-999+-999")

dummy.after(1, close_window)

dummy.mainloop()

hwnd = win32gui.GetForegroundWindow()

rect=win32gui.GetWindowRect(hwnd)

pyperclip.copy(fr"{rect[0]},{rect[1]},{rect[2]-rect[0]},{rect[3]-rect[1]}")

ウィンドウ幅=200
ウィンドウ高さ=30

desktop_hwnd=win32gui.GetDesktopWindow()
desktop_rect=win32gui.GetWindowRect(desktop_hwnd)
デスクトップ幅=desktop_rect[2]
デスクトップ高さ=desktop_rect[3]

表示位置X=(デスクトップ幅//2)-(ウィンドウ幅//2)
表示位置Y=(デスクトップ高さ//2)-(ウィンドウ高さ//2)

root = tk.Tk()

root.geometry(f"{ウィンドウ幅}x{ウィンドウ高さ}+{表示位置X}+{表示位置Y}")

label = tk.Label(root, text=fr"{rect[0]}　{rect[1]}　{rect[2]-rect[0]}　{rect[3]-rect[1]}")
label.pack()

root.mainloop()