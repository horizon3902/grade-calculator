# grade-calculator
This python code will calculate the grades & will plot the normal distribution curve of the given data.
The input data should follow the pattern given in dataSetFormat.xlsx file.

The output grades will be generated in Grades.xlsx file.


Relative Grading will follow the formula:


**Score > Average +1.5 SD** gives a AA


**Average +1.5 SD > Score > Average + SD** gives AB


**Average + SD > Score > Average + 0.5 SD** gives BB


**Average + 0.5 SD > Score > Average** gives BC


**Average>Score > Average - 0.5 SD** gives CC


**Average - 0.5 SD > Score > Average - SD** gives CD


**Average - SD > Score > Average - 1.5 SD** gives DD

The program will also give the normal distribution curve for all the subjects.


**To execute the script,**

1. Clone the repo
2.  Run `pip install -r requirements.txt` on CMD in the same directory
3.  Put your marksheet in DataSet folder & rename it to `marksheet.xlsx`
4.  Run `python main.py` to execute the main script
