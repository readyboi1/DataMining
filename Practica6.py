import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt




# Cargar los datos en un dfFrame
df=pd.read_csv('C:/Users/Readyboi/Desktop/vgsales/vgsales.csv')

# Preprocesamiento de datos
X = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]  # Variables independientes
y = df['Genre']  # Variable objetivo

# Convertir las etiquetas de texto en valores numéricos
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Escalado de características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y ajustar el clasificador k-NN
k = 3  # Número de vecinos a considerar
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled, y_train)

# Predecir las etiquetas de clase para los datos de prueba
y_pred = knn.predict(X_test_scaled)

# Calcular la precisión (accuracy) del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión (accuracy):", accuracy)

# Crear una gráfica de puntos para visualizar las predicciones
plt.scatter(X_test['NA_Sales'], X_test['EU_Sales'], c=y_pred)
plt.xlabel('NA_Sales')
plt.ylabel('EU_Sales')
plt.title('Predicciones de k-NN')
plt.show()