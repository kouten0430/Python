import tkinter as tk
import win32gui
import pyautogui

def close_dummy():
	dummy.destroy()
dummy_width=0
dummy_height=0
dummy = tk.Tk()
dummy.geometry(f"{dummy_width}x{dummy_height}+-999+-999")
dummy.after(1, close_dummy)
dummy.mainloop()

hwnd = win32gui.GetForegroundWindow()

win32gui.MoveWindow(hwnd,-10,0,242,1030,True)