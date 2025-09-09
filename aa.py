import tkinter
import tkinter as tk

root = tk.Tk()


def wyjscie():
    root.destroy()


def zmien1():
    opis.configure(width=50)


def zmien2():
    opis.configure(width=10)


root.title("Aplikacja testowa")
root.geometry("600x400")

label1 = tk.Label(root, text="abcdef", fg="white", background="red")
label1.grid(column=1, row=1)

label2 = tk.Label(root, text="qwerty")
label2.grid(column=1, row=2)

opis = tk.Entry(root, width=10)
opis.grid(column=2, row=1)

button1 = tk.Button(root, text="zamknij", command=wyjscie)
button1.grid(column=2, row=2)

button2 = tk.Button(root, text="zmien", command=zmien1)
button2.grid()

button3 = tk.Button(root, text="zmien", command=zmien2)
button3.grid()

root.mainloop()
