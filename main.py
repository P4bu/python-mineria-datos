from src.manejo_archivo.lector_csv import leer_csv
from src.limpieza.limpieza_csv import limpiar_csv
from src.manejo_archivo.guardar_csv import guardar_csv
from src.limpieza.analisis_outliers import resumen_outliers
from src.limpieza.limitar_outliers import capar_outliers
from src.eda.analisis_exploratorio import eda
from src.eda.correlacion import correlacion
from src.modelos.regresion import regresion_lineal
from src.modelos.kmeans import kmeans

def main():
    print('Evaluacion N°2 Mineria de Datos.')
    print('PARA INSTALAR LAS LIBRERIAS / pip install -r requirements.txt')

    path = './data/original/datos_consumo_energetico.csv'
    path_limpio = './data/procesado/datos_consumo_energetico_limpio.csv'

    df = leer_csv(path)

    if df is not None:
        # limpiar
        df_limpio = limpiar_csv(df)

        df_outliers = resumen_outliers(df_limpio)
        df_sin_outliers = capar_outliers(df_outliers)

        # guardar
        print(df_sin_outliers)
        guardar_csv(df, path_limpio)
    else:
        print('NO SE PUDO TRABAJAR EL ARCHIVO')

    # analisis exploratorio

    df_limpio = leer_csv(path_limpio)

    if df_limpio is not None:
        eda(df_limpio)
        correlacion(df_limpio)

        # aplicacion de un modelo
        regresion_lineal(df_limpio)
        kmeans(df_limpio)
    else:
        print('NO SE PUEDE TRABAJAR CON EL ARCHIVO')
        

if __name__ == '__main__':
    main()