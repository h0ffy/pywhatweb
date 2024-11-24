import os
import subprocess

# Especifica la ruta a la carpeta plugins
plugins_folder = 'whatwebstalker/plugins'

# Lista todos los archivos en la carpeta plugins
files = os.listdir(plugins_folder)

# Filtra solo los archivos Python (excluye los directorios y otros archivos)
python_files = [f for f in files if f.endswith('.py') and os.path.isfile(os.path.join(plugins_folder, f))]

# Formatea y revisa cada archivo Python
for file in python_files:
    file_path = os.path.join(plugins_folder, file)
    print(f"Format and Fix {file_path}")

    # Fix via autopep8
    try:
        subprocess.run(['autopep8', '--in-place', '--aggressive', '--aggressive', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running autopep8 on {file_path}: {e}")
        pass
    # Fix via pylint
    try:
        subprocess.run(['pylint', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running pylint on {file_path}: {e}")
        pass
    # Fix via black    
    try:
        subprocess.run(['black', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running black on {file_path}: {e}")
        pass
    # Fix via flake8
    try:
        subprocess.run(['flake8', file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running flake8 on {file_path}: {e}")
        pass