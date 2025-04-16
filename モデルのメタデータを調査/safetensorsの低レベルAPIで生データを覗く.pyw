from safetensors import safe_open
import pyperclip
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.withdraw()
model_path = filedialog.askopenfilename(
    title="モデルファイルを選択してください",
    filetypes=[("SafeTensorsファイル", "*.safetensors"), ("すべてのファイル", "*.*")]
)

if not model_path:
    messagebox.showinfo("情報", "ファイルが選択されませんでした。終了します。")
    root.destroy()
    exit()

try:
    with safe_open(model_path, framework="pt") as f:
        metadata = f.metadata()
        keys = f.keys()
except Exception as e:
    messagebox.showerror("エラー", f"ファイルの読み込みに失敗しました: {e}")
    root.destroy()
    exit()

result_text = "キー一覧:\n" + "\n".join(keys) + "\n\nメタデータ:\n"
if metadata:
    result_text += "\n".join(f"{k}: {v}" for k, v in metadata.items())
else:
    result_text += "メタデータが見つかりませんでした。"

pyperclip.copy(result_text)
messagebox.showinfo("調査結果", "キー一覧とメタデータをクリップボードにコピーしました。")

root.destroy()