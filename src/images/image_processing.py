from PIL import Image
import os
import customtkinter as ctk


file_path = os.path.dirname(os.path.realpath(__file__))

equal_button = ctk.CTkImage(Image.open(file_path + '/black_equal.png'), size=(25, 25))
c_button = ctk.CTkImage(Image.open(file_path + '/char_delete.png'), size=(28, 28))