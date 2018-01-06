__author__ = 'Perfecto'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

rocksVMines = pd.read_csv('sonar_all-data', header=None, prefix="V")

dataRow2 = rocksVMines.iloc[1, 0:60]
dataRow3 = rocksVMines.iloc[2, 0 : 60]

plot.scatter(dataRow2, dataRow3)
plot.xlabel('2 fila')
plot.ylabel('3 fila')
plot.show()

