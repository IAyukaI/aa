import tkinter as tk
from tkinter import messagebox
from funkcje import sil, fib, nwd, pali

# Funkcja do aktualizowania widoczności drugiego pola wejściowego w zależności od wybranej operacji
def update_inputs():
    operation = operation_var.get()  # Pobranie aktualnie wybranej operacji
    if operation == "NWD":
        # Jeśli wybrana operacja to NWD, pokaż drugie pole wejściowe i jego etykietę
        entry2_label.grid(row=2, column=0, padx=10, pady=10)
        entry2.grid(row=2, column=1, padx=10, pady=10)
    else:
        # Jeśli wybrana jest inna operacja, ukryj drugie pole wejściowe i jego etykietę
        entry2_label.grid_forget()
        entry2.grid_forget()

# Funkcja do wykonania obliczeń na podstawie wybranej operacji
def calculate():
    operation = operation_var.get()  # Pobranie aktualnie wybranej operacji
    if operation == "Silnia":
        try:
            # Pobierz wartość z pierwszego pola i oblicz silnię
            n = int(entry1.get())
            result = sil(n)
        except ValueError:
            # Jeśli użytkownik wprowadził niepoprawne dane, wyświetl komunikat o błędzie
            result = "Wprowadź poprawną liczbę całkowitą"
    elif operation == "Fibonacci":
        try:
            # Pobierz wartość z pierwszego pola i oblicz n-ty wyraz ciągu Fibonacciego
            n = int(entry1.get())
            result = fib(n)
        except ValueError:
            result = "Wprowadź poprawną liczbę całkowitą"
    elif operation == "NWD":
        try:
            # Pobierz wartości z obu pól i oblicz ich największy wspólny dzielnik
            a = int(entry1.get())
            b = int(entry2.get())
            result = nwd(a, b)
        except ValueError:
            result = "Wprowadź poprawne liczby całkowite"
    elif operation == "Palindrom":
        # Pobierz wartość z pierwszego pola i sprawdź, czy jest palindromem
        num = entry1.get()
        result = pali(num)
    else:
        # Obsługa przypadku, gdy operacja jest nieznana (teoretycznie nie powinno się zdarzyć)
        result = "Niepoprawna operacja"

    # Wyświetlenie wyniku w oknie dialogowym
    messagebox.showinfo("Wynik", f"Wynik: {result}")


root = tk.Tk()  # Tworzenie głównego okna aplikacji
root.title("Kalkulator matematyczny")  # Ustawienie tytułu okna
root.resizable(False, False)  # Zablokowanie możliwości zmiany rozmiaru okna

tk.Label(root, text="Wybierz operację:").grid(row=0, column=0, padx=10, pady=10)  # Etykieta dla wyboru operacji
operation_var = tk.StringVar(value="Silnia")  # Zmienna do przechowywania aktualnie wybranej operacji (domyślnie "Silnia")
operations_menu = tk.OptionMenu(root, operation_var, "Silnia", "Fibonacci", "NWD", "Palindrom", command=lambda _: update_inputs())  # Menu rozwijane z listą operacji
operations_menu.grid(row=0, column=1, padx=10, pady=10)  # Umieszczenie menu w oknie

tk.Label(root, text="Pierwsza liczba:").grid(row=1, column=0, padx=10, pady=10)  # Etykieta dla pierwszego pola wejściowego
entry1 = tk.Entry(root)  # Pole tekstowe do wprowadzenia pierwszej liczby
entry1.grid(row=1, column=1, padx=10, pady=10)  # Umieszczenie pola w oknie

entry2_label = tk.Label(root, text="Druga liczba: ")  # Etykieta dla drugiego pola wejściowego
entry2 = tk.Entry(root)  # Pole tekstowe do wprowadzenia drugiej liczby (ukryte domyślnie)

calculate_button = tk.Button(root, text="Oblicz", command=calculate)  # Przycisk, który uruchamia funkcję `calculate`
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)  # Umieszczenie przycisku w oknie

update_inputs()

root.mainloop()
