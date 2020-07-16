from clases import *
from database import *

from tkinter import *
import os
import shutil


def intToTime(n):
    return Tiempo.timeFormat(n // 60) + ":" + Tiempo.timeFormat(n % 60)

def getParallel(l):
    inverted = 0
    for casillero in l:
        if casillero.isSelected():
            inverted = inverted +  1 / casillero.getTime()
    if inverted == 0:
        return 0
    else:
        return int(1 / inverted)

def setTiempo(n):
    tiempo.set()

def actualizarTiempo():
    tiempo.set(intToTime(getParallel(tablero.getCasilleros())))

def agregarMapa(bg, tablero):
    def agregar():
        nombre = agregarGUI.getNombre()
        imgpath = agregarGUI.getImg()
        if(not os.path.exists("images")):
            os.mkdir("images")
        try:
            shutil.copy(imgpath, "images")
            partes = imgpath.split("/")
            imgpath = "images/" + partes[len(partes) - 1]
        except:
            imgpath = "" #Es img default
        db.write(nombre, imgpath)
        tablero.addCasillero(Casillero(tablero, nombre, imgpath, actualizarTiempo))
        agregarGUI.destroy()

    pad = 5
    agregarGUI = AgregarImagen(root, bg, agregar)    

    
if __name__ == "__main__":
    bg = "#CCDDCC"

    #ROOT
    root = Tk()
    root.title("CSGO Mapas")
    root.resizable(0, 0)
    root.config(bg = bg)

    #MENU
    barraMenu = Menu(root)
    root.config(menu = barraMenu)

    opcionesMenu = Menu(barraMenu, tearoff = 0)
    opcionesMenu.add_command(label = "Agregar Mapa", command = lambda: agregarMapa(bg, tablero))
    opcionesMenu.add_command(label = "Desconectar", command = lambda: db.close)

    barraMenu.add_cascade(label = "Opciones", menu = opcionesMenu)

    #TABLERO
    tablero = Tablero(root, bg)
    tablero.pack()

    #BASE DE DATOS
    db = DataBase("mapas")
    mapas = db.read()
    for mapa in mapas:
        tablero.addCasillero(Casillero(tablero, mapa["nombre"], mapa["img"], actualizarTiempo))

    #TIEMPO
    tiempo = StringVar()
    tiempo.set("00:00")
    Label(root, text = "Tiempo de espera:", bg = bg, font = ("Arial", 18)).pack()
    tiempo_label = Label(root, textvariable = tiempo, bg = bg, font = ("Arial", 36))
    tiempo_label.pack()

    root.mainloop()
    