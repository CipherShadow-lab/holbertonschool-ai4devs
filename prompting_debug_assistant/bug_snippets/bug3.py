# This code snippet causes an error while running the program (runtime exception).

def get_user_age():
    """Function retrieves user's age."""
    user_age = input("Enter your age: ")
    return user_age


def calculate_birth_year(user_age):
    """Function calculates the user's birth year based on their age."""
    current_year = 2026
    return current_year - user_age


entered_age = get_user_age()

if entered_age >= 18:
    print("You are an adult.")

birth_year = calculate_birth_year(entered_age)

print("You were born around:", birth_year)
