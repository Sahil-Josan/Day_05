import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"E:\Data Analytics work\VS code work\day5\sales_cleaned.csv")
df.head()
# df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

df.set_index('Date', inplace=True)
weekly_sales = df['Sales'].resample('W').sum()
print("Weekly Sales Performance:\n", weekly_sales)
# visualization of Trend line 
weekly_sales.plot(kind='line',marker='o',color='teal')
plt.title('Weekly Revenue Trend')
plt.ylabel('Total Sales')
plt.show()


