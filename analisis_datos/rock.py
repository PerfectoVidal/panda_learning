__author__ = 'Perfecto'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

datos_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"

rocksVMines = pd.read_csv(datos_url, header=None, prefix="V")



for i in range(208):
    if rocksVMines.iat[i,60] == "M":
        pcolor = "red"
    else:
        pcolor="blue"

    dataRow = rocksVMines.iloc[i, 0:60]
    dataRow.plot(color=pcolor)

plot.xlabel("Atribute Index")
plot.ylabel("Attributte Values")
plot.show()