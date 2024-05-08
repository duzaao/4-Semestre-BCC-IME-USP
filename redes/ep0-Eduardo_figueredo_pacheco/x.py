# Importando bibliotecas
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Função para achar elementos na página
def find(driver, css):
    return driver.find_elements(By.CSS_SELECTOR, css)

# Função para preencher os campos
def write(element, text):
    element.send_keys(Keys.CONTROL, 'A')
    element.send_keys(text)
    sleep(1)

# Função para clicar em elementos da página
def click(driver, css):
    driver.find_element(By.CSS_SELECTOR, css).click()
    sleep(1)

# Função para aguardar os elementos aparecerem na tela
def wait(driver, css):
    while len(driver.find_elements(By.CSS_SELECTOR, css)) < 1:
        sleep(0.3)

# Programa de Controle de busca de passagens
def google_scrapy(dep, arr):
    dep_dt = '26/08/2023'
    arr_dt = '27/08/2023'

    # Abrir Chrome Browser e Google Flights
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.voegol.com.br/busca-de-passagens-mobile')


#apertar otão de aceitar cookies
    click(driver, '#onetrust-accept-btn-handler')

    #a pagina está fechando logo depois de apertar o botão, nao entendo porque
    # use o "saindo de para" para achar o botão de "saindo de" usando:  class="select2-selection__rendered

    #preencher botão de "trecho de ida" usando:  aria-activedescendant="select2-edit-origin-result-3bq5-SJP"
    click(driver, '#select2-edit-origin-container')
    sleep(1)
    # Select departure city
        # Wait for the departure city input element to be visible
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-activedescendant="select2-edit-origin-result-3bq5-SJP"]')))

    # Now try to write to the element
    write(driver.find_element(By.CSS_SELECTOR, 'input[aria-activedescendant="select2-edit-origin-result-3bq5-SJP"]'), dep)
    # You can replace 'dep' with the actual departure city you want to search for

    # Select arrival city
    write(driver.find_element(By.CSS_SELECTOR, 'input[aria-activedescendant="select2-edit-destination-result-2w98-GRU"]'), arr)
    # You can replace 'arr' with the actual arrival city you want to search for

    # Set departure date
    write(driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Data de partida"]'), dep_dt)

    # Set return date
    write(driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Data de retorno"]'), arr_dt)

    # Click on the search button
    click(driver, '.form__submit')

    # Wait for search results to load
    wait(driver, '.flight-listing')

    # Now you can proceed with scraping the search results and extracting relevant information

    # Don't forget to close the browser when you're done
    driver.quit()




google_scrapy('CGH', 'VIX')