import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk

def ingresar():
    # Recopilación de información
    nombre_usuario = usuario_entry.get()
    info = f"Nombre de usuario: {nombre_usuario}\n"
    messagebox.showinfo("Informacion de login", info)
    
    # Mensaje de despedida
    despedida = f"¡Muchas gracias, querido usuario {nombre_usuario}, por usar mi código en fase beta!\nVuelva a usarlo cuando esté completado."
    messagebox.showinfo("Despedida", despedida)


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.title("Inicio de Sesión")
ventana.configure(bg="white")

# Colores
label_bg_color = "#FFCC80"
entry_bg_color = "#FFFFFF"

# Marco izquierdo con el logo
frame_izquierdo = tk.Frame(ventana, bg="white", padx=20, pady=20)
frame_izquierdo.pack(side="left", fill="both", expand=True)

logo = tk.PhotoImage(file="Actividad#11/login.png")
logo_label = tk.Label(frame_izquierdo, image=logo, bg="white")
logo_label.pack(pady=20)

# Imagen en la esquina derecha inferior del marco izquierdo 1
imagen_izquierda1 = Image.open("Actividad#11/decoration2.png")  # Ruta de tu imagen
imagen_izquierda1 = imagen_izquierda1.resize((120, 100), Image.Resampling.LANCZOS)  # Ajustar tamaño de la imagen
imagen_izquierda1 = ImageTk.PhotoImage(imagen_izquierda1)
imagen_izquierda_label1 = tk.Label(frame_izquierdo, image=imagen_izquierda1, bg="white")
imagen_izquierda_label1.pack(side="left", anchor="nw", padx=(0, 20), pady=(0, 20))

# Imagen en la esquina derecha inferior del marco izquierdo 2
imagen_izquierda2 = Image.open("Actividad#11/decoration.png")  # Ruta de tu imagen
imagen_izquierda2 = imagen_izquierda2.resize((120, 100), Image.Resampling.LANCZOS)  # Ajustar tamaño de la imagen
imagen_izquierda2 = ImageTk.PhotoImage(imagen_izquierda2)
imagen_izquierda_label2 = tk.Label(frame_izquierdo, image=imagen_izquierda2, bg="white")
imagen_izquierda_label2.pack(side="right", anchor="se", padx=(0, 20), pady=(0, 20))

# Texto de bienvenida
bienvenido_label = tk.Label(frame_izquierdo, text="¡Bienvenido!", font=("Microsoft YaHei UI Light", 15, "bold"), fg="#57A1F8", bg="white")
bienvenido_label.pack(side="left", anchor="se", padx=(40, 20), pady=(0, 20))

# Marco derecho para el formulario de inicio de sesión
frame_derecho = tk.Frame(ventana, bg="#A4D3EE", width=300)
frame_derecho.pack(side="right", fill="both", expand=True)

# Imagen en la parte superior del marco derecho
imagen = Image.open("Actividad#11/people.png")
imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)  # Ajustar tamaño de la imagen
imagen = ImageTk.PhotoImage(imagen)
imagen_label = tk.Label(frame_derecho, image=imagen, bg="#A4D3EE")
imagen_label.pack(pady=60)

# Título
titulo_label = tk.Label(frame_derecho, text="Inicio de sesión", font=("Microsoft YaHei UI Light", 15, "bold"), fg="white", bg="#A4D3EE")
titulo_label.pack(pady=40)
titulo_label.place(x=45, y= 20)

# Etiqueta y entrada para el usuario
usuario_label = tk.Label(frame_derecho, text="Usuario:", font=("Microsoft YaHei UI Light", 12, "bold"), fg="white", bg="#A4D3EE")
usuario_label.pack()

usuario_entry = tk.Entry(frame_derecho, bg=entry_bg_color, font=("Microsoft YaHei UI Light", 10))
usuario_entry.pack(pady=5)

# Etiqueta y entrada para la contraseña
clave_label = tk.Label(frame_derecho, text="Contraseña:", font=("Microsoft YaHei UI Light", 12, "bold"), fg="white", bg="#A4D3EE")
clave_label.pack()

clave_entry = tk.Entry(frame_derecho, show="*", bg=entry_bg_color, font=("Microsoft YaHei UI Light", 10))
clave_entry.pack(pady=5)

# Botón de ingreso
ingresar_button = tk.Button(frame_derecho, text="Ingresar", command=ingresar, font=("Microsoft YaHei UI Light", 12), fg="white", bg="#FF4040")
ingresar_button.pack(pady=20)

# Imagen 
path = Image.open("Actividad#11/people.png")
icon = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icon)


ventana.resizable(False, False)
ventana.mainloop()
