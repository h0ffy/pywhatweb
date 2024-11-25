import os
import subprocess
import argparse
import logging
import requests  # Asegúrate de tener la biblioteca requests instalada

# Configuración de logging
logging.basicConfig(filename='plugin_formatting.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    """Ejecuta un comando y maneja errores, mostrando la salida."""
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        logging.info(f"Ejecutado: {' '.join(command)}")
        print(result.stdout)  # Mostrar salida estándar
    except subprocess.CalledProcessError as e:
        logging.error(f"Error al ejecutar {' '.join(command)}: {e}")
        print(e.stderr)  # Mostrar salida de error

def send_to_blackboxia(file_path):
    """Envía el código a Blackboxia para su corrección."""
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        
        # Suponiendo que Blackboxia tiene un endpoint para recibir código
        response = requests.post('https://api.blackboxia.com/correct', json={'code': code})

        # Comprobar el estado de la respuesta
        if response.status_code == 200:
            corrected_code = response.json().get('corrected_code')
            with open(file_path, 'w') as file:
                file.write(corrected_code)
            logging.info(f"Código corregido por Blackboxia en {file_path}")
            print(f"Código corregido por Blackboxia en {file_path}")
        else:
            logging.error(f"Error al enviar a Blackboxia: {response.status_code} - {response.text}")
            print(f"Error al enviar a Blackboxia: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error de conexión al enviar a Blackboxia: {e}")
        print(f"Error de conexión al enviar a Blackboxia: {e}")
    except Exception as e:
        logging.error(f"Error al leer el archivo {file_path} o enviar a Blackboxia: {e}")
        print(f"Error al leer el archivo {file_path} o enviar a Blackboxia: {e}")



def main(plugins_folder, tools):
    """Función principal para formatear y revisar archivos Python en la carpeta de plugins."""
    # Lista todos los archivos en la carpeta plugins
    files = os.listdir(plugins_folder)

    # Filtra solo los archivos Python (excluye los directorios y otros archivos)
    python_files = [f for f in files if f.endswith('.py') and os.path.isfile(os.path.join(plugins_folder, f))]

    # Formatea y revisa cada archivo Python
    for file in python_files:
        file_path = os.path.join(plugins_folder, file)
        print(f"Formatear y Corregir {file_path}")

        if 'isort' in tools:
            run_command(['isort', file_path])

        if 'pycodestyle' in tools:
            run_command(['pycodestyle', file_path])

        if 'autopep8' in tools:
            run_command(['autopep8', '--in-place', '--aggressive', '--aggressive', file_path])
        
        if 'pylint' in tools:
            run_command(['pylint', file_path])


        """
        if 'black' in tools:
            run_command(['black', file_path])
        if 'flake8' in tools:
            run_command(['flake8', file_path])

        """
        if 'pytest' in tools:
            run_command(['pytest', file_path])

        if 'mypy' in tools:
            run_command(['mypy', file_path])

        """
        if 'bandit' in tools:
            run_command(['bandit', '-r', plugins_folder])  # Ejecutar bandit en toda la carpeta
        # Enviar el código a Blackboxia para corrección
        send_to_blackboxia(file_path)
        """

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Formatear y revisar archivos Python en una carpeta de plugins.')
    parser.add_argument('plugins_folder', type=str, help='Ruta a la carpeta de plugins')
    parser.add_argument('--tools', nargs='*', default=['autopep8', 'pylint', 'black', 'flake8', 'pytest', 'mypy', 'pycodestyle', 'isort', 'bandit'],
                        help='Lista de herramientas a ejecutar (por defecto: autopep8 pylint black flake8 pytest mypy pycod estyle isort bandit)')
    args = parser.parse_args()

    # Verificar si la carpeta existe
    if not os.path.exists(args.plugins_folder):
        logging.error(f"La carpeta {args.plugins_folder} no existe.")
    else:
        main(args.plugins_folder, args.tools)