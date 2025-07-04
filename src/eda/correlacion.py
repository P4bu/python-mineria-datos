import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def correlacion(df):

    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Matriz de correlación")
    plt.show()