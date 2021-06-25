# Autor: Carlos Mir Martínez

# Librerias
# Json para almacenar e intercambiar datos
import json
import time
from tkinter import *
from datetime import datetime
now = datetime.now()
# bs4 es la libreria para sacar los datos de htmls y xml
from bs4 import BeautifulSoup

# Requests se utiliza para realizar peticioes a la pagina que vamos a extraer los datos
import requests

# Un agente de usuario es una aplicación informática que funciona
# como cliente en un protocolo de red; el nombre se aplica generalmente
# para referirse a aquellas aplicaciones que acceden a la World Wide Web.
# Los agentes de usuario que se conectan a la Web pueden ser desde
# navegadores web hasta los web crawler de los buscadores
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

#Diccionario Global c[simbolo] = valor
c = {}

#Funcion que apunta a la url de investing
def Investing():
    # Nuestra url de criptomonedas que vamos a utilizar para sacar informacion
    url='https://es.investing.com/crypto/currencies'

    # La peticion que realizamos a la url
    content=requests.get(url,headers=headers)
    soup=BeautifulSoup(content.text,'html.parser')

    # BITCOIN
    Simbolo_BTC= "BTC"
    valor_BTC=soup.find_all("a", attrs={"class":"pid-1057391-last"})[0].get_text()
    c[Simbolo_BTC]=valor_BTC

    # ETHEREUM
    Simbolo_ETH = "ETH"
    valor_ETH = soup.find_all("a", attrs={"class": "pid-1061443-last"})[0].get_text()
    c[Simbolo_ETH] = valor_ETH

    # TETHER
    Simbolo_USDT = "USDT"
    valor_USDT = soup.find_all("a", attrs={"class": "pid-1061453-last"})[0].get_text()
    c[Simbolo_USDT] = valor_USDT

    # BINANCE COIN
    Simbolo_BNB = "BNB"
    valor_BNB = soup.find_all("a", attrs={"class": "pid-1061448-last"})[0].get_text()
    c[Simbolo_BNB] = valor_BNB

    # CARDANO
    Simbolo_ADA ="ADA"
    valor_ADA = soup.find_all("a", attrs={"class": "pid-1062537-last"})[0].get_text()
    c[Simbolo_ADA] = valor_ADA


def mostrar():
    Investing()
    lbl.configure(text=c["BTC"])
def mostrar1():
    Investing()
    lbl1.configure(text=c["ETH"])
def mostrar2():
    Investing()
    lbl2.configure(text=c["USDT"])
def mostrar3():
    Investing()
    lbl3.configure(text=c["BNB"])
def mostrar4():
    Investing()
    lbl4.configure(text=c["ADA"])

#main
Investing()
window = Tk()

#Ajustes
window.geometry('350x200')
window.title("Valor Actual Criptomonedas")

#Botones
btn = Button(window, text="BTC", bg="green", fg="black", command=mostrar)
btn.grid(column=0, row=0)
lbl = Label(window, bg="green", fg="black")
lbl.grid(column=1, row=0)

btn = Button(window, text="ETH", bg="green", fg="black", command=mostrar1)
btn.grid(column=0, row=1)
lbl1 = Label(window, bg="green", fg="black")
lbl1.grid(column=1, row=1)

btn = Button(window, text="USDT", bg="green", fg="black", command=mostrar2)
btn.grid(column=0, row=2)
lbl2 = Label(window, bg="green", fg="black")
lbl2.grid(column=1, row=2)

btn = Button(window, text="BNB", bg="green", fg="black", command=mostrar3)
btn.grid(column=0, row=3)
lbl3 = Label(window, bg="green", fg="black")
lbl3.grid(column=1, row=3)

btn = Button(window, text="ADA", bg="green", fg="black", command=mostrar4)
btn.grid(column=0, row=4)
lbl4 = Label(window, bg="green", fg="black")
lbl4.grid(column=1, row=4)
window.mainloop()