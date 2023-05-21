import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/Readyboi/Desktop/vgsales/vgsales.csv')


#########################   Promedio     #########################
#########################   Publisher    #########################
# Calcular el promedio de ventas globales por publisher
publisher_sales_avg = df.groupby('Publisher')['Global_Sales'].mean()

# Ordenar en orden descendente
publisher_sales_avg_sorted = publisher_sales_avg.sort_values(ascending=False)

# Imprimir el resultado
print(publisher_sales_avg_sorted)



#########################   Plataformas  #########################
# Calcular el promedio de ventas globales por plataforma
platform_sales_avg = df.groupby('Platform')['Global_Sales'].mean()

# Ordenar en orden descendente
platform_sales_avg_sorted = platform_sales_avg.sort_values(ascending=False)

# Imprimir el resultado
print(platform_sales_avg_sorted)




#########################   Género   #########################
# Calcular el promedio de ventas globales por plataforma
genre_sales_avg = df.groupby('Genre')['Global_Sales'].mean()

# Ordenar en orden descendente
genre_sales_avg_sorted = genre_sales_avg.sort_values(ascending=False)

# Imprimir el resultado
print(genre_sales_avg_sorted)


#########################  Moda  #########################
# Encontrar el género más vendido globalmente
most_sold_genre = df['Genre'].mode()[0]

# Imprimir el resultado
print("El género más vendido globalmente es:", most_sold_genre)

