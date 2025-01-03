import os
import openai
<<<<<<< Updated upstream
import time

# Configuración de la clave de OpenAI
openai.api_key = "API_KEY"

# Carpetas de origen y destino
source_folder = "plugins_old"
destination_folder = "plugins"

# Crear la carpeta destino si no existe
os.makedirs(destination_folder, exist_ok=True)

# Función para listar archivos .py en una carpeta
def list_python_files(folder):
    return [f for f in os.listdir(folder) if f.endswith(".py")]

# Función para leer un archivo con manejo de codificación
def read_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

# Función para escribir un archivo con manejo de codificación
def write_file(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Obtener archivos .py de la carpeta plugins_old
source_files = list_python_files(source_folder)

# Procesar cada archivo
for filename in source_files:
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename)
   
    # Si el archivo no existe en la carpeta destino
    if not os.path.exists(destination_path):
        time.sleep(2)
        print(f"{filename}\t[PROCESS]")

        # Leer el contenido del archivo original
        try:
            file_content = read_file(source_path)
        except Exception as e:
            print(f"Error leyendo {source_path}: {e}")
            continue

        # Enviar el contenido a GPT-4 para corregir
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un asistente que arregla código Python. Solo responde con el código corregido sin añadir comentarios.",
                    },
                    {"role": "user", "content": file_content},
                ],
                temperature=0,
            )
            fixed_code = response["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error en la llamada a GPT-4: {e}")
            continue

        # Guardar el código corregido en la carpeta destino
        try:
            write_file(destination_path, fixed_code)
            print(f"Archivo corregido guardado en: {destination_path}")
        except Exception as e:
            print(f"Error escribiendo {destination_path}: {e}")

    else:
        print(f"{filename}\t[EXISTS]")
=======

# Directorio de plugins y donde se almacenarán las correcciones
plugins_dir = 'plugins_old'
plugins_fix_dir = 'plugins'
openai.api_key = ''

# Crear el directorio de plugins_fix si no existe
if not os.path.exists(plugins_fix_dir):
    os.makedirs(plugins_fix_dir)

# Listar archivos ".py" en el directorio de plugins
for file_name in os.listdir(plugins_dir):
    if file_name.endswith(".py"):
        source_file_path = os.path.join(plugins_dir, file_name)
        output_file_path = os.path.join(plugins_fix_dir, file_name)

        # Leer contenido del archivo original
        
        if not os.path.exists(output_file_path):
       #     try:
            with open(source_file_path, 'r') as f:
                code = f.read().encode(encoding="utf-8")
                
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Eres un asistente de programación experto."},
                    {"role": "user", "content": f"Arregla el siguiente código, responde solo con el código sin ninguna explicación:\n\n{code}"}
                ],
                max_tokens=1500,
                temperature=0.2
            )
            fixed_code = response.choices[0].message['content'].strip()

            # Guardar el resultado en el archivo de salida
            with open(output_file_path, 'w') as f:
                print(f"Fixed: {output_file_path}")
                f.write(fixed_code)
            #except:
            #    print(f"Error en {source_file_path}")
            #    pass
            
print("Proceso completado.")

>>>>>>> Stashed changes
