# GoldenSection_Algorithm.py
#
# * Credits:
# - GitHub: @VKrishna04
#
# * Versions:
# - Python 3.12.0
# - sympy-1.12 install with {pip install sympy}
# - Code Runner by VS Code extension {code runner} install with {ext install ms-vscode.cpptools} in command palette with ctrl+p.
# - VS Code extension {better comments} install with {ext install aaron-bond.better-comments} in command palette with ctrl+p.
# Common functions
from re import search
import math
from sympy import symbols, sympify

try:

    def numOfSpace(formatted_string):
        match = search(r"\t", formatted_string)
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

    x = symbols("x")
    user_function = input("Enter the function f(x): ")
    user_function = sympify(user_function)
    # x^4 -14*x^3 +60*x^2 - 70*x
    # x * sin(x) + cos(x)

    def f(y):
        return user_function.subs(x, y)

    a = float(input("Enter the lower bound of the interval [a]: "))
    b = float(input("Enter the upper bound of the interval [b]: "))

    if a > b:
        a, b = swap(a, b)

    epsilon = float(input("Enter the epsilon / uncertainty value (eg. 0.005 ) : "))
    noOfDigits = int(input("Please enter the max number of digits : "))
    phi = float(1 - ((3 - math.sqrt(5)) / 2))

    A, B, X1, X2, F1, F2 = "0" * 6
    sign = ""
    length = abs(b - a)

    requiredIterations = math.ceil(math.log(epsilon / length) / math.log(phi))
    print(f"\nRequired Iterations: {requiredIterations}")
    print(f"Length of the given interval : {length}")
    precision = max(len(f"{epsilon - math.floor(epsilon)}") - 2, noOfDigits)
    text = f"| {'S.No.':<5} || {'a[k-1]':<18} || {'b[k-1]':<18} || {'x1':<18} || {'x2':<18} || {'f(x1)':<18} || {'f(x2)':<18} || {'f(t)___0':<8} |"
    char_count = numOfSpace(text)
    char_count = len(text)

    print("=" * char_count)
    print(text)
    print("=" * char_count)

    x1 = a + phi * (b - a)
    x2 = b - phi * (b - a)
    iteration = 0
    for iteration in range(requiredIterations):
        if f(x1) < f(x2):
            sign = "<"
        elif f(x1) > f(x2):
            sign = ">"
        else:
            sign = "="
        if x1 > x2:
            x1, x2 = swap(x1, x2)
        A = round(a, precision)
        B = round(b, precision)
        X1 = round(x1, precision)
        X2 = round(x2, precision)
        F1 = round(f(x1), precision)
        F2 = round(f(x2), precision)
        # Removing Scientific Notation
        A = float(format_number(A, precision))
        B = float(format_number(B, precision))
        X1 = float(format_number(X1, precision))
        X2 = float(format_number(X2, precision))
        F1 = float(format_number(F1, precision))
        F2 = float(format_number(F2, precision))
        print(
            f"| {iteration+1:<5} || {A:<18} || {B:<18} || {X1:<18} || {X2:<18} || {F1:<18} || {F2:<18} ||     {sign:<4} |"
        )
        if f(x1) > f(x2):
            a = x1
            b = b
            new = x2
        else:
            a = a
            b = x2
            new = x1
        if (new - a) < (b - new):
            x1 = new
            x2 = b - (new - a)
        else:
            x1 = b - (new - a)
            x2 = new

    if x1 > x2:
        x1, x2 = swap(x2, x1)

    char_count = len(text)
    print("=" * char_count)

    print(
        f"The extremum is found in the interval {X1} to {X2}. With exit condition as '(b[{iteration+1}] - a[{iteration+1}]) < {epsilon}'\nThe extremum found in the interval {iteration+1}."
    )
except KeyboardInterrupt:
    print("\n\nExiting the Method Calculation...")
except ValueError:
    print("\n\nInvalid Input Please Exit and Try Again.")
