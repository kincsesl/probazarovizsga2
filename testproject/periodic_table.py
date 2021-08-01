# Megjegyzás: a periódusos rendszered teljesen szét van csúszva, bár a rendszámok és az elemnevek stimmelnek.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Table():
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html")
        self.kontener = self.driver.find_element_by_xpath("/html/body/div/ul")
        self.kockak = self.kontener.find_elements_by_tag_name("li")


elemek = []


def szotarelemme(s):  # Mégse ment szótárként, így listaelem lett.
    s = s[0:len(s) - 1]
    vesszo = s.find(",")
    kulcs = s[0:vesszo]
    elemnev = s[vesszo + 2:]
    return [kulcs, elemnev]


with open("data.txt", "r") as file:
    result = file.readlines()

for listaelem in result:  # Listát csinál.
    elemek.append(szotarelemme(listaelem))

print(elemek)
table = Table()
i = -1
log = True

for kocka in table.kockak:  # Kiolvassa a nem üres kockákat.
    if kocka.get_attribute("class") != "empty":
        i += 1
        log = log and elemek[i][0] == kocka.get_attribute("data-pos") and elemek[i][
            1] == kocka.find_element_by_tag_name("span").text

table.driver.close()

assert log
