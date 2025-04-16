import subprocess
import win32gui
import pyautogui

subprocess.Popen("cmd.exe", cwd=r"C:\Users\wrfmf")

while True:
	windows = pyautogui.getWindowsWithTitle('cmd.exe')
	if windows:
		window = pyautogui.getWindowsWithTitle('cmd.exe')[0]
		break
	pyautogui.sleep(0.01)

hwnd=window._hWnd

win32gui.MoveWindow(hwnd,-10,0,980,1030,True)