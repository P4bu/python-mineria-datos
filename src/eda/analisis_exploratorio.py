import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def eda(df):
    
    # distribucion del consumo mensual
    sns.histplot(df['consumo_kw_mes'], kde=True)
    plt.title("Distribución de consumo mensual (kW)")
    plt.xlabel("kW/mes")
    plt.show()

    # promedio de consumo por ciudad
    plt.figure(figsize=(10,6))
    df.groupby('ciudad')['consumo_kw_mes'].mean().sort_values().plot(kind='barh')
    plt.title("Consumo promedio por ciudad")
    plt.xlabel("kW/mes")
    plt.show()

    # comparacion zona rural vs urbana
    sns.boxplot(data=df, x='zona', y='consumo_kw_mes')
    plt.title("Consumo por zona")
    plt.show()

    promedio_zona = df.groupby('zona')['consumo_kw_mes'].mean().reset_index()
    sns.barplot(data=promedio_zona, x='zona', y='consumo_kw_mes', palette='Set2')
    plt.title("Promedio mensual de consumo por zona (kW)")
    plt.xlabel("Zona")
    plt.ylabel("Consumo promedio (kW/mes)")
    plt.tight_layout()
    plt.show()