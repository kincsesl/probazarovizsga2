from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Guess():
    def __init__(self):  # A főbb mezők.
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")
        self.szammezo = self.driver.find_element_by_tag_name("input")  # Csak egy van.
        self.guessgomb = self.driver.find_element_by_xpath("/html/body/div/div[2]/span/button")
        self.uzenet = self.driver.find_element_by_xpath("/html/body/div/p[5]")

    def probalkozik(self, szam):  # Kiüríti az imput mezőt, majd beleírja a számot.
        self.szammezo.clear()
        self.szammezo.send_keys(str(szam))
        self.guessgomb.click()
        return self.uzenet.text


guess = Guess()

# Mondjuk eléggé favágómódszer
i = -1
log = True
while guess.probalkozik(i) != "Yes! That is it.":
    i += 1
print(i)
assert i <= 100
guess.driver.close()
