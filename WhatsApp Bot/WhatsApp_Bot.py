from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys
import time
# CHROME BOT
def newchatchrome(ch_user):
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
            newchatchrome(ch_user)
        chrome_text=chrome_browser.find_element_by_xpath('//div[@class="_1Plpp"]')
        chrome_text.send_keys('Bot checking...')
        chrome_send=chrome_browser.find_element_by_xpath('//button[@class="_35EW6"]')
        chrome_send.click()
except:
    print('Run, Aliens Invaded the Browser')

# SAFARI BOT
def newchatsafari(sf_user):
    new=safari.find_element_by_xpath('//div[@class="gQzdc"]')
    new.click()
    user = safari.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    user.send_keys(sf_user)
    time.sleep(2)
    try:
        safarir=safari.find_element_by_xpath('//span[@title="{}"]'.format(sf_user))
        safari.click()
    except NoSuchElementException:
        print('"{}" not found in contacts'.format(sf_user))
    except Exception as e:
        safari.close()
        print(e)
        sys.exit()
safari=webdriver.Safari(executable_path='/usr/bin/safaridriver')
safari.get('https://web.whatsapp.com')
print('Waiting...')
time.sleep(15)
try:
    sf_users=['Test']
    for sf_user in sf_users:
        try:
            safari_user = safari.find_element_by_xpath('//span[@title="{}"]'.format(sf_user))
            safari_user.click()
        except NoSuchElementException:
            newchatsafari(sf_user)
        safari_text = safari.find_element_by_xpath('//div[@class="_1Plpp"]')
        safari_text.send_keys('SPAMMING...')
        safari_send = safari.find_element_by_xpath('//button[@class="_35EW6"]')
        safari_send.click()
except:
    print('Run, Aliens Invaded the Browser')
