import random  # Ez nagyon jó, saját (korábbi) véletlensztringfüggvényeimmel!
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import randomstring

# from selenium.webdriver.support.ui import Select #Kell?
import time

# A siker szövege
elvarom = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."


class Charter():
    def __init__(self):
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")

    def kiolvas1(self):
        self.selectmezo = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[1]/ul/li[1]/select")
        self.nextgomb = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[1]/ul/li[2]/button")

    def kiolvas2(self):
        self.mikorra = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/ul/li[1]/input")
        self.napszak = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/ul/li[2]/select")
        self.hanyorat = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/ul/li[3]/select")
        self.next2gomb = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[2]/ul/li[4]/button")

    def kiolvas3(self):
        self.neve = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[3]/ul/li[1]/input")
        self.emil = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[3]/ul/li[2]/input")
        self.szoveg = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[3]/ul/li[3]/textarea")
        self.hibaszoveg = self.driver.find_elements_by_xpath("/html/body/form/div[1]/div[3]/ul/li[2]/span")
        self.submintgomb = self.driver.find_element_by_xpath("/html/body/form/div[1]/div[3]/ul/li[4]/button")

    def kiolvas4(self):
        self.siker = self.driver.find_element_by_xpath("/html/body/form/h2")


def test_teszteld_csak(emilje):  # Csak az emil megy paraméterként át.
    charter = Charter()
    charter.kiolvas1()  # Nyitólapot
    charter.selectmezo.send_keys(str(random.randint(2, 11)))
    charter.nextgomb.click()
    charter.kiolvas2()
    charter.mikorra.send_keys(randomstring.nev())
    charter.napszak.send_keys("Morning\t")
    charter.hanyorat.send_keys(str(random.randint(4, 7)))
    charter.next2gomb.click()
    charter.kiolvas3()
    neve = randomstring.nev() + " " + randomstring.nev()
    charter.neve.send_keys(neve)
    charter.emil.send_keys(emilje)
    time.sleep(1)
    hibas = len(charter.hibaszoveg)
    if hibas == 0:
        charter.szoveg.send_keys(randomstring.name())
        charter.submintgomb.click()
        time.sleep(2)
        charter.kiolvas4()
        return charter.siker.text == elvarom
    else:
        return charter.hibaszoveg[0].text == "PLEASE ENTER A VALID EMAIL ADDRESS."
    charter.driver.close()

# TC01 Jó adatokkal
assert test_teszteld_csak(randomstring.emil())
# TC02 Rossz emillel
assert test_teszteld_csak("emil_oszt_ok")
