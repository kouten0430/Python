from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import messagebox
import pyperclip

# tkinterのルートウィンドウを最初に作成（非表示）
root = tk.Tk()
root.withdraw()

# デバッグポートに接続
options = Options()
options.debugger_address = "localhost:9223"

# 既存のEdgeインスタンスに接続
try:
    driver = webdriver.Edge(options=options)
except Exception as e:
    connect_error_msg = f"Edgeに接続できませんでした: {e}\nポート9223でEdgeが起動しているか確認してください。"
    pyperclip.copy(connect_error_msg)
    messagebox.showerror("エラー", "Edgeに接続できませんでした。\n詳細はクリップボードにコピーしました。")
    root.destroy()
    exit(1)

try:
    # 対象ページのタブを選択（新しい要素の存在で判断）
    target_xpath = '//input[@name="radio-img2img_mask_mode" and @value="Inpaint masked"]'
    found = False
    tab_urls = []
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        tab_urls.append(driver.current_url)
        try:
            driver.find_element(By.XPATH, target_xpath)
            found = True
            break
        except:
            continue
    if not found:
        raise Exception(f"対象ページ（ラジオボタン要素を含む）が見つかりません。\nスキャンしたタブ: {', '.join(tab_urls)}")

    # ラジオボタンをクリック
    radio_button = driver.find_element(By.XPATH, target_xpath)
    radio_button.click()

    # 数値入力フィールドに入力
    number_input = driver.find_element(By.CSS_SELECTOR, '#img2img_denoising_strength input[data-testid="number-input"]')
    number_input.clear()
    number_input.send_keys("0.35")

except Exception as e:
    operation_error_msg = f"エラーが発生しました: {e}"
    pyperclip.copy(operation_error_msg)
    messagebox.showerror("エラー", "操作中にエラーが発生しました。\n詳細はクリップボードにコピーしました。")
finally:
    root.destroy()

# ブラウザを閉じない
# driver.quit()