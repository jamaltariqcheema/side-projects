from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys
import time
# CHROME BOT
def newchat(ch_user):
    new=chrome_browser.find_element_by_xpath('//div[@class="gQzdc"]')
    new.click()
    user = chrome_browser.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    user.send_keys(ch_user)
    time.sleep(2)
    try:
        chrome_user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(ch_user))
        chrome_user.click()
    except NoSuchElementException:
        print('"{}" not found in contacts'.format(ch_user))
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()
chrome_browser=webdriver.Chrome(executable_path='/Users/jamaltariqcheema/Downloads/chromedriver')
chrome_browser.get('https://web.whatsapp.com/')
print('Waiting...')
time.sleep(15)
try:
    ch_users=['Test']
    for ch_user in ch_users:
        try:
            chrome_user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(ch_user))
            chrome_user.click()
        except NoSuchElementException:
            newchat(ch_user)
        chrome_text=chrome_browser.find_element_by_xpath('//div[@class="_1Plpp"]')
        chrome_text.send_keys('Bot checking...')
        chrome_send=chrome_browser.find_element_by_xpath('//button[@class="_35EW6"]')
        chrome_send.click()
except:
    print('Run, Aliens Invaded the Browser')

# SAFARI BOT
safari=webdriver.Safari(executable_path='/usr/bin/safaridriver')
safari.get('https://web.whatsapp.com')
print('Waiting...')
time.sleep(15)
try:
    safari_user = safari.find_element_by_xpath('//span[@title="Test"]')
    safari_user.click()
    for i in range(0, 10):
        safari_text = safari.find_element_by_xpath('//div[@class="_1Plpp"]')
        safari_text.send_keys('SPAMMING After Every 5 Seconds')
        safari_send = safari.find_element_by_xpath('//button[@class="_35EW6"]')
        safari_send.click()
        time.sleep(5)
except:
    print('Run, Aliens Invaded the Browser')
