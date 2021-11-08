import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class GradeGen:
    def __init__(self, path="DataSet//dataSetFormat.xlsx"): # initialise constructor sets path to marksheet and converts it into pandas dataframe
        self.path = path
        try:
            self.data_set = pd.read_excel(path)
        except FileNotFoundError:
            print("No such File exists on given path!")
            quit()
        self.max_column = len(self.data_set.columns)

    def load(self): # Prepares a dictionary of subject name as key and an array of marks of all students serially as value
        header_and_col = {}
        for i in range(3, self.max_column):
            header_and_col[self.data_set.columns[i]] = self.data_set.loc[:, self.data_set.columns[i]].values
        return header_and_col

    def plot(self): # Used to display normal distribution graph of all subjects
        header_and_col = self.load()
        figure, axis = plt.subplots(int((self.max_column - 3) / 3) + 1, 3)
        idx = 0
        for i in header_and_col:
            mean = np.mean(header_and_col[i]) #cal mean using numpy
            std = np.std(header_and_col[i])  #cal standard deviation using numpy
            dist = np.random.normal(mean, std, size=len(header_and_col[i])) #generate normal distribution using numpy
            count, bins, ignored = axis[int(idx / 3), idx % 3].hist(dist, 30, density=True) #position the graph at given index
            axis[int(idx / 3), idx % 3].plot(bins, 1 / (std * np.sqrt(2 * np.pi)) * np.exp(
                - (bins - mean) ** 2 / (2 * std ** 2)), linewidth=2, color='r') #plot the graph
            axis[int(idx / 3), idx % 3].set_title(i) #set the title
            idx += 1
        plt.show()

    def marks_to_grades(self):  # Makes a dictionary of grades for the given data using standard deviation
        header_col = self.load()
        result = {}
        for i in range(0, 4):
            result[self.data_set.columns[i]] = self.data_set.loc[:, self.data_set.columns[i]].values 
        for i in header_col:
            arr = header_col[i]
            mean = np.mean(header_col[i])
            std = np.std(header_col[i])
            grade = []
            for mark in arr: #conditions for different grades
                if mark >= mean + 1.5 * std:
                    grade.append("AA")
                elif mark >= mean + std:
                    grade.append("AB")
                elif mark >= mean + 0.5 * std:
                    grade.append("BB")
                elif mark >= mean:
                    grade.append("BC")
                elif mark >= mean - 0.5 * std:
                    grade.append("CC")
                elif mark >= mean - std:
                    grade.append("CD")
                elif mark >= mean - 1.5 * std:
                    grade.append("DD")
                else:
                    grade.append("FF")
            result[i] = grade
        return result
    
    def write_to_excel(self):   # Makes an excel sheet from a dictionary
        result = self.marks_to_grades()
        df = pd.DataFrame(result)
        df.to_excel("Grades.xlsx")


if __name__ == "__main__":
    marks = GradeGen()
    marks.plot()
    marks.write_to_excel()