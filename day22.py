from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:/Windows/geckodriver')
browser = webdriver.Firefox(firefox_binary=binary)