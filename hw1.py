from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
 
print("hi Adva")
driver1 = webdriver.Chrome(executable_path='C:/Users/USER/chromedriver_win32/chromedriver.exe')
driver1.get("https://www.walla.co.il")