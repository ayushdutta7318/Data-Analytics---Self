# Pie chart:
import matplotlib.pyplot as plt;

#data
categories = ['A', 'B', 'C', 'D', 'E'];
sales = [23, 54, 22, 78, 12];

plt.pie(sales, labels=categories, autopct="%1.2f%%");
plt.title("Sample Data");
plt.show();