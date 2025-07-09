import os
import subprocess

def convert_py_to_ipynb(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Evita que entre a la carpeta del entorno virtual
        if 'venv' in dirnames:
            dirnames.remove('venv')

        for file in filenames:
            if file.endswith('.py') and not file.startswith('convertir_jupyter'):
                full_path = os.path.join(dirpath, file)
                print(f"Convirtiendo: {full_path}")
                subprocess.run(["p2j", full_path])

# Usa raw string o doble barra para la ruta
convert_py_to_ipynb(r"C:\Users\Pabu\Desktop\mineria_datos\python-mineria-datos")
