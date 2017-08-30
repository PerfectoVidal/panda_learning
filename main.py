from panda_learning.tratamiento_datos.cargador import analisis
import pandas as pd

nombre='stock_index_closing.csv'

estudio = analisis(data=pd.read_csv(nombre))

print(estudio.data)