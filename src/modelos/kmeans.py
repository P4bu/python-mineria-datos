import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def kmeans(df):

    # Clustering según consumo, metraje y habitantes
    X_kmeans = df[['habitantes', 'metraje_m2', 'consumo_kw_mes']]

    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(X_kmeans)
    df['grupo_consumo'] = clusters

    # Visualización
    sns.scatterplot(data=df, x='metraje_m2', y='consumo_kw_mes', hue='grupo_consumo', palette='Set2')
    plt.title("Agrupación de hogares por consumo")
    plt.show()

    # Silhouette score opcional
    print("Silhouette Score:", silhouette_score(X_kmeans, clusters))