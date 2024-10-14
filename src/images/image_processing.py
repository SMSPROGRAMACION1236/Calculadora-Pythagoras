from PIL import Image
import customtkinter as ctk

import os

# Obtener la ruta del directorio actual del script
base_path = os.path.dirname(os.path.abspath(__file__))
def create_path(file):
  return os.path.join(base_path, file)

black_path =create_path('black_equal.png') 
c_path = create_path('char_delete.png') 

# Debería imprimir la ruta correcta sin duplicar 'images'

# Usar la ruta construida para abrir el archivo
# try:
#     with open(black_path, 'rb') as img_file:
#         # Procesar la imagen
#         pass
# except FileNotFoundError:
#     print(f"Archivo no encontrado: {black_path}")


equal_button_path = fr"{black_path}"
# equal_button_path = r'src/images/black_equal.png'

# c_button_path = r'src/images/char_delete.png'
c_button_path = fr"{c_path}"

equal_button = ctk.CTkImage(Image.open(equal_button_path), size=(25, 25))
c_button = ctk.CTkImage(Image.open(c_button_path), size=(28, 28))
