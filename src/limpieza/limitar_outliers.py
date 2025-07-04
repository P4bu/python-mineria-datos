import pandas as pd

# limitar los valores extremos de las columnas
def capar_outliers(df):
    df_caped = df.copy()
    columnas_numericas = df_caped.select_dtypes(include=['int64', 'float64']).columns

    for col in columnas_numericas:
        Q1 = df_caped[col].quantile(0.25)
        Q3 = df_caped[col].quantile(0.75)
        IQR = Q3 - Q1
        lim_inf = Q1 - 1.5 * IQR
        lim_sup = Q3 + 1.5 * IQR

        # aplicacion de capado
        df_caped[col] = df_caped[col].clip(lower=lim_inf, upper=lim_sup)

    return df_caped
