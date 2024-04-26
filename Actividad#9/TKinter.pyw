import tkinter as tk
from PIL import Image, ImageTk


def change_text():
    widget.config(text="¡Changed text!")

def obtein_text():
    entered_text = text_box.get()
    widget.config(text="Entered: " + entered_text)

def get_selection():
    selected = list_box.curselection()
    for index in selected:
        element = list_box.get(index)
        print("Selected item:", element)

def get_status():
    if variable.get() == 1:
        print("The checkbox is selected")
    else:
        print("Checkbox is not selected")

def get_selection():
    selection = variable.get()
    if selection == 1:
        print("Option 1 selected")
    elif selection == 2:
        print("Option 2 selected")
    elif selection == 3:
        print("Option 3 selected")


Window = tk.Tk()
variable = tk.IntVar()


option1 = tk.Radiobutton(Window, text="Option 1", variable=variable, value=1, command=get_selection)
option1.pack()

option2 = tk.Radiobutton(Window, text="Option 2", variable=variable, value=2, command=get_selection)
option2.pack()

option3 = tk.Radiobutton(Window, text="Option 3", variable=variable, value=3, command=get_selection)
option3.pack()


checkbox = tk.Checkbutton(Window, text="Option 1", variable=variable, command=get_status)
checkbox.pack()

list_box = tk.Listbox(Window, width=30, selectmode="multiple")
list_box.pack()

elements = ["Element 1", "Element 2", "Element 3", "Element 4"]

for element in elements:
    list_box.insert(tk.END, element)

boton = tk.Button(Window, text="Obtain", command=get_selection)
boton.pack()


# Crear un marco con borde sólido
frame1 = tk.Frame(Window, width=200, height=100, bd=2, relief="solid")
frame1.pack()

# Agregar una etiqueta al marco1
widget1 = tk.Label(frame1, text="Frame 1")
widget1.pack()
widget3 = tk.Label(frame1, text="Frame 1")
widget3.pack()

# Crear un marco con borde en relieve
frame2 = tk.Frame(Window, width=200, height=100, bd=2, relief="raised")
frame2.pack()

# Agregar una etiqueta al marco2
widget2 = tk.Label(frame2, text="Frame 2")
widget2.pack()


#Agrega un icono a la ventana
widget = tk.Label(Window, text="Original text")
widget.pack()
label = tk.Label(Window, text="Entered text: ")
label.pack()

text_box = tk.Entry(Window, width=30)
text_box.pack()

button = tk.Button(Window, text="Obtein text", command=obtein_text)
button.pack()


#Crea un botón con texto y función de comando
button1 = tk.Button(Window, text="Change", command=change_text)
button1.pack()
button2 = tk.Button(Window, text="button 2", bg="blue", fg="white", font=("Arial", 12))
button2.pack()
button3 = tk.Button(Window, text="disabled", state="disabled")
button3.pack()
widget= tk.Label(Window, text="¡Hello, guys!", bg="gray", fg="white", font=("Times New Roman", 20), width=22, height=2, anchor="center")
widget.pack()

path = Image.open("Actividad#9/icon.png")
icon = ImageTk.PhotoImage(path)
Window.iconphoto(True, icon)
Window.title("RKWindow")

screen_width = Window.winfo_screenwidth()
screen_height = Window.winfo_screenheight()

Window.geometry(f"{screen_width}x{screen_height}")
Window.resizable(True, True)
Window.config(bg="gray")
Window.mainloop()
