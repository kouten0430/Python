import win32com.client
import pyautogui
import time

shell = win32com.client.Dispatch("Shell.Application")

shell.ShellExecute("microsoft-edge:https://colab.research.google.com")

while True:
	try:
		location=pyautogui.locateCenterOnScreen("kouten.png",confidence=0.9)
		break
	except:
		pass
x,y=location
pyautogui.leftClick(x,y)
pyautogui.leftClick(x,y)

while True:
	try:
		location=pyautogui.locateCenterOnScreen("kaine.png",confidence=0.9)
		break
	except:
		pass
x,y=location
pyautogui.leftClick(x,y)

while True:
	try:
		location=pyautogui.locateCenterOnScreen("googledrive.png",confidence=0.9)
		break
	except:
		pass
x,y=location
pyautogui.leftClick(x+50,y)