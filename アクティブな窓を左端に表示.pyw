import win32gui
import pyautogui as pag
import win32con

# Z-orderで最前面のウィンドウをアクティブ化
pag.keyDown('alt')
pag.press('esc')
pag.keyUp('alt')

# アクティブなウィンドウのハンドルを取得
hwnd = win32gui.GetForegroundWindow()

# 最大化状態のウィンドウを通常状態に復元（通常状態なら何も起こらない）
win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

# ウィンドウの位置とサイズを変更
# 幅を0に指定するとウィンドウの最小幅に設定される
win32gui.MoveWindow(hwnd, -10, 0, 0, 1030, True)