__author__ = 'Perfecto'

from urllib.request import urlopen
import numpy as np
import pylab
import scipy.stats as stats

datos_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"

data = urlopen(datos_url)

xList = []
labels = []

for line in data:
    row = str(line.strip()).split(",")
    xList.append(row)

# Estadísticos descriptivos
col = 3
colData = []

for row in xList:
    colData.append(float(row[col]))

colArray = np.array(colData)

print("La media es {}".format(np.mean(colArray)))
print("La varianza es {}".format(np.std(colArray)))

# Calculamos 10 cuantiles

ntiles = 5
percentBdry = []
for i in range(ntiles + 1):
    percentBdry.append(np.percentile(colArray, i * (100) / ntiles))
print("Los 5 cuantiles son")
print(percentBdry)

# Contamos los elementos de la columna 60 que son cualitativos
col = 60
colData = []

for row in xList:
    colData.append(row[col])

unique = set(colData)
print('Las etiquetas son :{}'.format(unique))

catDict = dict(zip(list(unique), range(len(unique))))

catCount = [0] * 2
for element in colData:
    catCount[catDict[element]] += 1
print("el recuento son {}".format(catCount))

# vamos a ver los outliers de una columna

nrow = len(xList)
ncol = len(xList[0])

col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))

stats.probplot(colData, dist='norm',plot=pylab)
pylab.show()

