import tkinter
import tkinter as tk

root = tk.Tk()


def wyjscie():
    root.destroy()


root.title("Aplikacja testowa")
root.geometry("600x400")

ramka = tkinter.Label(root, fg="yellow")
ramka.pack(tkinter.BOTTOM. )


button1 = tk.Button(ramka, text="zamknij", command=wyjscie)
button1.pack(tkinter.RIGHT.  )

root.mainloop()
