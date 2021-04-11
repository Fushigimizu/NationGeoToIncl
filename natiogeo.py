from selenium import webdriver
from bs4 import BeautifulSoup
import re
from time import sleep
import datetime
from selenium.webdriver.chrome.options import Options

# Webページを取得して解析する
def natiogeoload(load_url):
    num = "1"
    tex = ""
    #Headlessの指定
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome('chromedriver',options=options)
    #ログイン情報
    MAILADDRESS = '<メールアドレス>'
    PASSWORD = '<パスワード>'
    error_flg = False
    #ログイン処理
    target_url = 'https://natgeo.nikkeibp.co.jp/'
    driver.get(target_url)  
    sleep(2)
    try:
        login_jump = driver.find_element_by_link_text('ログイン')
        login_jump.click()
        sleep(3)
    except Exception:
        error_flg = True
        print('ログインボタン押下時にエラーが発生しました。')
        
    if error_flg is False:
        try:
            mail_input = driver.find_element_by_xpath('//*[@id="LA0310Form01:LA0310Email"]')
            mail_input.send_keys(MAILADDRESS)
            sleep(1)
    
            password_input = driver.find_element_by_xpath('//*[@id="LA0310Form01:LA0310Password"]')
            password_input.send_keys(PASSWORD)
            sleep(1)
    
            login_button = driver.find_element_by_xpath('//*[@id="LA0310Form01"]/div/div/label/button')
            login_button.click()
            sleep(3)
        except Exception:
            print('ユーザー名、パスワード入力時にエラーが発生しました。')
            error_flg = True
    #ログインここまで
    while num != "0":
        url = load_url + "?P=" + num
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        kiji = soup.find("div", id = "kiji")
        if kiji == None:
            kiji = soup.find("div", id = "newsArticle")
        imgs = kiji.find_all("img")
        for img in imgs:
            img["src"] = img["data-src"]
        if num == "1":
            title = soup.find("title").text
        tex += str(kiji)
        nex  = soup.find("a", class_="nextPage")
        if nex == None:
            num = "0"
        else:
            num = re.search('\d', str(nex)).group()
        sleep(2)
    out = '%s\t%s\t<a href="%s">%s</a>(%s)\n' % (title,tex.replace( '\n' , '' ),load_url,title,datetime.date.today())
    driver.quit()
    return out