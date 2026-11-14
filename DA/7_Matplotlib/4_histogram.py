# Histogram
import matplotlib.pyplot as plt;
import random;

data = [random.randint(1,10) for _ in range(100)];
plt.hist(data, bins= 5)
plt.title("Sample Data");
plt.show();