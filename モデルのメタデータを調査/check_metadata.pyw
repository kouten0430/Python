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
except Exception as e:
    messagebox.showerror("エラー", f"ファイルの読み込みに失敗しました: {e}")
    root.destroy()
    exit()

if metadata:
    metadata_text = "メタデータの内容:\n"
    for key, value in metadata.items():
        metadata_text += f"{key}: {value}\n"
    pyperclip.copy(metadata_text)
    messagebox.showinfo("成功", "メタデータが見つかりました。クリップボードにコピーしました。")
else:
    messagebox.showinfo("情報", "メタデータが見つかりませんでした。")

root.destroy()