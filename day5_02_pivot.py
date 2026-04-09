#pivot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"E:\Data Analytics work\VS code work\day5\sales_cleaned.csv")

pivot = df.pivot_table(values='Sales', index='Product', aggfunc=['sum', 'mean'])
print("---Product performance Pivot ---")
print(pivot)