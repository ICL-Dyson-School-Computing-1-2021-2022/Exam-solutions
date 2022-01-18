'''
PlotQuestionSolution.py

Corresponding solution file for PlotQuestion.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

'''

# Write a Python script that reads in the text file `data.txt`, in the folder Data, and generates 
# one plot as shown in image.png
# 
# Read the text file (hint: the delimiter in the file is `','`) and notice that there are 8 columns. 
# The last column represents the time of the measurement, whereas the other columns represent data collected at that specific time. 
# To get maximum marks you need to be sure that the code you write can be executed on a 
# computer different than yours (meaning, do not use absolute paths when opening and closing directories).
# 
#   - Plot the data contained in the 3rd column against the data contained in the 8th column (i.e., 
#   data in the 3rd column on the y axis, data in the 8th column on the x axis). This should be plotted in blue.
#   - Plot the data contained in the 5th column against the data contained in the 1st column (i.e., 
#   data in the 5th column on the y axis, data in the 8th column on the x axis). This should be plotted in red.
#   - Add an xlabel as "Time [s]" and a ylabel as "Force [N]"
#


from matplotlib import pyplot as plt
import os

# go in the appropriate directory. Notice that, depending on which directory you start, you might have wanted to not use the first 
# os.chdir()

os.chdir("Plot question")
os.chdir("Data")                                                       
                                                                                                
with open("data.txt", "r") as f:
    # read the file
    lines = f.readlines()

# create a list for the numbers we are interested in
time = []
third = []
fifth = []
for line in lines:
    # read line by line and add the elements to the appropriate list
    data = line.split(",")
    time.append(float(data[7]))
    third.append(float(data[2]))
    fifth.append(float(data[4]))

# plot the values

plt.plot(third, time, "blue")
plt.plot(fifth, time, "red")
plt.xlabel("Time [s]")
plt.ylabel("Force [N]")
plt.show()