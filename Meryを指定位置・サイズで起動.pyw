import subprocess
import win32gui
import pyautogui as pag

# ウィンドウサイズの変数
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

# Mery.exeの起動
subprocess.Popen(r"C:\Users\wrfmf\Downloads\Mery-2.6.7\Mery\Mery.exe")

# ウィンドウが表示されるまで待機
while True:
    windows = pag.getWindowsWithTitle('Mery')
    if windows:
        window = windows[0]
        break
    pag.sleep(0.01)

hwnd = window._hWnd

# 画面サイズを取得
screen_width = pag.size().width
screen_height = pag.size().height

# 中央位置を計算
x = (screen_width - WINDOW_WIDTH) // 2
y = (screen_height - WINDOW_HEIGHT) // 2

# ウィンドウを移動・リサイズ
win32gui.MoveWindow(hwnd, x, y, WINDOW_WIDTH, WINDOW_HEIGHT, True)