import sympy as sympy
 
#Define Symbol of the variable
X = sympy.Symbol('x')

def f(x):
    # simplifies the equation
    equation = sympy.simplify('x^3 + x^2 - 1')
    return float(equation.subs(X, x))

def g(x):
    # simplifies the equation
    equation = sympy.simplify('1/((x+1)^(1/2))')
    return float(equation.subs(X, x))


# Define Initial value of X in given range [a , b]
X0 = float(0.75)

#Define Tolerance for the value of x
t = int(input("Enter The Tolerance for Error:"))
tolerance = 1e-1 * 10**(-t)

iteration = 0
# Table Header
print(f"{'Iteration':<20}{'Value of X':<20}{'Value of G(x)':<20}{'Value of F(x)':<20}")

#looping for each table and their respective values
while iteration < 10000000:
    print(f"{iteration:<20}{X0:<20.6f}{g(X0):<20.6f}{f(X0):<20.6f}")
    X0 = g(X0)
    iteration += 1
    
    if abs(f(X0)) < tolerance:
        print(f"The Value of X is: {round(X0, t)}")
        break
else:
    print(f"The Method Did Not Converge......")