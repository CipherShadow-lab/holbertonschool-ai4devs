"""Code has been fixed by adding an 'empty list' check
and adding the missing parenthesis for the calculate_average call
"""

def calculate_average(numbers):
    """Function calculates average from an array of numbers"""
    if not numbers:
        return None

    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)

scores = [25, 50, 37, 44, 60]
print(calculate_average(scores)) # Output: 43.2
