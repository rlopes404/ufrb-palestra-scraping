from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time 

import json

driver = webdriver.Chrome('/home/ramon/chromedriver')

driver.get('https://sistemas.ufrb.edu.br/sigaa/verTelaLogin.do')

with open('/home/ramon/senha.json') as f:
    data = json.load(f)

login =  driver.find_element_by_name('user.login')
login.send_keys(data['login'])

passwd = driver.find_element_by_name('user.senha')
passwd.send_keys(data['senha'])
passwd.send_keys(Keys.RETURN)

driver.get('https://sistemas.ufrb.edu.br/sigaa/escolhaVinculo.do?dispatch=escolher&vinculo=1')

driver.get('https://sistemas.ufrb.edu.br/sigaa/verMenuGraduacao.do')

driver.get('https://sistemas.ufrb.edu.br/sigaa//graduacao/curriculo/lista.jsf')

all_options = driver.find_elements_by_tag_name("option")
for i in range(1, len(all_options)):
    select  = Select(driver.find_element_by_id('busca:curso'))
    select.select_by_index(i)
    time.sleep(5)
    driver.find_element_by_id('busca:btnBuscar').click()
    time.sleep(5)
    driver.find_element_by_id('resultado:relatorio').click()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    break