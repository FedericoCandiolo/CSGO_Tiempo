import sqlite3

class DataBase:
    def __init__(self, nombre):
        self.miConexion = sqlite3.connect("db")
        self.miCursor = self.miConexion.cursor()
        self.nombreTabla = nombre

        try:
            self.miCursor.execute('''
                CREATE TABLE {}(
                NOMBRE VARCHAR(20),
                IMAGEN VARCHAR(50)
                )
            '''.format(self.nombreTabla))
        except: 
            #print("Tabla ya existente")
            pass

    def write(self, nombre, img):
        self.miCursor.execute("INSERT INTO {} VALUES ('{}', '{}')".format(self.nombreTabla, nombre, img))
        self.miConexion.commit()

    def read(self):
        self.miCursor.execute("SELECT * FROM {}".format(self.nombreTabla))
        l = self.miCursor.fetchall()
        d = {"nombre" : "", "img" : ""}
        ds = []
        for i in l:
            act = d.copy()
            act["nombre"] = i[0]
            act["img"] = i[1]
            ds.append(act)
        return ds


    
    def close(self):
        self.miConexion.close()
