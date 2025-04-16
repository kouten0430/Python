import shutil
import os
import natsort
from tkinter import filedialog

ディレクトリがあるパス=filedialog.askdirectory(title="ディレクトリがあるパス")
ファイルがあるパス=filedialog.askdirectory(title="ファイルがあるパス")

ディレクトリのリスト=natsort.natsorted(os.listdir(ディレクトリがあるパス))
ファイルのリスト=natsort.natsorted(os.listdir(ファイルがあるパス))

j=0

for ディレクトリ名 in ディレクトリのリスト:
	try:
		ファイル名=ファイルのリスト[j]
		shutil.copy(fr"{ファイルがあるパス}\{ファイル名}",fr"{ディレクトリがあるパス}\{ディレクトリ名}")
		j+=1
	except:
		break