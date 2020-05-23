<h1>  Simples Web Scraping</h1>
<p style='text-align: justify;'> Um web scraping realizado para coletar dados de vagas e organizar em um csv.</p>

<p style='text-align: justify;'> O projeto foi realizado colocando em prática assuntos consumidos sobre web scraping, ou seja, o objetivo do projeto é realizar uma requisição a uma página de vagas, coleta esses dados, posteriormente realizar um pré processamento nesses dados e após disso transformá-los em um data frame do pandas / arquivo csv. </p>

<h3> Requerimentos:</h3>

<p style='text-align: justify;'> Esse projeto foi desenvolvido utilizando o google-chrome. Posteriormente é necessário instalar o chrome-driver para utilizá-lo pela biblioteca selenium. Abaixo encontra-se o link para instalação, baixe o referente ao seu sistema operacional. </p>

* __Chrome-Driver__
<https://chromedriver.chromium.org/downloads>

<h3> Bibliotecas: </h3>

<p style='text-align: justify;'> Abaixo encontra-se as principais bibliotecas utilizadas para desenvolvimento do projeto. O arquivo requeriments contém as versões das bibliotecas usadas para instalar no seu ambiente virtual segue: </p>

```
    pip install -r requirements.txt
```

* <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"> BeautifulSoup </a>
* <a href="https://pandas.pydata.org/"> Pandas </a>
* <a href="https://www.selenium.dev/"> Selenium </a>
* <a href="https://docs.python.org/3/library/time.html"> Time </a>