from math import sqrt

__author__ = 'Perfecto'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

rocksVMines = pd.read_csv('sonar_all-data', header=None, prefix="V")

target = []

Correlacion_Matrix = DataFrame(rocksVMines.corr())
plot.pcolor(Correlacion_Matrix, cmap='coolwarm')
plot.colorbar()
plot.show()