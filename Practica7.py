import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos en un dfFrame
df=pd.read_csv('C:/Users/Readyboi/Desktop/vgsales/vgsales.csv')

df = df[pd.notnull(df['Year'])]
df['Year']=df['Year'].astype(int)

data=df

# Agrupar los datos por género y calcular las ventas totales por año
sales_by_genre = data.groupby('Genre')['Global_Sales'].sum()

# Crear un DataFrame para almacenar las predicciones
predictions = pd.DataFrame(columns=['Year', 'Genre', 'Global_Sales'])

# Iterar por cada género y realizar las predicciones
for genre, sales in sales_by_genre.items():
    # Obtener las ventas históricas del género actual
    genre_sales = data[data['Genre'] == genre][['Year', 'Global_Sales']]
    
    # Crear un rango de años para las predicciones (5 años por delante)
    years = genre_sales['Year'].values.reshape(-1, 1)
    future_years = np.arange(max(years)+1, max(years)+6).reshape(-1, 1)
    
    # Preparar los datos para el modelo de regresión lineal
    X_train = years
    y_train = genre_sales['Global_Sales'].values
    
    # Entrenar el modelo de regresión lineal
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    
    # Realizar las predicciones para los próximos 5 años
    y_pred = regressor.predict(future_years)
    
    # Agregar las predicciones al DataFrame
    genre_predictions = pd.DataFrame({'Year': future_years.flatten(), 'Genre': genre, 'Global_Sales': y_pred})
    predictions = pd.concat([predictions, genre_predictions], ignore_index=True)

# Calcular el promedio de ventas globales para todas las predicciones
average_predictions = predictions.groupby('Year')['Global_Sales'].mean()

# Calcular el error cuadrado medio (MSE)
mse = ((data.groupby('Year')['Global_Sales'].sum() - average_predictions)**2).mean()

# Graficar las predicciones con fill_between
plt.plot(average_predictions.index, average_predictions.values, label='Predicciones')
plt.fill_between(average_predictions.index, average_predictions.values, alpha=0.3)
plt.xlabel('Año')
plt.ylabel('Ventas globales')
plt.title('Predicciones de ventas agrupadas por género')
plt.legend()
plt.show()

print("Error cuadrado medio (MSE):", mse)