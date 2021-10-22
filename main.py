import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class LoadData:
    def __init__(self, path = "DataSet//dataSetFormat.xlsx"):
        self.path = path
        self.dataSet = pd.read_excel(path)
        self.max_column = len(self.dataSet.columns)
        
    def load(self):
        headerAndCol = {}
        for i in range(3, self.max_column):
            headerAndCol[self.dataSet.columns[i]] = self.dataSet.loc[:,self.dataSet.columns[i]].values
        return headerAndCol

class PlotData:
    def plot():
        obj = LoadData()
        headerAndCol = obj.load()
        figure, axis = plt.subplots(int((obj.max_column-3)/3)+1,3)
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

class GradeCalculator():
    def marks_to_grades():
        obj = LoadData()
        headerAndCol = obj.load()
        result = {}
        for i in range(0, 4):
            result[obj.dataSet.columns[i]] = obj.dataSet.loc[:,obj.dataSet.columns[i]].values
        for i in headerAndCol:
            arr = headerAndCol[i]
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
        
res = GradeCalculator.marks_to_grades()
newDataSet = pd.DataFrame(res)
newDataSet.to_excel("Grades.xlsx")
PlotData.plot()