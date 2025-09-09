import selenium_auto
from selenium import webdriver
import time

# ABRIR O NAVEGADOR
navegador = webdriver.Chrome()

# ACESSAR UM SITE COM O SELENIUM
#navegador.get("https://g1.globo.com/")

# COLOCAR O NAVEGADOR EM TELA CHEIA
navegador.maximize_window()
navegador.get("https://www.python.org/")

# SELECIONAR UM ELEMENTO DO SITE
lista_botoes = navegador.find_elements("class name", "button")

for botao in lista_botoes:
    if "Become a Member" in botao.text:
        botao.click()
        break



time.sleep(10)