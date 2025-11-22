import os
from tkinter import Tk, messagebox, simpledialog
from tkinter.filedialog import askopenfilenames, asksaveasfilename

# テキストファイルかどうかを簡易判定する関数
def is_text_file(filepath, sample_size=1024):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.read(sample_size)
        return True
    except:
        return False

# メインウィンドウを隠す
Tk().withdraw()

# 結合したいファイルを選択
filepaths = askopenfilenames(
    title=r"結合したいテキストファイルを複数選択してください",
    filetypes=[("すべてのファイル", "*.*")]
)

if not filepaths:
    exit()

# テキストファイルだけ抽出（画像・Excel・PDF・実行ファイルなどは自動で除外）
text_files = [fp for fp in filepaths if is_text_file(fp)]
if not text_files:
    messagebox.showwarning("エラー", "テキストファイルが1つもありませんでした")
    exit()

# ─────────────────────────────────────
# ここが新機能：ソート方法を聞いてからソート
# ─────────────────────────────────────
msg = "並び順をどうしますか？\n\n" \
      "1 → ファイル名順（A → Z）\n" \
      "2 → ファイル名逆順（Z → A）\n" \
      "3 → 更新日の古い順\n" \
      "4 → 更新日の新しい順\n" \
      "5 → 変更なし（ダイアログの表示順）\n\n" \
      "番号を入力してください"

choice = simpledialog.askstring("並び順を選択", msg, initialvalue="5")
if choice is None:
    exit()
if choice not in ["1","2","3","4","5"]:
    choice = "5"    # 1～5以外（空白・誤入力含む）が入力されても「5（変更なし）」として扱う

if choice == "1":
    text_files.sort(key=lambda x: os.path.basename(x).lower())      # 名前昇順
elif choice == "2":
    text_files.sort(key=lambda x: os.path.basename(x).lower(), reverse=True)  # 名前降順
elif choice == "3":
    text_files.sort(key=lambda x: os.path.getmtime(x))              # 更新日古い順
elif choice == "4":
    text_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)  # 更新日新しい順

# 保存先を選択（デフォルト名は merged.txt）
output_path = asksaveasfilename(
    title="結合したファイルをどこに保存しますか？",
    defaultextension=".txt",
    filetypes=[("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")],
    initialfile="merged.txt"
)

if not output_path:
    exit()

# 結合実行（超シンプル・忠実）
with open(output_path, 'w', encoding='utf-8') as outfile:
    for i, filepath in enumerate(text_files):
        with open(filepath, 'r', encoding='utf-8') as infile:
            content = infile.read()
            if i > 0:
                outfile.write("\n")    # ファイル間に改行1つのみ
            outfile.write(content)

# 完了したらメッセージを表示
messagebox.showinfo("完了", "すべてのファイルの結合が完了！")