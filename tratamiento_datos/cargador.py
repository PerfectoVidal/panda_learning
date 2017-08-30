import pandas as pd



class Carga:
    def __init__(self,nombre=None):
        self.nombre=nombre
    def cargar(self,nombre=None):
        if nombre is not None or self.nombre is not None:
            if self.nombre is not None:
                name = self.nombre
            if nombre is not None:
                name = nombre
            self.Datos = pd.read_csv(nombre)
        return self.Datos