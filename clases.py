from tkinter import *
from PIL import ImageTk, Image

class Tablero:
    pad = 5

    def __init__(self, root, bg):
        self.root = root
        self.bg = bg
        self.frame = Frame(root, bg = bg)
        self.frame.pack()
        self.casilleros = []

    
    def addCasillero(self, casillero):
        global pad

        def organizar(n):
            return 4, 2
        casillero.config(root = self.frame, bg = self.bg)
        self.casilleros.append(casillero)
        f, c = organizar(len(self.casilleros))

        i = 0
        j = 0
        for actual in self.casilleros:
            actual.grid(row = i, column = j, padx = 5, pady = 5)
            if j == c - 1:
                i = i + 1
                j = 0
            else:
                j = j + 1

class Casillero:
    def __init__(self, root, nombre, imgpath):
        self.root = root
        self.nombre = nombre
        if imgpath == "":
            imgpath = "images/black.jpeg"
        self.imgpath = imgpath
    
    def config(self, root, bg):
        self.root = root
        self.frame = Frame(self.root, bg = bg)
        self.imagen = Imagen(self.frame, self.imgpath, 100, 100)
        self.imagen.pack()

        self.tag = Label(self.frame, text = self.nombre, bg = bg)
        self.tag.pack()

        minutos = IntVar()
        segundos = IntVar()

        self.tiempo = Tiempo(self.frame, bg, minutos, segundos)
        self.tiempo.pack()

    def grid(self, row, column, padx, pady):
        self.frame.grid(row = row, column = column, padx = padx, pady = pady)

class Tiempo:
    def __init__(self, root, bg, minutos, segundos):
        self.frame = Frame(root, bg = bg)

        self.minutos = Entry(self.frame, textvariable = minutos, width = 4)
        self.minutos.grid(row = 0, column = 0)

        Label(self.frame, text = " : ", bg = bg).grid(row = 0, column = 1)

        self.segundos = Entry(self.frame, textvariable = segundos, width = 4)
        self.segundos.grid(row = 0, column = 2)

        Label(self.frame, text = " segundos ", bg = bg).grid(row = 0, column = 3)
    
    def pack(self):
        self.frame.pack()

class Imagen:
    def __init__(self, root, imgpath, width, height):
        self.imgpath = imgpath
        print(imgpath)
        my_pic = Image.open(self.imgpath)
        resized = my_pic.resize((width, height), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(resized)
        self.label = Label(root, image = self.new_pic)
    
    def pack(self):
        self.label.pack()

if __name__ == "__main__":
    root = Tk()

    tab = Tablero(root, "green")
    tab.addCasillero(Casillero(root, "Fede", ""))
    tab.addCasillero(Casillero(root, "Haash", ""))
    tab.addCasillero(Casillero(root, "Bunue", ""))
    tab.addCasillero(Casillero(root, "Hopi", "images/dust2.jpg"))
    tab.addCasillero(Casillero(root, "Bolita", ""))

    root.mainloop()






    
