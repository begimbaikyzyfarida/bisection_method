import pandas as pd

# Define the function f(x) = x^3 + x - 1
def f(x):
    return x**3 + x - 1

# Define the bisection method with table data generation
def bisection_method(a, b, tol):
    # Create a list to store the table data
    table_data = []
    
    # Check if the initial interval is valid
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    iteration = 0
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        table_data.append([iteration, a, b, midpoint, f(midpoint)])
        
        # Update the interval based on the sign of f(midpoint)
        if f(midpoint) == 0:
            break  # Exact root found
        elif f(a) * f(midpoint) < 0:
            b = midpoint  # Root lies between a and midpoint
        else:
            a = midpoint  # Root lies between midpoint and b
            
        iteration += 1

    # Create a Pandas DataFrame to format the table
    table = pd.DataFrame(table_data, columns=["Iteration", "a", "b", "Midpoint", "f(Midpoint)"])
    
    # Return the table for display
    return table, (a + b) / 2

# Example usage:
a = 0  # lower bound of the interval
b = 1  # upper bound of the interval
tolerance = 0.01  # desired precision

# Run the bisection method and capture the table and root
table, root = bisection_method(a, b, tolerance)

# Display the table and the approximate root
print(table)
print(f"\nApproximate root: {root}")
