# Bisection AAlgorithm in the form of a table has the following columns i.e. Iteration(k), a k-1, b k-1, midpoint t,
# f(t) is the function value at midpoint t here f(t) has three values (>, <, =) 0

# For any continuous function f(x),

# Find two points, say a and b such that a < b and f(a) * f(b) < 0
# Find the midpoint of a and b, say “t”
# t is the root of the given function if f(t) = 0; else follow the next step
# Divide the interval [a, b] - If f(t)*f(a) <0, there exist a root between t and a
# - else if f(t) *f (b) < 0, there exist a root between t and b
# Repeat above three steps until f(t) = 0.

import re
import math


def numOfSpace(formatted_string):
    match = re.search(r"\t", formatted_string)
    if match:
        return len(match.group())
    else:
        return 0


def format_number(num, precision):
    if "e" in f"{num}":
        return "{:.{}f}".format(num, precision)
    else:
        return str(num)


def insert_multiplication_operator(expression):
    expression = list(expression)
    for i in range(1, len(expression)):
        if expression[i] == "x" and expression[i - 1].isdigit():
            expression[i] = "*x"
    return "".join(expression)


def prepare_expression(expression):
    operators = {
        "^": "**",
        "sin": "math.sin",
        "cos": "math.cos",
        "tan": "math.tan",
        "pi": "math.pi",
        "sqrt": "math.sqrt",
        "log": "math.log",
        "e": "math.e",
    }

    expression = insert_multiplication_operator(expression)

    for operator, function in operators.items():
        expression = expression.replace(operator, function)

    return expression


# Dynamically create a function from the user input
def f(x):
    return eval(user_function)


def bisection_method(a, b, precision, max_iterations, user_function, Rsci):
    iteration_width = max(len("S.No."), len(str(max_iterations)))

    char_count = numOfSpace(user_function)

    text = f"| {'S.No.':<{iteration_width}} || {'a[k-1]':<18} || {'b[k-1]':<18} || {'midpoint t':<25} || {'f(t)___0':<10} |"
    char_count = len(text)

    # Print table header
    print("=" * char_count)
    print(text)
    print("=" * char_count)

    iteration = 0
    t = 0
    T = 0  # Declare T outside the loop
    tolerance = 10 ** (-(precision + 2))

    while (b - a) >= tolerance and iteration <= max_iterations:
        t = (a + b) / 2
        fm = f(t)

        if fm > 0:
            sign = ">"
        elif fm < 0:
            sign = "<"
        else:
            sign = "="

        # Use precision to round a, b, and t
        A = round(a, precision)
        B = round(b, precision)
        T = round(t, precision)

        # Removing Scientific Notation
        if Rsci == True:
            text = f"| {iteration:<{iteration_width}} || {format_number(A, precision):<18} || {format_number(B, precision):<18} || {format_number(T, precision):<25} || {sign:<10} |"
        else:
            text = f"| {iteration:<{iteration_width}} || {A:<18} || {B:<18} || {T:<25} || {sign:<10} |"

        print(text)
        char_count = len(text)
        if abs(fm) < tolerance:
            print("=" * char_count)
            print(f"Root found at iteration {iteration}: {T}")
            break

        if f(a) * fm < 0:
            b = t
        else:
            a = t

        iteration += 1

    if iteration > max_iterations:
        text = "Bisection method stopped because maximum iterations reached."
    elif (b - a) < precision:
        text = f"Bisection method stopped because (b[{iteration}] - a[{iteration}]) < {precision}.\nThe Final root found in the interval is = {T}."
    else:
        text = "Unexpected exit condition."

    char_count = len(text)
    print("=" * char_count)
    print(text)


# Get the user-provided function
user_function = input("Enter the function f(x): ")
user_function = prepare_expression(user_function)

# Set initial interval [a, b], reference, and maximum iterations
a = float(input("Enter the lower bound of the interval [a]: "))
b = float(input("Enter the upper bound of the interval [b]: "))

# Get the desired number of decimal places for the root
precision = int(input("Enter the desired number of decimal places for the root: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Get the user's choice for removing scientific notation
Rsci = input("Do you want to remove scientific notation? (y/n): ")
if Rsci == "y":
    Rsci = True
else:
    Rsci = False

# Call the function to apply the bisection method and create the table
bisection_method(a, b, precision, max_iterations, user_function, Rsci)
# x^4 -14*x^3 +60*x^2 - 70*x
