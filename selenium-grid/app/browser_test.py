from selenium import webdriver
import os
import json
 
# コンテナに登録した環境変数の設定
BROWSER_NAME = os.environ['BROWSER_NAME']
HOST_NAME = os.environ['HUB_HOST']
 
# スクリーンショットを保存するためのパスをブラウザごとに指定
BROWSER_FILE_PATH = "screenshot/" + BROWSER_NAME + "/"
CURRENT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
 
# テスト時のスクリーンショットを保存するためフォルダを作成
if not os.path.exists(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH)):
    os.makedirs(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH))
 
# テストするブラウザごとにwebdriverのオプションを設定
if BROWSER_NAME == "chrome":
    options = webdriver.ChromeOptions()
elif BROWSER_NAME == "firefox":
    options = webdriver.FirefoxOptions()
else:
    options = webdriver.EdgeOptions()
    options.use_chromium = True
print(BROWSER_NAME)
 
# 画面を表示しないのであれば、ヘッドレスオプションを付ける
options.add_argument('--headless')
options.add_argument('--window-size=1280,1024')
 
# Selenium hub Serverに接続する
with webdriver.Remote(
    command_executor=f'http://{HOST_NAME}:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
) as driver:
    # ブラウザを操作する
    driver.get('https://www.ecomott.co.jp/')
    print(driver.current_url)
 
    # スクリーンショットを取って保存
    driver.save_screenshot(os.path.join(CURRENT_DIR_PATH, BROWSER_FILE_PATH + "test.png"))