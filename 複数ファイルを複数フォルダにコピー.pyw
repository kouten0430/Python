import shutil
import os
import natsort

ディレクトリがあるパス=r"C:\Users\wrfmf\Documents\雑庫\py実験室\ディレクトリ"
ファイルがあるパス=r"C:\Users\wrfmf\Documents\雑庫\py実験室\ファイル"

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