# First plot bar chart:
import matplotlib.pyplot as plt;

categories = ['A', 'B', 'C', 'D', 'E'];
sales = [10,34,23, 98, 37];
y2 = [23, 34, 54, 23, 99];

plt.figure(figsize=(6,4));
plt.subplot(1,2,1); #row, column, position
plt.bar(categories,  sales);
plt.title("Data Analysis");
plt.xlabel("Catergories");
plt.ylabel("Sales");

plt.figure(figsize=(6,4));
plt.subplot(1,2,2); #row, column, position
plt.scatter(categories,  y2);
plt.title("Data Analysis");
plt.show();