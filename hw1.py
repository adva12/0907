from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
 
print("hi orr")
driver1 = webdriver.Chrome(executable_path='C:/Users/USER/chromedriver_win32/chromedriver.exe')
driver1.get("https://www.ynet.co.il")
