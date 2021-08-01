from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Charter():
    def __init__(self):
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")


charter = Charter()

charter.driver.close()
