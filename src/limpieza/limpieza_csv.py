import numpy as np
import unicodedata
import matplotlib.pyplot as plt
import seaborn as sns


# elimina los caracteres con acentos
def remover_acentos(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)]) 


def limpiar_csv(df):

    # Analisis antes de la limpieza
    df.shape
    df.info()
    df.describe()
    df.isnull().sum()
    df.duplicated().sum()
    print("Valores nulos antes de limpieza:\n", df.isnull().sum())
    print("Duplicados antes de limpieza:", df.duplicated().sum())

    # columnas categoricas
    columnas_categoricas = df.select_dtypes(include=['object', 'category']).columns

    for col in columnas_categoricas:
        print(f'Columna {col}: {df[col].nunique()} subniveles')

    for column in df.columns:
        if column in columnas_categoricas:
            df[column] = df[column].str.lower().str.strip()
            df[column] = df[column].apply(remover_acentos)

    # cambiar los meses por numeros
    if 'mes_alto_consumo' in df.columns:
        meses = {
            'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
            'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
            'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
        }
        df['mes_alto_consumo_num'] = df['mes_alto_consumo'].map(meses)

    # columnas numericas
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns

    if 'habitantes' in df.columns:
        df = df[df['habitantes'] > 0]
    if 'consumo_kw_mes' in df.columns:
        df = df[df['consumo_kw_mes'] > 0]

    # grafico para ver los puntos que no esten en coherencia
    # for col in columnas_numericas:
    #     sns.boxplot(x=df[col])
    #     plt.title(f'Boxplot para {col}')
    #     plt.show()

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    print(df.info())
    
    return df