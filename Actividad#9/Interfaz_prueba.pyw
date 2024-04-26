from tkinter import *

def guardar_datos():
    nombre_guardado = nombre.get()
    apellido_guardado = apellido.get()
    # Guardar datos
    print("Nombre guardado:", nombre_guardado)
    print("Apellido guardado:", apellido_guardado)

master = Tk()
master.geometry("800x200")
master.title("Formulario de Datos")

# Colores
color_fondo = "#f0f0f0"
color_texto = "#333333"
color_boton = "#4CAF50"
color_boton_hover = "#45a049"

master.configure(bg=color_fondo)

# Fuentes
fuente_titulo = ("Arial", 18, "bold")
fuente_texto = ("Arial", 12)
fuente_boton = ("Arial", 12, "bold")

# Creacion de labels
l1 = Label(master, text="Nombre:", font=fuente_texto, bg=color_fondo, fg=color_texto)
l2 = Label(master, text="Apellido:", font=fuente_texto, bg=color_fondo, fg=color_texto)

# Definiendo posiciones
l1.grid(row=0, column=0, sticky=W, pady=10, padx=20)
l2.grid(row=1, column=0, sticky=W, pady=10, padx=20)

# Creando cajas de texto
nombre = Entry(master, font=fuente_texto, bg="white", fg=color_texto, relief="solid", bd=2)
apellido = Entry(master, font=fuente_texto, bg="white", fg=color_texto, relief="solid", bd=2)

# Definiendo posiciones para cajas de texto
nombre.grid(row=0, column=1, pady=10, padx=20)
apellido.grid(row=1, column=1, pady=10, padx=20)

# Botón para guardar datos
boton_guardar = Button(master, text="Guardar", font=fuente_boton, bg=color_boton, fg="white", relief="raised", bd=3, command=guardar_datos)
boton_guardar.grid(row=2, columnspan=2, pady=20)

mainloop()