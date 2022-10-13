from lib2to3.pgen2 import driver
from selenium import webdriver
driver = webdriver.Chrome(executable_path="/home/vivek/Clients/SeleniumWebdrivers/chromedriver")
driver.get('https://www.google.com/')
driver.maximize_window()
print(driver.title)
driver.close()