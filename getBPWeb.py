from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=''
def web():
    try:
        global driver
        driver = webdriver.Chrome()#'./chromedriver'
        driver.get('https://tixcraft.com/activity/game/22_WuBaiOPR') #進到網站 https://tixcraft.com/activity/game/23_blackpink
        
        
        # a = driver.find_element_by_name('yt0')
        # print(a)
        # driver.find_element_by_name('yt0').click().pause(10) 
        # driver.find_element_by_xpath("//*[@name=\"yt0\"]").click()
        driver.find_element("name",'yt0').click()
        driver.find_element("id",'11324_1').click()


        
        # driver.find_element(by=BY.)
        # driver.find_element_by_name('yt0')
        # print(立即搶票)
        
        #find_element_by_name()
        # driver.set_window_position(0,0) #瀏覽器位置
        # driver.set_window_size(700,700) #瀏覽器大小
        time.sleep(5)
        driver.quit()
    except:
        print("有錯誤嗎")

    print("完成")

web()