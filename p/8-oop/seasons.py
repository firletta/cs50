from datetime import datetime
from num2words import num2words
import sys

def get_birthdate():
    birthdate_str = input("Date of birth (YYYY-MM-DD): ")
    try:
        return datetime.strptime(birthdate_str, "%Y-%m-%d")
    except ValueError:
        sys.exit("Invalid date format. Please enter a date in the format YYYY-MM-DD.")

def calculate_age_in_minutes(birthdate):
    now = datetime.now()
    age_in_seconds = (now - birthdate).total_seconds()
    age_in_minutes = round(age_in_seconds / 60)
    return age_in_minutes

def main():
    birthdate = get_birthdate()
    age_in_minutes = calculate_age_in_minutes(birthdate)
    age_in_words = num2words(age_in_minutes)
    print(age_in_words)

if __name__ == "__main__":
    main()
