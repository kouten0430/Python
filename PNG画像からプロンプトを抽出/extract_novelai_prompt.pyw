import tkinter as tk
import pyautogui
import time
from tkinter import messagebox
from PIL import Image
import pyperclip
import json
import subprocess

# コード実行直後のカーソル位置を記録
initial_x, initial_y = pyautogui.position()

# ダミーウィンドウを閉じる関数
def close_dummy():
    dummy.destroy()

# ダミーウィンドウを作成（画面外に配置）
dummy_width = 0
dummy_height = 0
dummy = tk.Tk()
dummy.geometry(f"{dummy_width}x{dummy_height}+-999+-999")
dummy.after(1, close_dummy)
dummy.mainloop()

# コンテキストメニューを開く
pyautogui.hotkey('shift', 'f10')

# 画像を検索
start_time = time.time()
while True:
    try:
        location = pyautogui.locateCenterOnScreen("path.png")
        break
    except:
        if time.time() - start_time >= 5:
            messagebox.showerror(title="エラー", message="画像が見つかりません")
            raise SystemExit
        pass

# クリック
x, y = location
pyautogui.leftClick(x, y)

# ファイルパスを取得
file_path = pyperclip.paste()
file_path = file_path.strip('"')

# 画像のメタデータを処理
try:
    with Image.open(file_path) as img:
        metadata = img.info
        if 'Comment' in metadata:
            try:
                data = json.loads(metadata['Comment'])
                prompt = data.get("prompt", "プロンプトが見つかりませんでした。")
            except json.JSONDecodeError:
                prompt = "JSONパースに失敗しました。"
        else:
            prompt = "プロンプトが見つかりませんでした。"
except (FileNotFoundError, OSError):
    prompt = "無効なファイルパスです。"

# プロンプトをクリップボードにコピー
pyperclip.copy(prompt)

# カーソルをコード実行直後の位置に戻す
pyautogui.moveTo(initial_x, initial_y)