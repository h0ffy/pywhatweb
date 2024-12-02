import os
import subprocess

# Especifica la ruta a la carpeta plugins
plugins_folder = 'plugins'

# Lista todos los archivos en la carpeta plugins
files = os.listdir(plugins_folder)

# Filtra solo los archivos Python (excluye los directorios y otros tipos de archivos)
files = [f for f in files if f.endswith('.py') and os.path.isfile(os.path.join(plugins_folder, f))]

# Aplica autopep8 a cada archivo
for file in files:
    file_path = os.path.join(plugins_folder, file)
    subprocess.run(['autopep8', '--in-place', '--aggressive', '--aggressive', file_path])

print("Formateo completado.")
