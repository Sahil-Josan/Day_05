#Section 4: The Experiment
##Day 5: Exploratory Data Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"E:\Data Analytics work\VS code work\day5\sales_cleaned.csv")

top_3 = df.groupby('Product')['Sales'].sum().nlargest(3)
print(top_3)

top_3.plot(kind='bar')
import matplotlib.pyplot as plt
plt.title('Top 3 Products by Sales')
plt.ylabel('Total Sales')
plt.show()
##Top 3 products by sales are Mouse,UPS,and Monitor

#correlation doesn't mean that one causes the other to sell.
#  It means that both variables move together,but the demand,
#  seasonlity, and other factors can influence sales. '
#For example, if there is a promotion on Mouse,
#  it might lead to an increase in sales of UPS and
#  Monitor as well, but it doesn't necessarily mean 
# that the sales of Mouse are causing the sales of UPS 
# and Monitor to increase.

# Causation can be established through experiments,
# for example, sales of ice cream and the summer season are correlated, 
# but the summer season causes an increase in ice cream sales