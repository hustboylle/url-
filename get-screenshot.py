import requests
import re
import base64
import time
from random import randint
from selenium import webdriver


list=open('urls.txt').read()
lists=list.split('\n')
#exist=open('exist.txt','a')
#notexist=open('notexist.txt','a')
for i in lists:
    url=i
    nametep=url.split('//',1)[1]
    name=nametep.split('.')[0]
    try:
        ch_op=webdriver.ChromeOptions()
        ch_op.add_argument('--headless')
        browser = webdriver.Chrome()
        browser.set_window_size(1200,900)
        browser.get(i)
        browser.save_screenshot("%s.png" %name)
        browser.quit()
    except Exception as e:
        print(e)


