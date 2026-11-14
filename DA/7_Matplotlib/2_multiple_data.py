# Multiple Plots:
import matplotlib.pyplot as plt;

# more chart data:
q = [1,2,3,4,5];
w1 = [34,65,7,435,22]; #data for year 2024
w2 = [76, 85, 234, 57, 3]; # data for year 2025

plt.plot(q, w1, label = "Sales Data 2024"); #plot for year 2024
plt.plot(q, w2, label = "Sales Data 2025"); #plot for year 2025

plt.title("Year-On-Year Sales");
plt.xlabel("Months");
plt.ylabel("Sales");
plt.legend();
plt.show();