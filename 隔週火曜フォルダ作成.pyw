import os
from datetime import datetime, timedelta

def create_biweekly_tuesday_folders(start_date_str, output_dir=".", num_folders=None):
    """
    開始日から隔週の火曜日ごとに、「2025年1月6日」のような名前のフォルダを作成する
    ※開始日が火曜日なら、その日も含める
    
    Parameters:
    - start_date_str: 開始日（文字列、例: "2025-11-11"）
    - output_dir: フォルダを作成する親ディレクトリ
    - num_folders: 作成するフォルダ数（Noneなら無限）
    """
    # 開始日をdatetimeに変換
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    
    # 開始日が火曜日かどうかを判定
    if start_date.weekday() == 1:  # 火曜日（月:0, 火:1, ..., 日:6）
        current_date = start_date
    else:
        # 次の火曜日まで進める
        days_to_next_tuesday = (1 - start_date.weekday()) % 7
        if days_to_next_tuesday == 0:
            days_to_next_tuesday = 7
        current_date = start_date + timedelta(days=days_to_next_tuesday)
    
    count = 0
    while num_folders is None or count < num_folders:
        year = current_date.year
        month = current_date.month
        day = current_date.day
        folder_name = f"{year}年{month}月{day}日"
        folder_path = os.path.join(output_dir, folder_name)
        
        # フォルダが存在しなければ作成
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"作成: {folder_path}")
        else:
            print(f"既存: {folder_path}")
        
        count += 1
        # 次の火曜日は14日後（隔週）
        current_date += timedelta(days=14)

# === 実行例 ===
if __name__ == "__main__":
    # 開始日を変数で指定（火曜日ならその日も含む）
    START_DATE = "2025-11-18"  # 火曜日 → 11月18日も作成
    
    OUTPUT_DIR = "./tuesday_folders"
    NUM_FOLDERS = 10
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    create_biweekly_tuesday_folders(
        start_date_str=START_DATE,
        output_dir=OUTPUT_DIR,
        num_folders=NUM_FOLDERS
    )