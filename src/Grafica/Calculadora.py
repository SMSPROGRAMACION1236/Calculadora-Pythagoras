import tkinter as tk
import customtkinter as ctk
import ast
class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracion_inicial()
        self.configuracion_entry()
        self.configuracion_botones_numerico()
        self.configuracion_botones_operadores()
        self.configuracion_botones_especiales()


    def configuracion_inicial(self):
        self.title("Calculadora Pythagoras")
        self.geometry("410x367")
        self.configure(fg_color="#242530")
        self.resizable(False, False)
    def configuracion_entry(self):
        self.entry = ctk.CTkEntry(master=self.master)
        self.entry.configure(fg_color="#3A3F77", bg_color="#3A3F77", font=("Arial", 18), justify= "right", width= 363, height=70)
        self.entry.grid(row=1, column=0, columnspan=8, padx=40, pady=25, sticky = "we")

    def configuracion_botones_numerico(self):
        def agregar_al_entry(numero):
            self.entry.insert(tk.END, numero)

        self.button_1 = ctk.CTkButton(self, text="1", width=65, height=45, command=lambda: agregar_al_entry(1))
        self.button_1.grid(row=2, column=0)
        self.button_2 = ctk.CTkButton(self, text="2", width=65, height=45, command=lambda: agregar_al_entry(2))
        self.button_2.grid(row=2, column=1)
        self.button_3 = ctk.CTkButton(self, text="3", width=65, height=45, command=lambda: agregar_al_entry(3))
        self.button_3.grid(row=2, column=2)
        self.button_4 = ctk.CTkButton(self, text="4", width=65, height=45, command=lambda: agregar_al_entry(4))
        self.button_4.grid(row=3, column=0)
        self.button_5 = ctk.CTkButton(self, text="5", width=65, height=45, command=lambda: agregar_al_entry(5))
        self.button_5.grid(row=3, column=1)
        self.button_6 = ctk.CTkButton(self, text="6", width=65, height=45, command=lambda: agregar_al_entry(6))
        self.button_6.grid(row=3, column=2)
        self.button_7 = ctk.CTkButton(self, text="7", width=65, height=45, command=lambda: agregar_al_entry(7))
        self.button_7.grid(row=4, column=0)
        self.button_8 = ctk.CTkButton(self, text="8", width=65, height=45, command=lambda: agregar_al_entry(8))
        self.button_8.grid(row=4, column=1)
        self.button_9 = ctk.CTkButton(self, text="9", width=65, height=45, command=lambda: agregar_al_entry(9))
        self.button_9.grid(row=4, column=2)
        self.button_0 = ctk.CTkButton(self, text="0", width=65, height=45, command=lambda: agregar_al_entry(0))
        self.button_0.place(x=100, y=250)
        self.button_punto = ctk.CTkButton(self, text=".", width=65, height=45, command=lambda: agregar_al_entry("."))
        self.button_punto.place(x=40, y=250)

    def configuracion_botones_operadores(self):

        def obtener_operacion(option):
            operator_length = len(option)
            self.entry.insert(tk.END, (option))

        self.button_mas = ctk.CTkButton(master=self, text="+", width=45, height=45, command=lambda: obtener_operacion("+"))
        self.button_mas.grid(row=3, column=5)
        self.button_menos = ctk.CTkButton(self, text="-",  width=45, height=45, command=lambda: obtener_operacion("-"))
        self.button_menos.grid(row=3, column=6)
        self.button_multiplicar = ctk.CTkButton(self, text="*",  width=45, height=45,
                                                command=lambda: obtener_operacion("*"))
        self.button_multiplicar.grid(row=2, column=5)
        self.button_dividir = ctk.CTkButton(self, text="/",  width=45, height=45, command=lambda: obtener_operacion("/"))
        self.button_dividir.grid(row=2, column=6, sticky="we")

    def configuracion_botones_especiales(self):
        def borrar_todo():
            self.entry.delete(0, tk.END)

        def borrar_caracter():
            self.display_state = self.entry.get()
            if len(self.display_state):
                self.new_state = self.display_state[:-1]
                borrar_todo()
                self.entry.insert(0, self.new_state)
            else:
                borrar_todo()
                self.entry.insert(0, "Error")

        def calcular():
            self.display_state = self.entry.get()
            try:
                result = eval(self.display_state)
                borrar_todo()
                self.entry.insert(0, result)
            except Exception:
                borrar_todo()
                self.entry.insert(0, 'Error')
        self.button_igual = ctk.CTkButton(self, text="=", width=117, height=46, command=lambda: calcular())
        self.button_igual.grid(row=5, column=4, columnspan=3, sticky="we")
        self.button_borrar_todo = ctk.CTkButton(self, text="AC",  width=45, height=45, command=lambda: borrar_todo())
        self.button_borrar_todo.grid(row=4, column=6)
        self.button_borrar_ultimo_caracter = ctk.CTkButton(self, text="C",  width=45, height=45, command=lambda: borrar_caracter())
        self.button_borrar_ultimo_caracter.grid(row=4, column=5)
