import tkinter
import win32gui
import pyautogui
import pyperclip
import os

def close_dummy():
	global radio_selection
	radio_selection=var.get()
	dummy.destroy()
dummy_width=300
dummy_height=480
x=1920//2-dummy_width//2
y=1080//2-dummy_height//2
dummy =  tkinter.Tk()
dummy.title("")
#dummy.iconbitmap("icon.ico")
dummy.geometry(f"{dummy_width}x{dummy_height}+{x}+{y}")
var = tkinter.IntVar(value=1)
photo = tkinter.PhotoImage(file="image.png")
label1 = tkinter.Label(dummy, image=photo)
label2 = tkinter.Label(dummy, text="ファイル名を取得します", font=("メイリオ", 9,"bold"), fg="DarkViolet")
radiobutton1 = tkinter.Radiobutton(dummy, text="実行ファイル以外",font=("メイリオ", 10), variable=var, value=1)
radiobutton2 = tkinter.Radiobutton(dummy, text="実行ファイル　　",font=("メイリオ", 10), variable=var, value=2)
radiobutton3 = tkinter.Radiobutton(dummy, text="キャンセル　　　",font=("メイリオ", 10), variable=var, value=3)
button = tkinter.Button(dummy, text="　　決定　　", command=close_dummy, bg="DarkGray",font=("メイリオ", 8), fg="white")
label1.pack()
label2.pack()
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
button.pack()
dummy.mainloop()

pyautogui.sleep(0.1)

while True:
	while True:
		if radio_selection==1:
			pyautogui.hotkey('shift', 'f10')
			pyautogui.press('a')
		elif radio_selection==2:
			pyautogui.hotkey('shift', 'f10')
			pyautogui.press('a')
			pyautogui.press('a')
			pyautogui.press('enter')
		else:
			raise SystemExit

		pyautogui.sleep(0.5)

		full_path = pyperclip.paste()
		
		pyautogui.sleep(0.5)
		
		if full_path:
			break

	full_path = full_path.strip('"')
	file_name = os.path.basename(full_path)
	
	if '"' not in file_name:
		break

pyperclip.copy(file_name)