import pandas as pd

def resumen_outliers(df):
    columnas_numericas = df.select_dtypes(include=['int64', 'float64']).columns
    outliers_resumen = []

    for col in columnas_numericas:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lim_inf = Q1 - 1.5 * IQR
        lim_sup = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lim_inf) | (df[col] > lim_sup)]
        porcentaje = round(len(outliers) / len(df) * 100, 2)

        outliers_resumen.append({
            'columna': col,
            'Q1': round(Q1, 2),
            'Q3': round(Q3, 2),
            'IQR': round(IQR, 2),
            'lim_inf': round(lim_inf, 2),
            'lim_sup': round(lim_sup, 2),
            'outliers': len(outliers),
            '% outliers': porcentaje
        })

    return pd.DataFrame(outliers_resumen).sort_values(by='% outliers', ascending=False)
