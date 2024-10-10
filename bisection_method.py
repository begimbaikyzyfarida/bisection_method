import pandas as pd

def f(x):
    return x**3 + x - 1

def bisection_method(a, b, tol):

    table_data = []
    
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    iteration = 0
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        table_data.append([iteration, a, b, midpoint, f(midpoint)])
        
      
        if f(midpoint) == 0:
            break  
        elif f(a) * f(midpoint) < 0:
            b = midpoint  
        else:
            a = midpoint  
            
        iteration += 1

    table = pd.DataFrame(table_data, columns=["Iteration", "a", "b", "Midpoint", "f(Midpoint)"])
    
    return table, (a + b) / 2

a = 0  
b = 1  
tolerance = 0.01  

table, root = bisection_method(a, b, tolerance)

print(table)
print(f"\nApproximate root: {root}")
