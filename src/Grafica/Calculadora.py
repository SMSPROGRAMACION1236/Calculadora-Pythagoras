import customtkinter as ctk


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
        self.entry.configure(fg_color="#3A3F77", bg_color="#3A3F77", font=("Arial", 32), justify="right", width=363,
                             height=70, corner_radius=50)
        # self.entry.grid(row=1, column=0, columnspan=8, padx=40, pady=25, sticky = "we",anchor="center" )
        self.entry.place(relx=0.5, rely=0.15, anchor="center")

    def configuracion_botones_numerico(self):

        def agregar_al_entry(numero):
            """
            Agrega el número ingresado en el Entry
            :param numero:
            :return: None
            """
            self.entry.insert(ctk.END, numero)

        ctk.CTkButton(self, text="1", width=65, height=45, command=lambda: agregar_al_entry(1), fg_color="#404258",
                      corner_radius=40).place(x=20, y=120)
        ctk.CTkButton(self, text="2", width=65, height=45, command=lambda: agregar_al_entry(2), fg_color="#404258",
                      corner_radius=40).place(x=100, y=120)
        ctk.CTkButton(self, text="3", width=65, height=45, command=lambda: agregar_al_entry(3), fg_color="#404258",
                      corner_radius=40).place(x=180, y=120)
        ctk.CTkButton(self, text="4", width=65, height=45, command=lambda: agregar_al_entry(4), fg_color="#404258",
                      corner_radius=40).place(x=20, y=180)
        ctk.CTkButton(self, text="5", width=65, height=45, command=lambda: agregar_al_entry(5), fg_color="#404258",
                      corner_radius=40).place(x=100, y=180)
        ctk.CTkButton(self, text="6", width=65, height=45, command=lambda: agregar_al_entry(6), fg_color="#404258",
                      corner_radius=40).place(x=180, y=180)
        ctk.CTkButton(self, text="7", width=65, height=45, command=lambda: agregar_al_entry(7), fg_color="#404258",
                      corner_radius=40).place(x=20, y=240)
        ctk.CTkButton(self, text="8", width=65, height=45, command=lambda: agregar_al_entry(8), fg_color="#404258",
                      corner_radius=40).place(x=100, y=240)
        ctk.CTkButton(self, text="9", width=65, height=45, command=lambda: agregar_al_entry(9), fg_color="#404258",
                      corner_radius=40).place(x=180, y=240)
        ctk.CTkButton(self, text="0", width=65, height=45, command=lambda: agregar_al_entry(0), fg_color="#404258",
                      corner_radius=40).place(x=55, y=300)
        ctk.CTkButton(self, text=".", width=65, height=45, command=lambda: agregar_al_entry("."), fg_color="#404258",
                      corner_radius=40).place(x=145, y=300)

    def configuracion_botones_operadores(self):

        def obtener_operacion(option):
            """
            Agregar la operacion
            :param option:
            :return:  None
            """
            operator_length = len(option)  # Para soportar operaciones mas largas, que necesitan mas de una  letra.
            self.entry.insert(ctk.END, option)

        ctk.CTkButton(master=self, text="+", width=45, height=45, command=lambda: obtener_operacion("+"),
                      fg_color="#F49D1A", corner_radius=400).place(x=280, y=180)
        ctk.CTkButton(self, text="-", width=45, height=45, command=lambda: obtener_operacion("-"), fg_color="#F49D1A",
                      corner_radius=400).place(x=345, y=180)
        ctk.CTkButton(self, text="*", width=45, height=45, command=lambda: obtener_operacion("*"), fg_color="#F49D1A",
                      corner_radius=400).place(x=280, y=120)
        ctk.CTkButton(self, text="/", width=45, height=45, command=lambda: obtener_operacion("/"), fg_color="#F49D1A",
                      corner_radius=400).place(x=345, y=120)

    def configuracion_botones_especiales(self):
        def borrar_todo():
            """
            Elimina totalmente el contenido del entry
            :return:
            """
            self.entry.delete(0, ctk.END)  # Regresar al indice 0 en donde no hay nada.

        def borrar_caracter():
            """
            Elimina el ultimo caracter del contenido del entry

            :return: None
            """
            self.display_state = self.entry.get()
            if len(self.display_state):
                self.new_state = self.display_state[:-1]  # Te permite ir en un estado anterior
                borrar_todo()
                self.entry.insert(0, self.new_state)  # Ingresa el nuevo estado
            else:  # Si no hay nada para eliminar
                borrar_todo()
                self.entry.insert(0, "Error: Nada Para Eliminar!")

        def calcular():
            """
            Calcular el resultado de la expresion dentro del entry

            :return:
            """
            self.display_state = self.entry.get()  # Obtener la expression dentro del entry y guardarlo en una variable
            try:
                result = eval(self.display_state)  # Calcular el resultado
                borrar_todo()
                self.entry.insert(0, result)  # Insertar el resultado, tras eliminar anteriormente.
            except Exception:
                borrar_todo()
                self.entry.insert(0, 'Error En EL Calculo')

        ctk.CTkButton(self, text="=", width=125, height=46, command=lambda: calcular(), fg_color="#B2B2B2",
                      corner_radius=60).place(x=277, y=300)
        ctk.CTkButton(self, text="AC", width=45, height=45, command=lambda: borrar_todo(), fg_color="#5FB25F",
                      corner_radius=60).place(x=345, y=240)
        ctk.CTkButton(self, text="C", width=45, height=45, command=lambda: borrar_caracter(), fg_color="#5FB25F",
                      corner_radius=60).place(x=280, y=240)
