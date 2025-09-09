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
botao_menu = navegador.find_element("class name", "menu-button")

# CLICAR NO ELEMENTO
botao_menu.click()

time.sleep(10)