import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
df=pd.read_csv('C:/Users/Readyboi/Desktop/vgsales/vgsales.csv')
##print(df)

###################################################################
##Contar plataformas
counts_plat= df['Platform'].value_counts()
##print(counts_plat)
"""plt.title("Creación de juegos por plataformas")
plt.xlabel("Plataformas")
plt.ylabel("Cantidad")
plt.bar(counts_plat.index, counts_plat.values)
plt.show()
"""
###################################################################
##Contar Año
counts_year= df['Year'].value_counts()
##print(counts_year)
"""plt.title("Juegos creados por año")
plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.bar(counts_year.index, counts_year.values)
plt.show()
"""

###################################################################
"""##Contar Género
counts_genre= df['Genre'].value_counts()

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

data = counts_genre.values
genero = counts_genre.index

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, genero,
          title="Género",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Division por géneros")
plt.show()
"""
###################################################################
##Contar Publicador
df1=df
counts_publisher= df1['Publisher'].value_counts()

df_aux1=counts_publisher[counts_publisher < 130]
df_aux2=counts_publisher[counts_publisher >= 130]

small_sums=pd.Series([df_aux1.sum()], index=["Other (less than 130 units)"])

df_aux2 = pd.concat([df_aux2,small_sums], ignore_index=False)

print(df_aux2)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

data = df_aux2.values
publisher = df_aux2.index

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, publisher,
          title="Publisher",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Titulos lanzados por publicadores")
plt.show()

