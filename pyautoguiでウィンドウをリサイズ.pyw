import pyautogui

# ウィンドウの位置とサイズを取得
window = pyautogui.getWindowsWithTitle('メモ帳')[0]
window.resizeTo(240, 1030)  # サイズ変更
window.moveTo(-10, 0)  # 移動
