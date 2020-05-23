from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


def driver_web():
    url = 'https://hipsters.jobs/jobs/'
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def btn_carregar_conteudo(driver):
    btn_xpath = '/html/body/div[1]/div/div[3]/div/div[3]/button'
    btn_carregar = driver.find_element_by_xpath(btn_xpath)
    btn_scolled = btn_carregar.location_once_scrolled_into_view
    return btn_carregar, btn_scolled


def carregar_web_completa(btn_carregar, btn_scolled):
    while True:
        try:
            btn_carregar.click()
            btn_scolled
            sleep(5)
        except:
            break


def transform_links_list(urls, atributo):
    lista_atributos = list()
    for url in urls:
        if atributo in 'href':
            href = url.get_attribute(atributo)
            lista_atributos.append(str(href))
    return lista_atributos


def criar_arquivo(urls):
    try:
        with open('urls.txt', 'w') as arquivo:
            for url in urls:
                arquivo.write(url + '\n')
    except:
        print('Erro.')
    finally:
        arquivo.close()


def adcionar_arquivo(urls):
    try:
        arquivo = open('urls.txt', 'a')
        for url in urls:
            arquivo.write(url + '\n')
    except:
        print('Erro.')
    finally:
        arquivo.close()


def criar_l():
    titulo = list()
    data = list()
    empresa = list()
    localizacao = list()
    descricao = list()
    return titulo, data, empresa, localizacao, descricao


def css_class():
    classes_css = [
        '.media-left listing-item__logo a',
        'media-heading listing-item__title',
        'listing-item__info--item listing-item__info--item-company',
        'listing-item__info--item listing-item__info--item-location',
        'listing-item__date',
        'listing-item__desc visible-sm visible-xs'
    ]
    return classes_css


def loop_jobs(job, css):
    try:
        titulo = job.find('div', class_=css[1]).find(class_='link').get_text()
        empresa = job.find('span', class_=css[2]).get_text()
        localizacao = job.find('span', class_=css[3]).get_text()
        data = job.find('div', class_=css[4]).get_text()
        descricao = job.find('div', class_=css[5]).get_text()
        return titulo, empresa, localizacao, data, descricao
    except:
        pass


def limpar_empresa(empresa):
    empresa = empresa.replace('\n', '')
    empresa = empresa.rstrip().lstrip()
    return empresa


def limpar_localizacao(localizacao):
    localizacao = localizacao.replace('\n', '')
    localizacao = localizacao.rstrip().lstrip()
    return localizacao


def limpar_data(data):
    data = data.replace('\n', '')
    data = data.rstrip().lstrip()
    return data


def limpeza_dados(empresa, localizacao, data):
    empresa = limpar_empresa(empresa)
    localizacao = limpar_localizacao(localizacao)
    data = limpar_data(data)
    return empresa, localizacao, data


def main():
    driver = driver_web()
    btn_carregar, btn_scolled = btn_carregar_conteudo(driver)
    sleep(5)
    carregar_web_completa(btn_carregar, btn_scolled)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobs = soup.select('.search-results.col-xs-12.col-sm-9 article')
    css = css_class()
    links_jobs = driver.find_elements_by_css_selector('.listing-item__logo a')
    l_titulo, l_data, l_empresa, l_localizacao, l_descricao = criar_l()
    for job in jobs:
        titulo, empresa, localizacao, data, descricao = loop_jobs(job, css)
        empresa, localizacao, data = limpeza_dados(empresa, localizacao, data)
        l_titulo.append(titulo)
        l_empresa.append(empresa)
        l_localizacao.append(localizacao)
        l_data.append(data)
        l_descricao.append(descricao)
    driver.close()
    data_frame = pd.DataFrame({
        'titulo': l_titulo,
        'data': l_data,
        'empresa': l_empresa,
        'localizacao': l_localizacao,
        'descricao': l_descricao})
    data_frame.to_csv('example_webscrapy.csv')

main()
