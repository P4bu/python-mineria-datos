import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def regresion_lineal(df):

    # Codificar variables categoricas
    df_model = df.copy()
    for col in ['ciudad', 'zona', 'tipo_hogar']:
        df_model[col] = LabelEncoder().fit_transform(df_model[col])

    # Variables predictoras y objetivo
    X = df_model[['habitantes', 'metraje_m2', 'zona', 'tipo_hogar']]
    y = df_model['consumo_kw_mes']

    # Modelo
    modelo = LinearRegression()
    modelo.fit(X, y)
    y_pred = modelo.predict(X)

    # Evaluacion
    mse = mean_squared_error(y, y_pred)
    print("MSE:", mse)

    # Coeficientes
    for name, coef in zip(X.columns, modelo.coef_):
        print(f"{name}: {coef:.2f}")