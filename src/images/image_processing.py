# from PIL import Image
# import os
# import customtkinter as ctk
#
#
# file_path = os.path.dirname(os.path.realpath(__file__))
#
# equal_button = ctk.CTkImage(Image.open(file_path + '/black_equal.png'), size=(25, 25))
# c_button = ctk.CTkImage(Image.open(file_path + '/char_delete.png'), size=(28, 28))

# image_resources.py

import os
import sys
from PIL import Image
import customtkinter as ctk

# Define la ruta directamente
equal_button_path = r'C:\Users\santi\Programación\Proyectos\Calculadora-Pythagoras\src\images\black_equal.png'
c_button_path = r'C:\Users\santi\Programación\Proyectos\Calculadora-Pythagoras\src\images\char_delete.png'
# Carga las imágenes
equal_button = ctk.CTkImage(Image.open(equal_button_path), size=(25, 25))
c_button = ctk.CTkImage(Image.open(c_button_path), size=(28, 28))
