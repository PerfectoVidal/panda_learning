from math import sqrt

__author__ = 'Perfecto'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

rocksVMines = pd.read_csv('sonar_all-data', header=None, prefix="V")

target = []

#Calculamos la correlacion entre el 2,3
dataRow2 = rocksVMines.iloc[1,0:60]
dataRow3 = rocksVMines.iloc[2,0:60]

mean2=dataRow2.mean()
mean3=dataRow3.mean()
var2 = dataRow2.std()**2
var3 = dataRow3.std()**2

corr23 = 0
num =len(dataRow2)
for i in range(num):
    corr23+= (dataRow2[i]-mean2)* (dataRow3[i]-mean3)/(sqrt(var2*var3)*num)

print("La correlación entre la fila 2 y la fila 3 es:")
print(corr23)