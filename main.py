import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

path = "DataSet//dataSetFormat.xlsx"
dataSet = pd.read_excel(path)

max_column = len(dataSet.columns)
headerAndCol = {}
for i in range(3, max_column):
    headerAndCol[dataSet.columns[i]] = dataSet.loc[:,dataSet.columns[i]].values

figure, axis = plt.subplots(int((max_column-3)/3)+1,3)
idx = 0
for i in headerAndCol:
    mean = np.mean(headerAndCol[i])
    std = np.std(headerAndCol[i])
    dist = np.random.normal(mean, std, size=len(headerAndCol[i]))
    count, bins, ignored = axis[int(idx/3),idx%3].hist(dist, 30, density=True)
    axis[int(idx/3),idx%3].plot(bins, 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * std**2) ),linewidth=2, color='r')
    axis[int(idx/3),idx%3].set_title(i)
    idx += 1 

plt.show()

# mean = np.mean(col)
# standardDeviation = np.std(col)
# print(mean, standardDeviation)
# dist = np.random.normal(mean, standardDeviation, size=len(col))
# count, bins, ignored = plt.hist(dist, 30, density=True)
# plt.plot(bins, 1/(standardDeviation * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * standardDeviation**2) ),linewidth=2, color='r')
# plt.show()
