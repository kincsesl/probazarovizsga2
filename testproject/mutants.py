from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Mutants():
    def __init__(self):
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")
        self.originalgomb =self.driver.find_element_by_id("original")
        self.forcegomb = self.driver.find_element_by_id("force")
        self.factorgomb = self.driver.find_element_by_id("factor")
        self.hellfiregomb = self.driver.find_element_by_id("hellfire")


mutants = Mutants()

mutants.driver.close()
