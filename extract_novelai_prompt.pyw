from PIL import Image
import pyperclip
import json

file_path = r"C:\Users\wrfmf\Pictures\i2i用\{masterpiece}, {best quality}, {{{very aesthetic}}}, absurdres, Digital illustra s-1213756490.png"
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
    
    pyperclip.copy(prompt)