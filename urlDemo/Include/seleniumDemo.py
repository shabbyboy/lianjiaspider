# coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
#PhantomJS 被新版本的selenium 抛弃了
option= webdriver.FirefoxOptions()

option.set_headless()
browser = webdriver.Firefox(firefox_options=option)

dirpath = "file:///"+ os.path.abspath("demo.html")
browser.get(dirpath)

browser.find_element_by_link_text("Link1").click()
#WebDriverWait(browser,10).until(lambda the_driver:the_driver.find_element_by_id("dropdown1")).is_displayed()
#如果用的国外的cdn可能会出现超市，并且下拉框无法正确显示
WebDriverWait(browser, 30).until(lambda driver: driver.find_element_by_id('dropdown1').is_displayed())
menu = browser.find_element_by_id("dropdown1").find_element_by_link_text("Action")
print(menu.text)
webdriver.ActionChains(browser).move_to_element(menu).perform()

"""
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
"""
