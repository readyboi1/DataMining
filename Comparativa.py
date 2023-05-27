import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv('C:/Users/Readyboi/Desktop/vgsales/vgsales.csv')

#separador= df1['Genre'].value_counts()
#df=separador[separador >= 30]

df=df1.sort_values(by='Year', ascending=True)
df.index=df['Year']

#print(df.head(5))

genre=df.groupby('Genre')

#unique_genreisher = df['Genre'].unique()

print(genre)
#print(unique_genreisher)



#Dibujamos una gráfica con el resultado
plt.figure(figsize=(10,7))
#Ajustamos a dividendos y splits
#df['Global_Sales'].plot()
genre['Global_Sales'].plot()
"""
for x in unique_genreisher:
    genre['Global_Sales'].plot()
"""    
"""df['EU_Sales'].plot()
df['JP_Sales'].plot()
df['NA_Sales'].plot()"""
#Configurarmos la gráfica
plt.title('Ventas globales', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Ventas', fontsize=12)

#Leyenda
plt.legend()
#Mostramos la gráfica
plt.show()
