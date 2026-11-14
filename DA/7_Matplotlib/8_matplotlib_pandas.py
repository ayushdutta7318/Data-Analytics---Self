# Real Data with pandas and matplot
import pandas as pd;
import matplotlib.pyplot as plt;

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [435, 342, 753, 799, 501]
};

df = pd.DataFrame(data);
print(df);

plt.bar(df['Month'], df['Sales']);
plt.title("Sales Data");
plt.xlabel('Month');
plt.ylabel('Sales');
plt.savefig("monthly_sales_from_df.png");# save as image
plt.show();