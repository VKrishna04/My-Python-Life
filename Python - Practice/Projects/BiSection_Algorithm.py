# Bisection AAlgorithm in the form of a table has the following columns i.e. Iteration(k), a k-1, b k-1, midpoint mk,
# f(mk) is the function value at midpoint mk here f(mk) has three values (>, <, =) 0

from spacesByTabs import numOfSpace

def bisection_method(a, b, tol, max_iterations, user_function):
    
    iteration_width = max(len('S.No.'),len(str(max_iterations)))

    char_count = numOfSpace(user_function)

    text = f"| {'S.No.':<{iteration_width}} || {'a[k-1]':<18} || {'b[k-1]':<18} || {'midpoint mk':<25} || {'f(mk)_0':<1} |"
    char_count = len(text)
    print()
    
    # Print table header
    print("="*char_count)
    print(text)
    print("="*char_count)

    iteration = 1
    mk= 0
    
    # Dynamically create a function from the user input
    def f(x):
        return eval(user_function)

    while (b - a) >= tol and iteration <= max_iterations:
        mk = (a + b) / 2
        fm = f(mk)

        if fm > 0:
            sign = '>'
        elif fm < 0:
            sign = '<'
        else:
            sign = '='
        
        A = round(a,tol)
        B = round

        text = f"| {iteration:< {iteration_width}} || {a:<18} || {b:<18} || {mk:<25} || {sign:<1} |"
        print(text)
        char_count = len(text)
        if abs(fm) < tol:
            print("=" * char_count)
            print(f"Root found at iteration {iteration}: {mk}")
            break

        if f(a) * fm < 0:
            b = mk
        else:
            a = mk

        iteration += 1

    else:
        if iteration > max_iterations:
            text = "Bisection method stopped because maximum iterations reached."
        text = f"Bisection method stopped because (b[{iteration}] - a[{iteration}]) < {tol}.\nThe Final root found in the interval is = {mk}."
        char_count = len(text)
        print("="*char_count)
        print(text)
# Get the user-provided function
user_function = input("Enter the function f(x): ") # 'x ** 3 - 5 * x + 1'

# Set initial interval [a, b], tolerance, and maximum iterations
a = float(input("Enter the lower bound of the interval [a]: "))
b = float(input("Enter the upper bound of the interval [b]: "))

# Get the desired number of decimal places for the root
precision = int(input("Enter the desired number of decimal places for the root: "))
tolerance = 10**(-(precision + 2))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Call the function to apply the bisection method and create the table
bisection_method(a, b, tolerance, max_iterations, user_function)