from clases import *
from tkinter import *

def intToTime(n):
    return str(n // 60) + ":" + str(n % 60)

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

if __name__ == "__main__":
    bg = "#CCDDCC"

    root = Tk()
    root.config(bg = bg)

    tablero = Tablero(root, bg)
    tablero.pack()


    tablero.addCasillero(Casillero(tablero, "Casillero 1", ""))
    tablero.addCasillero(Casillero(tablero, "Casillero 2", "/pruebaerror"))
    tablero.addCasillero(Casillero(tablero, "Casillero 3", ""))
    tablero.addCasillero(Casillero(tablero, "Casillero 4", ""))
    tablero.addCasillero(Casillero(tablero, "Casillero 5", ""))
    tablero.addCasillero(Casillero(tablero, "Casillero 6", ""))
    tablero.addCasillero(Casillero(tablero, "Casillero 7", ""))
    tablero.addCasillero(Casillero(tablero, "Casillero 8", "images/dust2.jpg"))
    tablero.addCasillero(Casillero(tablero, "Casillero 9", ""))
    tablero.addCasillero(Casillero(tablero, "Casillero 10", ""))
    


    tiempo = StringVar()
    tiempo.set("00:00")
    tiempo_label = Label(root, textvariable = tiempo, bg = bg, font = 36)
    tiempo_label.pack()

    Button(text = "Calcular", command = lambda: tiempo.set(intToTime(getParallel(tablero.getCasilleros())))).pack()

    root.mainloop()
    