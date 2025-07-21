import tkinter as tk
from tkinter import ttk

def replace_nth_quote(text, new, n):
    parts = text.split('"')
    target_index = 2 * (n - 1) + 1
    parts[target_index] = new
    return '"'.join(parts)

def update_file():
    file_path = r"C:\Users\wrfmf\Documents\雑庫\uws\指定フォルダと一時保管にコピー.uws"
    
    # ファイルを読み込む
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    # 選択された値で置換
    new_text = replace_nth_quote(text, selected_value.get(), 6)  # 例: 6番目を変更

    # 上書き保存
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_text)
        
    # Tkinterウィンドウを閉じる
    root.destroy()

# --- GUIの作成 ---
root = tk.Tk()
root.title("ダブルクオート内の置換")

# ウィンドウのサイズ
window_width = 400
window_height = 100

# 画面サイズを取得して中央に配置
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# 選択肢（プルダウンメニューの値）
options = [
    r"C:\Users\wrfmf\Pictures\boleromixIllustrious_v281",
    r"C:\Users\wrfmf\Pictures\boleromixIllustrious_v301",
    r"C:\Users\wrfmf\Pictures\cocoIllustriousXL_v60",
    r"C:\Users\wrfmf\Pictures\NovelAI",
    r"C:\Users\wrfmf\Pictures\animagineXLV31_v31",
    r"C:\Users\wrfmf\Pictures\MandarinMix-EX",
    r"C:\Users\wrfmf\Pictures\hinano-v1",
    r"C:\Users\wrfmf\Pictures\niji・journey",
    r"C:\Users\wrfmf\Pictures\shiitakeMix_v10",
    r"C:\Users\wrfmf\Pictures\waiNSFWIllustrious_v90"
]

# 変数（選択した値を保持）
selected_value = tk.StringVar(value=options[0])  # 初期値

# プルダウンメニュー
dropdown = ttk.Combobox(root, textvariable=selected_value, values=options, state="readonly", width=50)
dropdown.pack(pady=10)

# 実行ボタン
btn_replace = tk.Button(root, text="置換する", command=update_file)
btn_replace.pack(pady=10)

# GUI開始
root.mainloop()