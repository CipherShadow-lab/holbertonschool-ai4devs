"""Code is fixed by converting the input to an integer"""

from datetime import datetime

def get_user_age():
    """Function retrieves user's age."""
    user_age = int(input("Enter your age: "))
    return user_age

def calculate_birth_year(user_age):
    """Function calculates the user's birth year based on their age."""
    current_year = datetime.now().year
    return current_year - user_age

entered_age = get_user_age()

if entered_age >= 18:
    print("You are an adult.")
else:
    print("You're a spring chicken!!!")

birth_year = calculate_birth_year(entered_age)

print("You were born in:", birth_year)
