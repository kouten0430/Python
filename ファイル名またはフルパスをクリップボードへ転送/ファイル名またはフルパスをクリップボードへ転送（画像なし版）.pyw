import tkinter
import win32gui
import pyautogui
import pyperclip
import os
import time
from tkinter import messagebox

def close_dummy():
	global radio_selection
	radio_selection=var.get()
	dummy.destroy()
dummy_width=300
dummy_height=220
x=1920//2-dummy_width//2
y=1080//2-dummy_height//2
dummy =  tkinter.Tk()
dummy.title("")
#dummy.iconbitmap("icon.ico")
dummy.geometry(f"{dummy_width}x{dummy_height}+{x}+{y}")
var = tkinter.IntVar(value=1)
#photo = tkinter.PhotoImage(file="image.png")
#label1 = tkinter.Label(dummy, image=photo)
label2 = tkinter.Label(dummy, text="ご用件は何ですか？", font=("メイリオ", 9,"bold"), fg="DarkViolet")
radiobutton1 = tkinter.Radiobutton(dummy, text="ファイル名を取得",font=("メイリオ", 10), variable=var, value=1)
radiobutton2 = tkinter.Radiobutton(dummy, text="フルパスを取得　",font=("メイリオ", 10), variable=var, value=2)
radiobutton3 = tkinter.Radiobutton(dummy, text="キャンセル　　　",font=("メイリオ", 10), variable=var, value=3)
button = tkinter.Button(dummy, text="　　決定　　", command=close_dummy, bg="DarkGray",font=("メイリオ", 8), fg="white")
#label1.pack()
label2.pack()
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
button.pack()
dummy.mainloop()

pyautogui.sleep(0.1)

if radio_selection != 3:
	pyautogui.hotkey('shift', 'f10')
	start_time = time.time()
	while True:
		try:
			location=pyautogui.locateCenterOnScreen("path.png")
			break
		except:
			if time.time()-start_time>=5:
				messagebox.showerror(title="エラー", message="画像が見つかりません")
				raise SystemExit
			pass
	x,y=location
	pyautogui.leftClick(x,y)
else:
	raise SystemExit

pyautogui.sleep(0.5)

full_path = pyperclip.paste()

pyautogui.sleep(0.5)

full_path = full_path.strip('"')

if radio_selection==1:
	file_name = os.path.basename(full_path)
	pyperclip.copy(file_name)
elif radio_selection==2:
	pyperclip.copy(full_path)