import re  # Import biblioteki do obsługi wyrażeń regularnych
from datetime import datetime


def validate_name(name):
   return name.isalpha()


def validate_date(date_str):
   try:
       datetime.strptime(date_str, "%Y-%m-%d")
       return True
   except ValueError:
       return False


def validate_pesel(pesel):
   return pesel.isdigit() and len(pesel) == 11


def validate_postal_code(code):
   return bool(re.match(r"^\d{2}-\d{3}$", code))


def validate_phone(phone):
   return bool(re.match(r"^\d{9}$", phone))


def validate_not_empty(value):
   return bool(value.strip())
