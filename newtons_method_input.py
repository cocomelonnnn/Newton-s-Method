def newton_method(f, df, x0, tol, max_iter=10):
    x = x0
    print("Starting Newton's Method:")
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        print(f"Iteration {i+1}: x = {x_new:.6f}")
        if abs(x_new - x) < tol:
            break
        x = x_new
    print(f"\nApproximate root: {x:.6f}")

# Predefined initial guess and tolerance
x0 = 1
tol = 0.000001

# Get user input for function and derivative
import math

expr = input("Enter the function f(x) (e.g., x**2 - 2): ")
d_expr = input("Enter the derivative f'(x) (e.g., 2*x): ")

# Define the function and derivative using eval safely
def f(x): return eval(expr, {'x': x, 'math': math})
def df(x): return eval(d_expr, {'x': x, 'math': math})

# Run the method
newton_method(f, df, x0, tol)