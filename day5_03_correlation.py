# Section 3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"E:\Data Analytics work\VS code work\day5\sales_cleaned.csv")
numeric_df = df.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()
#creating a heatmap
sns.heatmap(correlation_matrix,annot=True,cmap='RdYlGn')
plt.title('Variable Correlation Map')
plt.show()