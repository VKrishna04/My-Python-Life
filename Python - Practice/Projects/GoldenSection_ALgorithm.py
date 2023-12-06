# GoldenSection_Algorithm.py
#
# * Credits:
# - GitHub: @VKrishna04
#
# * Versions:
# - Python 3.12.0
# - sympy-1.12 install with {pip install sympy}
#
# The Golden Section Search is a method for finding the maximum or minimum of a unimodal function. The method operates by successively narrowing the range of values on the function to find the extremum. It's based on the mathematical concept of golden ratio.
#
# Here's a simple pseudocode for the Golden Section Search:
#
# 1. Define the function to be optimized.
# 2. Define the initial interval of uncertainty (lower and upper bounds).
# 3. Calculate the number of iterations required.
# 4. Define the new points within the interval using the golden ratio.
# 5. Evaluate the function at these new points.
# 6. Update the interval of uncertainty based on the function evaluations.
# 7. Repeat steps 4-6 until the interval of uncertainty is smaller than a predefined threshold.

# Common functions
from re import search
import math
from typing import Required

# from sympy import symbols, lambdify
import sympy


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


# Dynamically create a function from the user input
x = sympy.symbols("x")


def f(val):
    operators = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "pi": math.pi,
        "sqrt": math.sqrt,
        "log": math.log,
        "e": math.e,
    }
    func = sympy.lambdify(
        x,
        user_function,
        [operators, "math"],
    )
    return float(func(val))


# Calculate the number of Iterations Required
def calculate_iterations(lower, upper, precision):
    return math.ceil(
        math.log((upper - lower) / precision) / math.log((3 - 5**0.5) / 2)
    )


# Calculate the intervals for the next iteration
def goldenSectionIntRecalculate(func, lower, upper, x1, x2):
    if func(x1) < func(x2):
        lower = x1
    else:
        upper = x2
    return lower, upper


