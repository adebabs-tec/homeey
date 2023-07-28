import math

def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant (D)
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return root, None
    else:
        # No real roots
        return None, None

# Input coefficients a, b, and c
a = float(input("Enter the coefficient 'a': "))
b = float(input("Enter the coefficient 'b': "))
c = float(input("Enter the coefficient 'c': "))

# Calculate and display the solutions
root1, root2 = solve_quadratic_equation(a, b, c)

if root1 is not None and root2 is not None:
    print(f"The solutions are: {root1} and {root2}")
elif root1 is not None:
    print(f"There is one solution: {root1}")
else:
    print("No real solutions exist.")
