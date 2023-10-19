from BiSection_Algorithm import bisection_method

def test_bisection_example():
  # Define test inputs
  a = 0
  b = 2
  tol = 6
  max_iterations = 15
  user_function = "x**3 - 5*x + 1"  # Adjust this function as needed

  # Run the bisection method
  captured_output = bisection_method(a, b, tol, max_iterations, user_function)

  # Assert that the printed output contains expected information
  # assert "Root found at iteration" in captured_output
  # assert "Bisection method stopped because" in captured_output