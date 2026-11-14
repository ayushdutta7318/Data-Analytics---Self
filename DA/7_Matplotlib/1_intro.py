# Intro: Used for data visualization and analysis of the data.

import matplotlib.pyplot as plt;
# pyplot is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

# create a simple plot

#data
x = [1, 2, 3, 4, 5];
y = [58, 78, 90, 100, 120];

plt.plot(x,y, color='red', marker='o', linestyle='solid', linewidth=2, markersize = 12);

# title in chart:
plt.title('sample data');
plt.xlabel("x-axis");
plt.ylabel("y-axis");

plt.show() #to display chart

# chart size
plt.figure(figsize = (4,3));


