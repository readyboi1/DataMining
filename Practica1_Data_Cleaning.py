import pandas as pd 
import numpy as np 
df=pd.read_csv('C:/Users/Readyboi/Desktop/vgsales/vgsales.csv')
print(df)
## La columna del rango es bastante prescindible para un análisis
df = df.drop(['Rank','EU_Sales', 'JP_Sales', 'NA_Sales', 'Other_Sales'], axis=1)
#df.drop('Rank', inplace=True, axis=1)
print(df)