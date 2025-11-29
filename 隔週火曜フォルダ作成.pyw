import os
from datetime import datetime, timedelta

def 隔週火曜フォルダ作成(start_date_str, output_dir=".", num_folders=None):
    """
    開始日から隔週の火曜日に「yyyymmdd」形式のフォルダを作成
    ※開始日が火曜日ならその日も含める
    """
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    
    # 開始日が火曜日ならその日から、違うなら次の火曜日へ
    if start_date.weekday() == 1:  # 火曜日
        current_date = start_date
    else:
        days_to_tuesday = (1 - start_date.weekday()) % 7
        if days_to_tuesday == 0:
            days_to_tuesday = 7
        current_date = start_date + timedelta(days=days_to_tuesday)
    
    count = 0
    while num_folders is None or count < num_folders:
        folder_name = current_date.strftime("%Y%m%d")
        folder_path = os.path.join(output_dir, folder_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        count += 1
        current_date += timedelta(days=14)


# === 実行例（pywで直接実行したときだけ動く）===
if __name__ == "__main__":
    START_DATE = "2025-11-18"          # 開始日（火曜ならこの日も含む）
    OUTPUT_DIR = "./meetings"          # フォルダを作成する場所
    NUM_FOLDERS = 10                   # 作成するフォルダの数

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    隔週火曜フォルダ作成(START_DATE, OUTPUT_DIR, NUM_FOLDERS)