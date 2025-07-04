import pandas as pd

def leer_csv(path):
    try:
        df = pd.read_csv(path)
        print('ACCESO EXITOSO AL ARCHIVO')
        return df
    except Exception as e:
        print(f'ERROR AL LEER EL ARCHIVO CSV: ${e}')
        return None