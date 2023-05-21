import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import iplot
import plotly.graph_objs as go

df=pd.read_csv('C:/Users/Readyboi/Desktop/vgsales/vgsales.csv')

# Realizar la regresión lineal
model = sm.formula.ols(formula='Global_Sales ~ Year + Genre', data=df).fit()

# Crear un dataframe con los años y géneros únicos
unique_years = df['Year'].unique()
unique_genres = df['Genre'].unique()
df_plot = pd.DataFrame(columns=['Year', 'Genre', 'Global_Sales'])

# Calcular las ventas globales predichas para cada combinación de año y género
for year in unique_years:
    for genre in unique_genres:
        df_temp = pd.DataFrame([[year, genre]], columns=['Year', 'Genre'])
        df_plot = pd.concat([df_plot, df_temp], ignore_index=True)

df_plot['Global_Sales'] = model.predict(df_plot)

# Crear la gráfica de puntos
plt.figure(figsize=(10, 6))
for genre in unique_genres:
    plt.scatter(df_plot[df_plot['Genre'] == genre]['Year'], df_plot[df_plot['Genre'] == genre]['Global_Sales'], label=genre)

plt.xlabel('Año')
plt.ylabel('Ventas Globales')
plt.title('Comportamiento de Ventas Globales por Género a lo largo de los Años')
plt.legend()
plt.show()

"""
fig={
    "data" : [
    {
        'x': df.Rank,
        'y': df.Year,
        'mode': 'markers',
        'marker': {
            "color":df.Global_Sales,
            'size': df.Global_Sales,
            'showscale': True,
            "colorscale":'Blackbody'
        },
        "text" :  "Name:"+ df.Name +","+" Publisher:" + df.Publisher
        
    },
],
"layout":
    {
    "title":"Release Years of Top 100 Video Games According to Global Sales",
    "xaxis":{
        "title":"Rank",
        "gridcolor":'rgb(255, 255, 255)',
        "zerolinewidth":1,
        "ticklen":5,
        "gridwidth":2,
    },
    "yaxis":{
        "title":'Years',
        "gridcolor":'rgb(255, 255, 255)',
        "zerolinewidth":1,
        "ticklen":5,
        "gridwidth":2,
    },
    
    "paper_bgcolor":'rgb(243, 243, 243)',
    "plot_bgcolor":'rgb(243, 243, 243)'
    }}

iplot(fig)
"""
trace1 = go.Scatter(
                    x = df.Rank,
                    y = df.NA_Sales,
                    mode = "markers",
                    name = "North America",
                    marker = dict(color = 'rgba(28, 149, 249, 0.8)',size=8),
                    text= df.Name)

trace2 = go.Scatter(
                    x = df.Rank,
                    y = df.EU_Sales,
                    mode = "markers",
                    name = "Europe",
                    marker = dict(color = 'rgba(249, 94, 28, 0.8)',size=8),
                    text= df.Name)
trace3 = go.Scatter(
                    x = df.Rank,
                    y = df.JP_Sales,
                    mode = "markers",
                    name = "Japan",
                    marker = dict(color = 'rgba(150, 26, 80, 0.8)',size=8),
                    text= df.Name)
trace4 = go.Scatter(
                    x = df.Rank,
                    y = df.Other_Sales,
                    mode = "markers",
                    name = "Other",
                    marker = dict(color = 'lime',size=8),
                    text= df.Name)
                    

data = [trace1, trace2,trace3,trace4]
layout = dict(title = 'North America, Europe, Japan and Other Sales of Top 100 Video Games',
              xaxis= dict(title= 'Rank',ticklen= 5,zeroline= False,zerolinewidth=1,gridcolor="white"),
              yaxis= dict(title= 'Sales(In Millions)',ticklen= 5,zeroline= False,zerolinewidth=1,gridcolor="white",),
              paper_bgcolor='rgb(243, 243, 243)',
              plot_bgcolor='rgb(243, 243, 243)' )
fig = dict(data = data, layout = layout)
iplot(fig)