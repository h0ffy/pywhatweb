import os

# Especifica la ruta a la carpeta plugins
plugins_folder = 'whatwebstalker/plugins'

# Lista todos los archivos en la carpeta plugins
files = os.listdir(plugins_folder)

# Filtra solo los archivos (excluye los directorios)
files = [f for f in files if os.path.isfile(os.path.join(plugins_folder, f))]

# Imprime la lista de archivos
print("Archivos en la carpeta plugins:")
for file in files:
    print(file)
