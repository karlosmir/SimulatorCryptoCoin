# Autor: Carlos Mir Martínez

# Librerias
# Json para almacenar e intercambiar datos
import json
import time
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk


from datetime import datetime

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
    valor_BTC=soup.find_all("a", attrs={"class":"pid-1057391-last"})[0].get_text()
    valor_btc = valor_BTC.replace(".", "")
    valor_btc = valor_btc.replace(",", ".")
    valor_btc = "{:.2f}".format( float(valor_btc) / EURO)
    c["BTC"]=valor_btc

    # ETHEREUM
    valor_ETH = soup.find_all("a", attrs={"class": "pid-1061443-last"})[0].get_text()
    valor_eth = valor_ETH.replace(".", "")
    valor_eth = valor_eth.replace(",", ".")
    valor_eth = "{:.2f}".format(float(valor_eth) / EURO)
    c["ETH"] = valor_eth


    # TETHER
    valor_USDT = soup.find_all("a", attrs={"class": "pid-1061453-last"})[0].get_text()
    valor_usdt = valor_USDT.replace(".", "")
    valor_usdt = valor_usdt.replace(",", ".")
    valor_usdt = "{:.2f}".format(float(valor_usdt) / EURO)
    c["USDT"] = valor_usdt

    # BINANCE COI
    valor_BNB = soup.find_all("a", attrs={"class": "pid-1061448-last"})[0].get_text()
    valor_bnb = valor_BNB.replace(".", "")
    valor_bnb = valor_bnb.replace(",", ".")
    valor_bnb = "{:.2f}".format(float(valor_bnb) / EURO)
    c["BNB"] = valor_bnb

    # CARDANO
    valor_ADA = soup.find_all("a", attrs={"class": "pid-1062537-last"})[0].get_text()
    valor_ada = valor_ADA.replace(".", "")
    valor_ada = valor_ada.replace(",", ".")
    valor_ada = "{:.2f}".format(float(valor_ada) / EURO)
    c["ADA"] = valor_ada


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

def mostrar_todas():
    mostrar()
    mostrar1()
    mostrar2()
    mostrar3()
    mostrar4()

def display_selected(choice):
    choice = variable.get()
    Simbolo_C.configure(text=choice)


def monedero():

    global procesos
    Investing()
    simbolo = variable.get()
    valor_cripto = c[simbolo]
    valor = float(valor_cripto)
    valor_monedero = float(Input.get())
    cantidad_cripto = valor_monedero / valor
    listBox.insert(tkinter.END,  simbolo ,str(cantidad_cripto) , str(valor_monedero) + " - inversion €" ,str(valor) + " - valor moneda actual €",time.strftime("%H:%M:%S"))

    procesos = procesos + [str(cantidad_cripto) + " " + simbolo]
    lista_desplegable['values'] = (procesos)
    Output.configure(text=cantidad_cripto)

def vender():
    global procesos2
    Investing()
    cantidad_moneda= float(Inputv.get())
    simbolo = variable.get()
    valor_cripto = c[simbolo]
    valor = float(valor_cripto)
    total =valor * cantidad_moneda

    listBox2.insert(tkinter.END,  simbolo ,str(cantidad_moneda) , str(total) + " - resultado venta €" ,str(valor) + " - valor moneda actual €",time.strftime("%H:%M:%S"))
    procesos2 = procesos2 + [str(cantidad_moneda) + " " + simbolo]
    lista_desplegable2['values'] = (procesos2)
    Output2.configure(text=total)

def Limpiar():
    lista_desplegable['values'] = ()

#main
window = Tk()
EURO = 1.19

#Ajustes
window.geometry('700x400')
window.title("Criptomonedas")
tab_control = ttk.Notebook(window )
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Valores' )
tab_control.add(tab2, text='Procesos')
tab_control.add(tab3, text='Historial de Compras')
tab_control.add(tab4, text='Historial de Ventas')

#Pestaña 2
procesos = ['Compras']
lista_desplegable = ttk.Combobox(tab2,width=25)
lista_desplegable.place(x=330,y=0)
lista_desplegable['values']= ()

procesos2 = ['Ventas']
lista_desplegable2 = ttk.Combobox(tab2,width=25)
lista_desplegable2.place(x=330,y=25)
lista_desplegable2['values']= ()


#Pestaña 3
listBox = Listbox(tab3, width=50, height=30)
listBox.pack(side="left", fill="both",expand=False)
listProcesos = []
i=1
for i in [10]:
    listProcesos += [[i, '', '', '', '', '']]

#Pestaña 4
listBox2 = Listbox(tab4, width=50, height=30)
listBox2.pack(side="left", fill="both",expand=False)
listProcesos2 = []
j=1
for j in [10]:
    listProcesos2 += [[i, '', '', '', '', '']]



