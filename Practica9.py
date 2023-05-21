import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Cargar los datos en un dfFrame
df=pd.read_csv('C:/Users/Readyboi/Desktop/vgsales/vgsales.csv')


############### Wordcloud de Juegos ###################
# Obtener las palabras más comunes en la columna 'Name'
word_counts = df['Name'].value_counts()

# Crear un objeto WordCloud con las palabras más comunes
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

# Mostrar la nube de palabras en una figura
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()



############### Wordcloud de Publisher ###################
# Obtener las palabras más comunes en la columna 'Publisher'
word_counts = df['Publisher'].value_counts()

# Crear un objeto WordCloud con las palabras más comunes
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

# Mostrar la nube de palabras en una figura
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()



############### Wordcloud de Genero, Publisher, Nombre, Plataform ###################
# Obtener las palabras más comunes en la columna 'Publisher'
# Concatenate the values from 'Publisher', 'Name', 'Genre', and 'Platform' columns
combined_text = ' '.join(df['Publisher'].astype(str)) + ' ' + \
               ' '.join(df['Name'].astype(str)) + ' ' + \
               ' '.join(df['Genre'].astype(str)) + ' ' + \
               ' '.join(df['Platform'].astype(str))

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

# Mostrar la nube de palabras en una figura
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()