# Golden Section Algorithm
def goldenSection_Method(user_function, lower, upper, precision, max_iterations, Rsci):
    iteration_width = max(len("S.No."), len(str(max_iterations)))

    # Use arrays to store the values of the variables we are not giving the list fixed length since there might be issues where the number of iterations is less than the max iterations and the that will lead to wastage of allocated memory
    a = [float(lower)]
    b = [float(upper)]
    x1 = [float(0)]
    x2 = [float(0)]

    # Declaring and Initializing variables and necessary constants / parameters
    iteration = 0  # iteration counter always add 1 to get the current iteration
    A = 0
    B = 0
    X1 = 0
    X2 = 0
    F1 = 0
    F2 = 0
    Mid = 0
    length = upper - lower
    tolerance = 10 ** (-(precision + 2))
    sign = ""

    # Golden Ratio for calculations
    phi = (3 - math.sqrt(5)) / 2

    # Calculate the number of Iterations Required
    requiredIterations = math.ceil(
        math.log(length / precision) / math.log((3 - math.sqrt(5)) / 2)
    )
    print("Required Iterations: ", requiredIterations)

    # Print table header
    char_count = numOfSpace(user_function)

    text = f"| {'S.No.':<{iteration_width}} || {'a[k-1]':<18} || {'b[k-1]':<18} || {'x1':<18} || {'x2':<18} || {'f(x1)':<18} || {'f(x2)':<18} || {'f(t)___0':<8} |"
    char_count = len(text)

    # Print table header
    print("=" * char_count)
    print(text)
    print("=" * char_count)

    # x1 and x2 using the formula where x1 is the and x2 are the new intervals
    # x1 = a + (b - a) * phi
    # x2 = b - (b - a) * phi
    x1[0] = lower + (length * phi)
    x2[0] = upper - (length * phi)

    # Main Iterative loop
    while (
        iteration < max_iterations
        and (b[iteration] - a[iteration]) > tolerance
        and iteration < requiredIterations
    ):
        # Setting all the variables from previous iteration
        Mid = (b[iteration] - a[iteration]) / 2
        print(
            "ite ",
            iteration,
            "a",
            a.__len__(),
            "b",
            b.__len__(),
            "x1 = ",
            x1.__len__(),
            "x2 = ",
            x2.__len__(),
        )
        # Calculate the intervals for the next iteration
        if f(x1[iteration]) < f(x2[iteration]):
            sign = "<"
            # Calculating the x1 and x2 for next interval
            a.append(a[iteration])  # a does not change
            b.append(
                x2[iteration]
            )  # x2 for this iteration becomes b for next iteration
            if x1[iteration] < Mid:
                x1.append(
                    x1[iteration]
                )  # x1 for next iteration and is constant if x1 < Mid
                x2.append(
                    b[iteration] - (b[iteration] - a[iteration]) * phi
                )  # x2 is being calculated for next iteration
            if x1[iteration] > Mid:
                x2.append(
                    x1[iteration]
                )  # x1 for this iteration becomes x2 for next iteration
                x1.append(
                    a[iteration] + (b[iteration] - x1[iteration])
                )  # x1 for next iteration

        elif f(x1[iteration]) > f(x2[iteration]):
            sign = ">"
            # Calculating the x1 and x2 for next interval
            b.append(b[iteration])  # b does not change
            a.append(
                x2[iteration]
            )  # x2 for this iteration becomes b for next iteration
            if x2[iteration] > Mid:
                x1.append(
                    a[iteration] + (b[iteration] - a[iteration]) * phi
                )  # x1 is being calculated for the next iteration
                x2.append(
                    x2[iteration]
                )  # x2 for next iteration and is constant if x2 > Mid
            if x2[iteration] < Mid:
                x1.append(
                    x2[iteration]
                )  # x1 for this iteration becomes x2 for next iteration
                x2.append(
                    b[iteration] - (x2[iteration] - a[iteration])
                )  # x2 for next iteration
        else:
            sign = "="
            break

        # Use precision to round a, b, and t
        A = round(a[iteration], precision)
        B = round(b[iteration], precision)
        X1 = round(x1[iteration], precision)
        X2 = round(x2[iteration], precision)
        F1 = round(f(x1[iteration]), precision)
        F2 = round(f(x2[iteration]), precision)

        # Removing Scientific Notation
        if Rsci == True:
            A = float(format_number(A, precision))
            B = float(format_number(B, precision))
            X1 = float(format_number(X1, precision))
            X2 = float(format_number(X2, precision))
            F1 = float(format_number(F1, precision))
            F2 = float(format_number(F2, precision))

        text = f"| {iteration+1:<{iteration_width}} || {A:<18} || {B:<18} || {X1:<18} || {X2:<18} || {F1:<18} || {F2:<18} ||     {sign:<4} |"

        print(text)

        iteration += 1  # increment the iteration counter at the end of each iteration
        print("iteration", iteration)

    # print(f"a = {a[iteration-1]} b = {b[iteration-1]} x1 = {x1[iteration-1]} x2 = {x2[iteration-1]} f(x1) = {f(x1[iteration-1])} f(x2) = {f(x2[iteration-1])}")
    # print(f"a = {a[iteration]} b = {b[iteration]} x1 = {x1[iteration]} x2 = {x2[iteration]} f(x1) = {f(x1[iteration])} f(x2) = {f(x2[iteration])}")

    # Exit Conditions
    if iteration > max_iterations:
        text = "Golden Section method stopped because maximum iterations reached."
    elif iteration == requiredIterations:
        text = f"Golden Section method stopped because the extremum is found in the interval {X1} to {X2} (b[{iteration}] - a[{iteration}]) < {tolerance}.\nThe extremum found in the interval {iteration}."
    else:
        text = "Unexpected exit condition."

    char_count = len(text)
    print("=" * char_count)
    print(text)


# User Inputs
# Get the user-provided function
user_function = input("Enter the function f(x): ")
user_function = user_function.replace(" ", "")
user_function = user_function.replace("^", "**")
user_function = insert_multiplication_operator(user_function)
# Example Functions
# x^4 -14*x^3 +60*x^2 - 70*x
# x * sin(x) + cos(x)

# Set initial interval [a, b], reference, and maximum iterations
# ! Make Sure not to give a and b such that abs(a) = abs(b)
lower = float(input("Enter the lower bound of the interval [a]: "))
upper = float(input("Enter the upper bound of the interval [b]: "))

# Swap lower and upper if lower > upper
if lower > upper:
    lower, upper = swap(lower, upper)

# Precision or the uncertainty of the extremum
precision = int(
    input(
        "Enter the desired number of decimal places for the Precision or the uncertainty of the extremum : "
    )
)

# Get the max number of iterations to perform if the goal is not reached
max_iterations = int(input("Enter the maximum number of iterations: "))

# Get the user's choice for removing scientific notation
Rsci = input("Do you want to remove scientific notation? (y/n): ")
if Rsci == "y":
    Rsci = True
else:
    Rsci = False

# Call the function to apply the bisection method and create the table
goldenSection_Method(user_function, lower, upper, precision, max_iterations, Rsci)
