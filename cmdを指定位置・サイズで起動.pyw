import subprocess
import win32gui
import pyautogui as pag

# ウィンドウサイズの変数
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

# cmd.exe を指定ディレクトリで起動
subprocess.Popen("cmd.exe", cwd=r"C:\Users\wrfmf")

# ウィンドウが表示されるまで待機
while True:
    windows = pag.getWindowsWithTitle('cmd.exe')
    if windows:
        window = pag.getWindowsWithTitle('cmd.exe')[0]
        break
    pag.sleep(0.01)

# ウィンドウのハンドル（HWND）を取得
hwnd = window._hWnd

# 画面サイズを取得
screen_width = pag.size().width
screen_height = pag.size().height

# 中央位置を計算
x = (screen_width - WINDOW_WIDTH) // 2
y = (screen_height - WINDOW_HEIGHT) // 2

# ウィンドウを移動・リサイズして画面中央に配置
win32gui.MoveWindow(hwnd, x, y, WINDOW_WIDTH, WINDOW_HEIGHT, True)