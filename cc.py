import tkinter as tk
from tkinter import messagebox

root = tk.Tk()


def anuluj():
    root.destroy()


def zaloguj():
    haslo = haslo_entry.get()

    if haslo == "1234":
        messagebox.showinfo("Aplikacja testowa", "Pomyślnie zalogowano!")
        root.destroy()
    else:
        messagebox.showinfo("Aplikacja testowa", "Błędne hasło")


root.title("Aplikacja testowa")
root.geometry("600x400")
root.minsize(400, 300)
root.maxsize(900, 600)

root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(3, weight=1)

label_login = tk.Label(root, text="Login", font="bold")
label_login.grid(column=1, row=1, sticky="ew", padx=60, pady=40)

login_entry = tk.Entry(root)
login_entry.grid(column=2, row=1, sticky="ew", padx=60, pady=10)

label_haslo = tk.Label(root, text="Hasło", font="bold")
label_haslo.grid(column=1, row=2, sticky="ew", padx=60, pady=40)

haslo_entry = tk.Entry(root, show="*")
haslo_entry.grid(column=2, row=2, sticky="ew", padx=60, pady=10)

button_anuluj = tk.Button(root, text="Anuluj", command=anuluj, background="black", fg="white")
button_anuluj.grid(column=1, row=3, sticky="ew", padx=10, pady=10)

button_zaloguj = tk.Button(root, text="Zaloguj", command=zaloguj, background="black", fg="white")
button_zaloguj.grid(column=2, row=3, sticky="ew", padx=10, pady=10)

root.mainloop()
