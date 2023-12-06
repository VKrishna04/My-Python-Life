#
# * Bisection_Algorithm.py
#
# This script implements the Bisection Algorithm, a root-finding method that uses Bolzano's theorem and applies to any function that is continuous over the given interval for which one knows that there exists a zero.
#
# * Credits:
# - GitHub: @VKrishna04
#
# * Versions:
# - Python 3.12.0
#
# * Algorithm:
# 1. Find two points, a and b, such that a < b and f(a) * f(b) < 0.
# 2. Find the midpoint t of a and b.
# 3. If f(t) = 0, t is the root of the function. Otherwise, proceed to the next step.
# 4. Divide the interval [a, b]. If f(t)*f(a) < 0, a root exists between t and a. If f(t) *f (b) < 0, a root exists between t and b.
# 5. Repeat steps 2-4 until f(t) = 0.
# 6. Then announce that t is the root of the function.
#
# * Inputs:
# - A continuous function f(x)
# - Two points a and b such that a < b and f(a) * f(b) < 0
# - Precision of the root
# - Maximum number of iterations
# - An option to turn off Scientific notation if it appears in the resulting table.
#
# * Outputs:
# - The table of iterations, a, b, midpoint t, f(t)___0.
# - The rows where each row represents a single iteration.
# - If the max_Iteration is reached then terminate it directly otherwise continue.
# - For any unknown reason of error causing the program to end will display this. -> "Unexpected exit condition."
# - The root of the function within the interval [a, b].

from re import search


def numOfSpace(formatted_string):
    match = search(r"\t", formatted_string)  # search from re module.
    if match:
        return len(match.group())
    else:
        return 0


def swap(lower, upper):
    return upper, lower


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


def biSection_Method(user_function, a, b, precision, max_iterations, Rsci):
    iteration_width = max(len("S.No."), len(str(max_iterations)))

    char_count = numOfSpace(user_function)

    text = f"| {'S.No.':<{iteration_width}} || {'a[k-1]':<18} || {'b[k-1]':<18} || {'midpoint t':<25} || {'f(t)___0':<10} |"
    char_count = len(text)

    # Print table header
    print("=" * char_count)
    print(text)
    print("=" * char_count)

    # Declaring and Initializing variables
    iteration = 0
    t = 0
    T = 0  # Declare T outside the loop
    tolerance = 10 ** (-(precision + 2))

    # While loop for iterations and checking conditions to take another iteration.
    # If failed will proceed with termination of the program.
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
            A = int(format_number(A, precision))
            B = int(format_number(B, precision))
            T = int(format_number(T, precision))

        text = f"| {iteration:<{iteration_width}} || {A:<18} || {B:<18} || {T:<25} || {sign:<10} |"

        print(text)
        if abs(fm) < tolerance:
            char_count = len(text)
            print("=" * char_count)
            print(
                f"Root found at iteration {iteration}: {tolerance} with {T} digits after decimal."
            )
            break

        # Main Step for changing the interval [a, b] to [t, b] or [a, t] based on the sign of f(t) and f(a)
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
# Example Functions
# x^4 -14*x^3 +60*x^2 - 70*x
# x * sin(x) + cos(x)

# Set initial interval [a, b], reference, and maximum iterations
lower = float(input("Enter the lower bound of the interval [a]: "))
upper = float(input("Enter the upper bound of the interval [b]: "))

# Swap lower and upper if lower > upper
if lower > upper:
    lower, upper = swap(lower, upper)

# Get the desired number of decimal places for the root
precision = int(input("Enter the desired number of decimal places for the root: "))

# Get the max number of iterations to perform if the goal is not reached
max_iterations = int(input("Enter the maximum number of iterations: "))

# Get the user's choice for removing scientific notation
Rsci = input("Do you want to remove scientific notation? (y/n): ")
if Rsci == "y":
    Rsci = True
else:
    Rsci = False

# Call the function to apply the bisection method and create the table
biSection_Method(user_function, lower, upper, precision, max_iterations, Rsci)
