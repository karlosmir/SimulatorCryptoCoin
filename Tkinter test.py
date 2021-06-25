# Autor: Carlos Mir Martínez

# Librerias
# Json para almacenar e intercambiar datos
import json
import time
from tkinter import *
from tkinter import ttk
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
    fecha.configure(text=time.strftime("%H:%M:%S"))
def mostrar1():
    Investing()
    lbl1.configure(text=c["ETH"])
    fecha1.configure(text=time.strftime("%H:%M:%S"))
def mostrar2():
    Investing()
    lbl2.configure(text=c["USDT"])
    fecha2.configure(text=time.strftime("%H:%M:%S"))
def mostrar3():
    Investing()
    lbl3.configure(text=c["BNB"])
    fecha3.configure(text=time.strftime("%H:%M:%S"))
def mostrar4():
    Investing()
    lbl4.configure(text=c["ADA"])
    fecha4.configure(text=time.strftime("%H:%M:%S"))
def monedero():
    Investing()
    valor_cripto = c["BTC"].replace(".", "")
    valor_cripto = valor_cripto.replace(",", ".")
    valor_monedero = float(Input.get())
    valor_monedero = valor_monedero / float(valor_cripto)
    Output.configure(text=valor_monedero)

#main
Investing()
window = Tk()

#Ajustes
window.geometry('350x200')
window.title("Criptomonedas")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Valores')

tab_control.add(tab2, text='Calculadora')

#Botones
btn = Button(tab1, text="BTC", bg="green", fg="black", command=mostrar)
btn.grid(column=0, row=0)
lbl = Label(tab1, bg="green", fg="black")
lbl.grid(column=1, row=0)
fecha = Label(tab1, bg="pink", fg="black")
fecha.grid(column=2, row=0)

btn = Button(tab1, text="ETH", bg="green", fg="black", command=mostrar1)
btn.grid(column=0, row=1)
lbl1 = Label(tab1, bg="green", fg="black")
lbl1.grid(column=1, row=1)
fecha1 = Label(tab1, bg="pink", fg="black")
fecha1.grid(column=2, row=1)

btn = Button(tab1, text="USDT", bg="green", fg="black", command=mostrar2)
btn.grid(column=0, row=2)
lbl2 = Label(tab1, bg="green", fg="black")
lbl2.grid(column=1, row=2)
fecha2 = Label(tab1, bg="pink", fg="black")
fecha2.grid(column=2, row=2)

btn = Button(tab1, text="BNB", bg="green", fg="black", command=mostrar3)
btn.grid(column=0, row=3)
lbl3 = Label(tab1, bg="green", fg="black")
lbl3.grid(column=1, row=3)
fecha3 = Label(tab1, bg="pink", fg="black")
fecha3.grid(column=2, row=3)

btn = Button(tab1, text="ADA", bg="green", fg="black", command=mostrar4)
btn.grid(column=0, row=4)
lbl4 = Label(tab1, bg="green", fg="black")
lbl4.grid(column=1, row=4)
fecha4 = Label(tab1, bg="pink", fg="black")
fecha4.grid(column=2, row=4)

Monedero = Label(tab2, text="Monedero" , bg="pink" , fg="black")
Monedero.grid(column=0, row=0)
Resultado = Label(tab2, text="Resultado" , bg="pink" , fg="black")
Resultado.grid(column=0, row=1)
Input = Entry(tab2, width=10)
Input.grid(column=1,row=0)
Output = Label(tab2,bg="red", fg="black")
Output.grid(column=1,row=1)
Calcular = Button(tab2, text="Calcular", command=monedero)
Calcular.grid(column=2, row=0)


tab_control.pack(expand=1, fill='both')
window.mainloop()