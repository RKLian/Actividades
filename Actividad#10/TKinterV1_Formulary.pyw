import tkinter as tk
import tkinter.messagebox as messagebox

def registrar():
    # Information gathering
    info = f"Name: {entry_name.get()}\nLast Name: {entry_lastname.get()}\nAge: {entry_age.get()}\nAddress: {entry_address.get()}\nPhone: {entry_cellphone.get()}\nGender: {entry_gender.get()}\nCity: {entry_city[listbox_city.curselection()[0]]}"
    messagebox.showinfo("Registration Information", info)

# Main window
window = tk.Tk()
window.title("Please Fill Out the Form")
window.geometry("800x600")

# Labels and Entry widgets for personal information
tk.Label(window, text="Names:").grid(row=0, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

tk.Label(window, text="Last Names:").grid(row=1, column=0)
entry_lastname = tk.Entry(window)
entry_lastname.grid(row=1, column=1)

tk.Label(window, text="Age:").grid(row=2, column=0)
entry_age = tk.Entry(window)
entry_age.grid(row=2, column=1)

tk.Label(window, text="Address:").grid(row=3, column=0)
entry_address = tk.Entry(window)
entry_address.grid(row=3, column=1)

tk.Label(window, text="Cell Phone:").grid(row=4, column=0)
entry_cellphone = tk.Entry(window)
entry_cellphone.grid(row=4, column=1)

# Radio buttons for gender selection
entry_gender = tk.StringVar()
tk.Label(window, text="Gender Identity:").grid(row=5, column=0)
tk.Radiobutton(window, text="Male", variable=entry_gender, value="Male").grid(row=5, column=1)
tk.Radiobutton(window, text="Female", variable=entry_gender, value="Female").grid(row=5, column=2)

# Listbox for selecting city
tk.Label(window, text="City of Residence:").grid(row=6, column=0)
entry_city = ["Barranquilla", "Bogota", "Medellin", "Cali", "Bucaramanga", "Cartagena"]
listbox_city = tk.Listbox(window, selectmode=tk.SINGLE, height=len(entry_city))
for city in entry_city:
    listbox_city.insert(tk.END, city)
listbox_city.grid(row=6, column=1)

# Button to submit the form
tk.Button(window, text="Register", command=registrar).grid(row=7, column=0, columnspan=2)

window.mainloop()