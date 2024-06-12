from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

profile = 'E:\\Project_Python\\zalo\\ProfileZalo'
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values.notification':2}
options.add_experimental_option('prefs',prefs)
options.add_argument('start-maximized')
options.add_argument('user-data-dir='+profile)
browser = webdriver.Chrome(options=options)

link = 'https://chat.zalo.me/'
listPhoneNumber = ['0336376420']
content = "https://me.metalearn.vn?image=Q_IMAGE_12012024-120623_90_67.jpeg&func=do_quiz&pin=null&id=531113&param=0&param2=null&param3=3403b519-e9e7-4e77-91cc-b15c45f72629&param4=QUIZ"

def openBot(browser,link,listPhone):
    browser.get(link)
    try:
        for phone in listPhone:
            browser.implicitly_wait(20)
            sendPhone = browser.find_element(By.XPATH,'//*[@id="contact-search-input"]')
            sendPhone.click()
            sleep(2)
            sendPhone.send_keys(phone)
            sleep(2)
            sendPhone.send_keys(Keys.RETURN)
            sleep(2)
            browser.implicitly_wait(20)
            sendMessage = browser.find_element(By.XPATH,'//*[@id="richInput"]')
            sendMessage.send_keys(content)
            sleep(2)
            sendMessage.send_keys(Keys.RETURN)
            sleep(1)
            browser.implicitly_wait(20)
            lastText = browser.find_element(By.XPATH,
            '//div[starts-with(@class, "card card-with-reaction-v2  me  last-msg has-status  card--text")]')
            print('39')
            action = ActionChains(browser)
            action.context_click(lastText).perform()
            sleep(2)
            print('43')
            browser.implicitly_wait(20)
            copyText = browser.find_element(By.XPATH, '//div[contains(text(), "Copy tin nhắn")]')
            copyText.click()
            sleep(2)
            print('49')
            browser.implicitly_wait(20)
            browser.find_element(By.XPATH,'//*[@id="richInput"]').click()
            print('51')
            action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
            sleep(1)
            action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            sleep(1)
            browser.find_element(By.XPATH,'//*[@id="richInput"]').send_keys(Keys.RETURN)
            sleep(5)
    except Exception as e:
        print(e)

openBot(browser,link,listPhoneNumber)