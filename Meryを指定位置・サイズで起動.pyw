import subprocess
import win32gui
import pyautogui

subprocess.Popen(r"C:\Users\wrfmf\Downloads\Mery-2.6.7\Mery\Mery.exe")

while True:
	windows = pyautogui.getWindowsWithTitle('Mery')
	if windows:
		window = pyautogui.getWindowsWithTitle('Mery')[0]
		break
	pyautogui.sleep(0.01)

hwnd=window._hWnd

win32gui.MoveWindow(hwnd,513,184,980,749,True)