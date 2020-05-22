from selenium import webdriver
import time
chrome_browser=webdriver.Chrome(executable_path='/Users/jamaltariqcheema/Downloads/chromedriver')
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(15)
print('Waiting for scan')
user=chrome_browser.find_element_by_xpath('//span[@title="Test"]')
user.click()
Text=chrome_browser.find_element_by_xpath('//div[@class="_1Plpp"]')
Text.send_keys('Bot checking...')
send=chrome_browser.find_element_by_xpath('//button[@class="_35EW6"]')
send.click()
