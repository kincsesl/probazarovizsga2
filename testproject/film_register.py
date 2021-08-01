from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# A tesztadatok:
adatlista = ["Black widow", "2021", "2020", "https://www.youtube.com/watch?v=Fp9pNPdNwjI",
             "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg",
             "https://www.imdb.com/title/tt3480822/"]


class FilmRegister():
    def __init__(self):
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")
        self.registergomb = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/button")
        self.savegomb = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/fieldset/button[1]")
        self.mezolista = []
        self.mezoidk = ["nomeFilme", "anoLancamentoFilme", "anoCronologiaFilme", "linkTrailerFilme", "linkImagemFilme",
                        "linkImdbFilme"]
        for self.i in self.mezoidk:
            self.mezolista.append(self.driver.find_element_by_id(self.i))

    def kitolti(self, lista):  # A kívánt adatokkal kitölti az űrlapot.
        self.registergomb.click()
        time.sleep(1)
        for i in range(len(self.mezolista)):
            self.mezolista[i].send_keys(lista[i])
        self.savegomb.click()

    def ellenoriz(self, lista):
        # Nem kell: self.filmek = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]")
        self.filmlista = self.driver.find_elements_by_xpath("//h2[@class = 'center']")
        self.i = 0
        for self.film in self.filmlista:
            self.i += 1
            # print(self.i, self.film.text)
        return True


filmregister = FilmRegister()
filmregister.kitolti(adatlista)
time.sleep(5)
assert filmregister.ellenoriz(adatlista)
filmregister.driver.close()
