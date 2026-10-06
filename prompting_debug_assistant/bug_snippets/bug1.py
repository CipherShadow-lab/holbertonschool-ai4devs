# Code snippet contains syntax problems that produces a Syntax Error.


def calculate_average(numbers):
    """Function calculates average from an array of numbers"""
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)
    return average


scores = [75, 82, 91, 68, 88]
print(calculate_average(scores)
