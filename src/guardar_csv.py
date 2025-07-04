def guardar_csv(df, path, index=False):
    try:
        df.to_csv(path, index=index)
        print('ARCHIVO GUARDADO CON EXITO')
    except Exception as e:
        print(f'ERROR AL GUARDAR EL ARCHIVO: ${e}')