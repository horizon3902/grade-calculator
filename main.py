import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

def marksToGrades(headCol, dataSet):
    result = {}
    for i in range(0, 4):
        result[dataSet.columns[i]] = dataSet.loc[:,dataSet.columns[i]].values
    for i in headCol:
        arr = headCol[i]
        mean = np.mean(headerAndCol[i])
        std = np.std(headerAndCol[i])
        grade = []
        for mark in arr:
            if(mark >= mean + 1.5*std):
                grade.append("AA")
            elif(mark >= mean + std):
                grade.append("AB")
            elif(mark >= mean + 0.5*std):
                grade.append("BB")
            elif(mark >= mean):
                grade.append("BC")
            elif(mark >= mean - 0.5*std):
                grade.append("CC")
            elif(mark >= mean - std):
                grade.append("CD")
            elif(mark >= mean - 1.5*std):
                grade.append("DD")
            else:
                grade.append("FF")
        result[i] = grade
    return result
    
res = marksToGrades(headerAndCol, dataSet)
newDataSet = pd.DataFrame(res)
newDataSet.to_excel("Grades.xlsx")

