import database


def main():
   while True:
       print("\n=== MENU ===")
       print("1. Dodaj osobę")
       print("2. Wyświetl wszystkie osoby")
       print("3. Usuń osobę")
       print("4. Zapisz do pliku")
       print("5. Odczytaj z pliku")
       print("6. Wyjdź")

       choice = input("Wybierz opcję: ").strip()

       if choice == "1":
           database.add_person()
       elif choice == "2":
           print("\n")
           database.show_people()
       elif choice == "3":
           database.remove_person()
       elif choice == "4":
           database.save_file()
       elif choice == "5":
           database.read_file()
       elif choice == "6":
           print("Zamykanie programu...")
           break
       else:
           print("Nieprawidłowa opcja, spróbuj ponownie.")


# Uruchamia program, jeśli plik jest wykonywany jako główny
if __name__ == "__main__":
   main()