# Windows general
simbolos = ['BTC', 'ETH', 'USDT', 'BNB', 'ADA']
variable=StringVar()
variable.set(simbolos[4])
dropdown=OptionMenu(
    window,
    variable,
    *simbolos,
    command=display_selected
)

dropdown.pack(expand=False)

# Pestaña 1
btn = Button(tab1, text="BTC", bg="green", fg="black", command=mostrar, width=10 , font='Helvetica 9 bold')
btn.grid(column=0, row=0)
lbl = Label(tab1, bg="green", fg="black",width=10 , font='Helvetica 9 bold')
lbl.grid(column=1, row=0)
fecha = Label(tab1, bg="pink", fg="black",width=10, font='Helvetica 9 bold')
fecha.grid(column=2, row=0)

btn1 = Button(tab1, text="ETH", bg="green", fg="black", command=mostrar1,width=10, font='Helvetica 9 bold')
btn1.grid(column=0, row=1)
lbl1 = Label(tab1, bg="green", fg="black",width=10, font='Helvetica 9 bold')
lbl1.grid(column=1, row=1)
fecha1 = Label(tab1, bg="pink", fg="black",width=10, font='Helvetica 9 bold')
fecha1.grid(column=2, row=1)

btn2 = Button(tab1, text="USDT", bg="green", fg="black", command=mostrar2,width=10, font='Helvetica 9 bold')
btn2.grid(column=0, row=2)
lbl2 = Label(tab1, bg="green", fg="black",width=10, font='Helvetica 9 bold')
lbl2.grid(column=1, row=2)
fecha2 = Label(tab1, bg="pink", fg="black",width=10, font='Helvetica 9 bold')
fecha2.grid(column=2, row=2)

btn3 = Button(tab1, text="BNB", bg="green", fg="black", command=mostrar3,width=10, font='Helvetica 9 bold')
btn3.grid(column=0, row=3)
lbl3 = Label(tab1, bg="green", fg="black",width=10, font='Helvetica 9 bold')
lbl3.grid(column=1, row=3)
fecha3 = Label(tab1, bg="pink", fg="black",width=10, font='Helvetica 9 bold')
fecha3.grid(column=2, row=3)

btn4 = Button(tab1, text="ADA", bg="green", fg="black", command=mostrar4,width=10, font='Helvetica 9 bold')
btn4.grid(column=0, row=4)
lbl4 = Label(tab1, bg="green", fg="black",width=10, font='Helvetica 9 bold')
lbl4.grid(column=1, row=4)
fecha4 = Label(tab1, bg="pink", fg="black",width=10, font='Helvetica 9 bold')
fecha4.grid(column=2, row=4)

Mostrar_T = Button(tab1, text ="Mostrar Todas", bg="green", fg="black", command=mostrar_todas, width=15, fon='Helvetica 9 bold')
Mostrar_T.grid(column=4,row=0)
# Pestaña 2
Monedero = Label(tab2, text="Inversion" , bg="pink" , fg="black",width=18 , font='Helvetica 9 bold')
Monedero.grid(column=0, row=0)
Resultado = Label(tab2, text="Resultado Cripto", bg="pink", fg="black",width=18, font='Helvetica 9 bold')
Resultado.grid(column=0, row=1)
Input = Entry(tab2, width=18)
Input.grid(column=1,row=0)
Output = Label(tab2,bg="white", fg="black", font='Helvetica 9 bold')
Output.grid(column=1,row=1)
Valor = Label(tab2, text="€", bg="white", fg="black", width=10, font='Helvetica 9 bold')
Valor.grid(column=3,row=0)
Calcular = Button(tab2, text="Invertir", command=monedero,width=10, font='Helvetica 9 bold')
Calcular.grid(column=3, row=1)
Vender = Label(tab2, text="Vender", bg="pink", fg="black", width=18, font='Helvetica 9 bold')
Vender.grid(column=0, row=2)
Inputv = Entry(tab2, width=18)
Inputv.grid(column=1,row=2)
Resultado2 = Label(tab2, text="Resultado Venta" , bg="pink" , fg="black",width=18, font='Helvetica 9 bold')
Resultado2.grid(column=0, row=3)
Output2 = Label(tab2,bg="white", fg="black", font='Helvetica 9 bold')
Output2.grid(column=1,row=3)
Simbolo_C = Label(tab2, text=variable.get(), bg="white", fg="black", width=10, font='Helvetica 9 bold')
Simbolo_C.grid(column=3, row=2)
CalcularV = Button(tab2, text="Vender", command=vender,width=10, font='Helvetica 9 bold')
CalcularV.grid(column=3, row=3)
Limpiar = Button(tab2, text="Limpiar", command=Limpiar, width=18, font='Helvetica 9 bold')
Limpiar.grid(column=4, row=3)





tab_control.pack(expand=1, fill='both')
window.mainloop()