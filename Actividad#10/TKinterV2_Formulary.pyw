import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

def registrar():
    # Information gathering
    info = f"Name: {entry_name.get()}\nLast Name: {entry_lastname.get()}\nAge: {entry_age.get()}\nAddress: {entry_address.get()}\nPhone: {entry_cellphone.get()}\nGender: {entry_gender.get()}\nCity: {entry_city[listbox_city.curselection()[0]]}"
    messagebox.showinfo("Registration Information", info)

# Main window
window = tk.Tk()
window.title("Please Fill Out the Form")
window.geometry("800x600")
window.configure(bg="#C5E1A5")

# Font & color settings
font_style = ("Helvetica", 12, "bold")
label_bg_color = "#FFCC80"
entry_bg_color = "#FFFFFF"

# Labels and Entry widgets for personal information
tk.Label(window, text="Names:", bg=label_bg_color, font=font_style).grid(row=0, column=0)
entry_name = tk.Entry(window, bg=entry_bg_color)
entry_name.grid(row=0, column=1)

tk.Label(window, text="Last Names:", bg=label_bg_color, font=font_style).grid(row=1, column=0)
entry_lastname = tk.Entry(window, bg=entry_bg_color)
entry_lastname.grid(row=1, column=1)

tk.Label(window, text="Age:", bg=label_bg_color, font=font_style).grid(row=2, column=0)
entry_age = tk.Entry(window, bg=entry_bg_color)
entry_age.grid(row=2, column=1)

tk.Label(window, text="Address:", bg=label_bg_color, font=font_style).grid(row=3, column=0)
entry_address = tk.Entry(window, bg=entry_bg_color)
entry_address.grid(row=3, column=1)

tk.Label(window, text="Cell Phone:", bg=label_bg_color, font=font_style).grid(row=4, column=0)
entry_cellphone = tk.Entry(window, bg=entry_bg_color)
entry_cellphone.grid(row=4, column=1)

# Radio buttons for gender selection
entry_gender = tk.StringVar()
def on_enter(event):
    event.widget.config(bg="#FFD54F")
def on_leave(event):
    event.widget.config(bg="#FAFAFA")

male_radio = tk.Radiobutton(window, text="Male", variable=entry_gender, value="Male", bg="#FAFAFA")
male_radio.bind("<Enter>", on_enter)
male_radio.bind("<Leave>", on_leave)
male_radio.grid(row=5, column=1)

tk.Label(window, text="Gender Identity:", bg=entry_bg_color).grid(row=5, column=0)
tk.Radiobutton(window, text="Male", variable=entry_gender, value="Male").grid(row=5, column=1)
tk.Radiobutton(window, text="Female", variable=entry_gender, value="Female").grid(row=5, column=2)

# Listbox for selecting city
def on_select(event):
    selected_index = listbox_city.curselection()
    if selected_index:
        listbox_city.itemconfig(selected_index, bg="#FFAB91", fg="#FFFFFF")

tk.Label(window, text="City of Residence:").grid(row=6, column=0)
entry_city = ["Barranquilla", "Bogota", "Medellin", "Cali", "Bucaramanga", "Cartagena"]
listbox_city = tk.Listbox(window, selectmode=tk.SINGLE, height=len(entry_city))
for city in entry_city:
    listbox_city.insert(tk.END, city)
listbox_city.grid(row=6, column=1)
listbox_city.bind("<<ListboxSelect>>", on_select)

# Icon selection
path = Image.open("Actividad#10/icon.png")
icon = ImageTk.PhotoImage(path)
window.iconphoto(True, icon)

# Button to submit the form
tk.Button(window, text="Register", command=registrar).grid(row=7, column=0, columnspan=2)

window.mainloop()

# create for Liam / Yulian Herrera Zuñiga >>> Formulary <<<