# Task 1: Calculate the number of days from today to a given date
from datetime import datetime

# Function that calculates the difference in days between a given date and today
def get_days_from_today(date):
    try:
        # Parse the input date string into a datetime object
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        # Calculate the difference between the given date and today
        delta_date = date - today
        # Return the number of days from the difference
        return delta_date.days
    except ValueError:
        # Handle invalid date format
        print("Invalid date format. Please use YYYY-MM-DD.")


print(get_days_from_today("2026-06-04"))

# Task 2: Generate a lottery-like ticket of unique random numbers
import random

# Function that generates a list of unique random numbers within a specified range
def get_numbers_ticket1(min, max, quantity):
    if (
            min < 1
            or max > 1000
            or min > max
            or quantity < 1
            or quantity > (max - min + 1)
    ):
        return []
    # random.sample selects unique values without replacement
    numbers = random.sample(range(min, max), quantity)
    return numbers

# Example usage: generate 6 unique numbers between 1 and 999 (1000 is exclusive)
print(get_numbers_ticket1(-10, 10, 5))

# Task 3: Normalize various raw phone number formats to a consistent international form
import re

# normalize_phone takes a phone number string in various formats and normalizes it to international format
def normalize_phone(phone_number: str) -> str:
    # Remove all characters except digits and plus sign
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    # If the cleaned number already starts with '+' keep it as international
    if cleaned_number.startswith("+"):
        return cleaned_number

    # If the cleaned number already starts with country code '380' add leading '+'
    if cleaned_number.startswith("380"):
        return "+" + cleaned_number

    # Otherwise assume missing country prefix and add '+38' for Ukraine
    return "+38" + cleaned_number

# Example list of raw phone strings in various formats
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Show normalized version of one example (index 5) and print it
print(normalize_phone(raw_numbers[5]))
