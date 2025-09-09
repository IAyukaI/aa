import validators


database = []  # Lista przechowująca dane osobowe


def add_person():
   person = {}  # Tworzymy pusty słownik do przechowywania danych osoby

   person["id"] = len(database) + 1

   # Pobieranie imienia i walidacja
   while True:
       first_name = input("Imię: ").strip()
       if validators.validate_name(first_name):
           person["first_name"] = first_name
           break
       print("Błąd: Imię może zawierać tylko litery.")

   # Pobieranie nazwiska i walidacja
   while True:
       last_name = input("Nazwisko: ").strip()
       if validators.validate_name(last_name):
           person["last_name"] = last_name
           break
       print("Błąd: Nazwisko może zawierać tylko litery.")

   # Pobieranie i walidacja daty urodzenia
   while True:
       birth_date = input("Data urodzenia (YYYY-MM-DD): ").strip()
       if validators.validate_date(birth_date):
           person["birth_date"] = birth_date
           break
       print("Błąd: Niepoprawny format daty.")

   # Pobieranie PESEL i jego walidacja
   while True:
       pesel = input("PESEL: ").strip()
       if validators.validate_pesel(pesel):
           person["pesel"] = pesel
           break
       print("Błąd: PESEL musi zawierać 11 cyfr.")

   # Pobieranie płci (opcjonalne)
   person["gender"] = input("Płeć (M/K): ").strip().upper()

   # Pobieranie danych adresowych
   while True:
       person["street"] = input("Ulica: ").strip()
       if validators.validate_not_empty(person["street"]):
           break
       print("Błąd: To pole jest wymagane.")

   while True:
       person["city"] = input("Miejscowość: ").strip()
       if validators.validate_not_empty(person["city"]):
           break
       print("Błąd: To pole jest wymagane.")

   # Pobieranie numeru budynku
   while True:
       building_number = input("Nr budynku: ").strip()
       if validators.validate_not_empty(building_number):
           person["building_number"] = building_number
           break
       print("Błąd: To pole jest wymagane.")

   # Pobieranie numeru lokalu (opcjonalne)
   person["apartment_number"] = input("Nr lokalu (opcjonalnie): ").strip()

   # Pobieranie i walidacja kodu pocztowego
   while True:
       postal_code = input("Kod pocztowy (XX-XXX): ").strip()
       if validators.validate_postal_code(postal_code):
           person["postal_code"] = postal_code
           break
       print("Błąd: Niepoprawny format kodu pocztowego.")

   # Pobieranie nazwy poczty
   person["post_office"] = input("Nazwa poczty: ").strip()

   # Pobieranie i walidacja numeru telefonu
   while True:
       phone_number = input("Numer telefonu (9 cyfr): ").strip()
       if validators.validate_phone(phone_number):
           person["phone_number"] = phone_number
           break
       print("Błąd: Numer telefonu musi mieć 9 cyfr.")

   # Dodanie osoby do listy
   database.append(person)
   print("Osoba dodana pomyślnie!\n")


def show_people():
   if not database:
       print("Brak zapisanych osób.\n")
       return

   for person in database:
       print(f"ID: {person['id']}, Imię: {person['first_name']}, Nazwisko: {person['last_name']}, PESEL: {person['pesel']}")
       print(f"Data urodzenia: {person['birth_date']}, Płeć: {person['gender']}")
       print(f"Adres: {person['street']} {person['building_number']} {person['apartment_number']}, {person['postal_code']} {person['city']} ({person['post_office']})")
       print(f"Telefon: {person['phone_number']}\n")
       print("-" * 40)


def remove_person():
   pesel = input("Podaj PESEL osoby do usunięcia: ").strip()

   # Usunięcie osoby z listy
   global database
   updated_database = [person for person in database if person["pesel"] != pesel]

   if len(updated_database) == len(database):
       print("Nie znaleziono osoby z podanym PESEL.\n")
   else:
       database = updated_database
       print("Osoba została usunięta.\n")


def save_file():
    pass


def read_file():
    def read_numbers(filename):
        try:
            with open(filename) as f:
                return list(map(int, f.read().split()))
        except (FileNotFoundError, ValueError):
            print(f"Error '{filename}'")
            return []

    def write_numbers(filename, numbers):
        with open(filename, "w") as f:
            f.write(" ".join(map(str, numbers)))

    filename = input("Nazwa pliku: ")
    numbers = read_numbers(filename)
