import tkinter as tk
import win32gui
import pyautogui
import pyperclip
import os

def close_dummy():
	dummy.destroy()
dummy_width=0
dummy_height=0
dummy = tk.Tk()
dummy.geometry(f"{dummy_width}x{dummy_height}+-999+-999")
dummy.after(1, close_dummy)
dummy.mainloop()

pyautogui.sleep(0.1)

while True:
	while True:
		pyautogui.hotkey('shift', 'f10')
		pyautogui.press('a')
		pyautogui.press('a')
		pyautogui.press('enter')

		pyautogui.sleep(0.5)

		full_path = pyperclip.paste()
		
		pyautogui.sleep(0.5)
		
		if full_path:
			break

	full_path = full_path.strip('"')

	if '"' not in full_path:
		break

pyperclip.copy(full_path)