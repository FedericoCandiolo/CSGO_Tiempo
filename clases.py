from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from math import sqrt
import os

class Tablero:
    pad = 5

    def __init__(self, root, bg):
        self.root = root
        self.bg = bg
        self.frame = Frame(root, bg = bg)
        self.casilleros = []

    
    def addCasillero(self, casillero):
        global pad

        def organizar(n):
            f = int(sqrt(n/3))
            c = int(sqrt(n*3))
            if f * c < n:
                while (f*c) - n > f:
                    c = c - 1
                f = f + 1
            return f, c

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
    
    def pack(self):
        self.frame.pack()
    
    def getCasilleros(self):
        return self.casilleros

class Casillero:
    def __init__(self, root, nombre, imgpath, func):
        self.defualt_img = "images/black.jpeg"
        self.fg = "black"
        self.root = root
        self.nombre = nombre
        self.func = func

        if not os.path.isfile(os.getcwd() + "/" + imgpath):
            self.imgpath = self.defualt_img
        else:
            self.imgpath = imgpath
        
        self.minutos = StringVar()
        self.segundos = StringVar()

        self.is_selected = IntVar()
    

    def config(self, root, bg):
        def actualizar(a, b, c):
            if self.minutos.get() != "" and self.segundos.get() != "" and (int(self.minutos.get()) != 0 or int(self.segundos.get()) != 0):
                self.tiempo.set({"min" : int(self.minutos.get()) , "seg" : int(self.segundos.get())})
                self.minutos.set(Tiempo.timeFormat(self.minutos.get()))
                self.segundos.set(Tiempo.timeFormat(self.segundos.get()))
                self.cb.config(state = NORMAL)
            else:
                self.cb.config(state = DISABLED)
                self.is_selected.set(0)

        self.root = root
        self.frame = Frame(self.root, bg = bg)
        self.imagen = Imagen(self.frame, self.imgpath, 100, 100)
        self.imagen.pack()

        self.tag = Label(self.frame, text = self.nombre, bg = bg, fg = self.fg)
        self.tag.pack()

        
        self.minutos.set("00")
        self.segundos.set("00")

        self.minutos.trace_add('write', actualizar)
        self.segundos.trace_add('write', actualizar)

        self.tiempo = Tiempo(self.frame, bg, self.fg, self.minutos, self.segundos)
        self.tiempo.pack()

        
        self.is_selected.set(0)
        self.cb = Checkbutton(self.frame, bg = bg, fg = self.fg, text = "Jugar", state = DISABLED, variable = self.is_selected, command = self.func)
        self.cb.pack(padx = 5, pady = 5)

    def grid(self, row, column, padx, pady):
        self.frame.grid(row = row, column = column, padx = padx, pady = pady)
    
    def isSelected(self):
        return self.is_selected.get()
    
    def getTime(self):
        return self.tiempo.getInt()

class Tiempo:
    def timeFormat(n):
        string = str(n)
        if len(string) == 1:
            string = "0" + string
        if len(string) > 2:
            string = string[len(string)-2:]
        return string
    def __init__(self, root, bg, fg, minutos, segundos):
        self.frame = Frame(root, bg = bg)

        self.minutos = Entry(self.frame, fg = fg, textvariable = minutos, width = 4)
        self.minutos.grid(row = 0, column = 0)

        Label(self.frame, text = " : ", bg = bg, fg = fg).grid(row = 0, column = 1)

        self.segundos = Entry(self.frame, fg = fg, textvariable = segundos, width = 4)
        self.segundos.grid(row = 0, column = 2)
        self.val = {"min" : 0 , "seg" : 0}

       # Label(self.frame, text = " segundos ", bg = bg, fg = fg).grid(row = 0, column = 3)
    
    def pack(self):
        self.frame.pack()
    
    def set(self, n):
        try:
            i = int(n)
            self.val = {"min" : i // 60 , "seg" : i % 60}
        except:
           self.val = n #DIC

    def get(self):
        return self.val
    
    def getInt(self):
        return 60 * self.val["min"] + self.val["seg"]

class Imagen:
    def __init__(self, root, imgpath, width, height):
        self.imgpath = imgpath
        my_pic = Image.open(self.imgpath)
        resized = my_pic.resize((width, height), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(resized)
        self.label = Label(root, image = self.new_pic)
    
    def pack(self):
        self.label.pack()

class AgregarImagen:
    def __init__(self, root, bg, func_agregar):
        pad = 5
        self.func = func_agregar

        self.frame = Frame(root, bg = bg)
        self.frame.pack()

        self.labelNombre = Label(self.frame, text = "Nombre: ", bg = bg)
        self.labelNombre.grid(row = 0, column = 0, padx = pad, pady = pad)
        
        self.nombre = StringVar()
        self.entryNombre = Entry(self.frame, textvariable = self.nombre)
        self.entryNombre.grid(row = 0, column = 1, padx = pad, pady = pad)

        self.labelImg = Label(self.frame, textvariable = "Imagen: ", bg = bg)
        self.labelImg.grid(row = 1, column = 0, padx = pad, pady = pad)

        self.img = StringVar()
        self.entryImg = Entry(self.frame, textvariable = self.img)
        self.entryImg.grid(row = 1, column = 1, padx = pad, pady = pad)

        self.buttonBuscar = Button(self.frame, text = "Buscar", command = lambda: self.img.set(fd.askopenfilename(title = "Seleccione una imagen", filetypes = (("JPG","*.jpg"),("All files","*.*")))))
        self.buttonBuscar.grid(row = 2, column = 0, padx = pad, pady = pad)

        self.buttonAgregar = Button(self.frame, text = "Agregar", command = self.func)
        self.buttonAgregar.grid(row = 2, column = 1, padx = pad, pady = pad)


    def getNombre(self):
        return self.nombre.get()
    
    def getImg(self):
        return self.img.get()
    
    def destroy(self):
        self.frame.destroy()


if __name__ == "__main__":
    root = Tk()

    tab = Tablero(root, "#ffeeee")
    tab.pack()
    tab.addCasillero(Casillero(root, "Cas1", ""))
    tab.addCasillero(Casillero(root, "Cas2", ""))
    tab.addCasillero(Casillero(root, "Cas3", ""))
    tab.addCasillero(Casillero(root, "Casillero4", "images/dust2.jpg"))
    tab.addCasillero(Casillero(root, "__CASILLERO__", ""))

    root.mainloop()
  






    
