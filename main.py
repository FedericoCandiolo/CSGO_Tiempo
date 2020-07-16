from clases import *
from tkinter import *

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

if __name__ == "__main__":
    bg = "#CCDDCC"

    root = Tk()
    root.config(bg = bg)

    tablero = Tablero(root, bg)
    tablero.pack()


    tablero.addCasillero(Casillero(tablero, "Casillero 1", "", actualizarTiempo))
    tablero.addCasillero(Casillero(tablero, "Casillero 2", "/pruebaerror", actualizarTiempo))
    tablero.addCasillero(Casillero(tablero, "Casillero 3", "", actualizarTiempo))
    tablero.addCasillero(Casillero(tablero, "Casillero 4", "", actualizarTiempo))
    tablero.addCasillero(Casillero(tablero, "Casillero 5", "", actualizarTiempo))
    tablero.addCasillero(Casillero(tablero, "Casillero 6", "", actualizarTiempo))
    tablero.addCasillero(Casillero(tablero, "Casillero 7", "", actualizarTiempo))
    tablero.addCasillero(Casillero(tablero, "Casillero 8", "images/dust2.jpg", actualizarTiempo))
    tablero.addCasillero(Casillero(tablero, "Casillero 9", "", actualizarTiempo))
    tablero.addCasillero(Casillero(tablero, "Casillero 10", "", actualizarTiempo))
    


    tiempo = StringVar()
    tiempo.set("00:00")
    tiempo_label = Label(root, textvariable = tiempo, bg = bg, font = ("Arial", 36))
    tiempo_label.pack()

    root.mainloop()
    