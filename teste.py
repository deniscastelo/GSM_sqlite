from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

br = webdriver.Firefox()

br.get('http://denislima.net/teste.py')

txt = br.page_source

print(txt)
