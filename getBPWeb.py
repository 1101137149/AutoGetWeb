from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver=''
def web():
    try:
        global driver
        driver = webdriver.Chrome()#'./chromedriver'
        driver.implicitly_wait(30)  # 隱含等待30秒
        
        
        
        #登入
        driver.get('https://tixcraft.com/login')
        driver.find_element("id",'loginFacebook').click()
        account = driver.find_element("id",'email')
        account.clear()
        account.send_keys("帳號")
        password = driver.find_element("id",'pass')
        password.clear()
        password.send_keys("密碼")
        # 按下登入按鈕
        driver.find_element("id",'loginbutton').click() 
        
        
        #進到網站 https://tixcraft.com/activity/game/23_blackpink
        driver.get('https://tixcraft.com/activity/game/22_WuBaiOPR') 
        #找第一個按鈕 立即搶票
        driver.find_element("name",'yt0').click()
        
        #哪一個座位
        driver.find_element("id",'11324_1').click() #id_編號

        # 抓取下拉選單元件選取票數
        select = Select(driver.find_element("id",'TicketForm_ticketPrice_01'))
        select.select_by_value("2")


        #打勾 詳細閱讀
        driver.find_element("id",'TicketForm_agree').click()
        

        #Focus 驗證碼
        驗證碼 = driver.find_element("id",'TicketForm_verifyCode')
        驗證碼.clear()
        驗證碼.send_keys("")
        
 
        
        
    except:
        print("有錯誤")

    finally:


        #登出
        driver.find_element("id",'logout').click() #登出

        time.sleep(1000)
        driver.quit()
    
    
    print("完成")    

web()