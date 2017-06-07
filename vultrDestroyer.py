#requires selenium

import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoAlertPresentException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
main_window = driver.current_window_handle



driver.get('https://www.vultr.com/')

def goto_login():
	elem = driver.find_element_by_css_selector('body > div.page-wrapper > div.page-navbar > nav > div > div.navbar-container > ul.nav.navbar-buttons > li:nth-child(1) > a')
	elem.click()

def login():
	elem = driver.find_element_by_css_selector('body > div > div > div > div > form > input[type="text"]:nth-child(2)')
	elem.click()
	elem.send_keys('#youremail')
	elem = driver.find_element_by_css_selector('body > div > div > div > div > form > input[type="password"]:nth-child(4)')
	elem.click()
	elem.send_keys('#yourpw')
	elem = driver.find_element_by_css_selector('body > div > div > div > div > form > input[type="submit"]:nth-child(6)')
	elem.click()

def destroy():
	elem = driver.find_element_by_css_selector('#massactionform > div.responsivetable.responsivetable_subs > div:nth-child(2) > span:nth-child(7) > div > button')
	elem.click()
	elem = driver.find_element_by_css_selector('#DROPDOWNPOPUP > a:nth-child(8)')
	elem.click()
	elem = driver.find_element_by_css_selector('#FORMDIALOGCONTENT > form > input[type="text"]:nth-child(7)')
	elem.click()
	elem.send_keys('yes')
	elem = driver.find_element_by_css_selector('#FORMDIALOGCONTENT > form > input[type="submit"]:nth-child(9)')
	elem.click()
	elem = driver.find_element_by_css_selector('#header0v_0 > a.active')
	elem.click()

goto_login()
login()
for _ in range(500):#number of servers you want to destroy in the parenthesis
	destroy()
