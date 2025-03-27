from math import pi

# Q1: Recursive factorial function
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

# Q2: sin(x) approximation using Taylor series
def sine_x(x_deg, n):
    x = x_deg * (pi / 180)  # Convert degrees to radians manually
    result = 0
    for i in range(n):
        term = (lambda n: ((-1) * n) * (x * (2 * n + 1)) / factorial(2 * n + 1))(i)
        result += term
    return result

# Q3: Harmonic number
harmonic_sum = 0

def harmonic(n):
    """
    Recursive function to calculate the harmonic number Hn.
    Updates the global variable harmonic_sum instead of returning the result.
    """
    global harmonic_sum
    if n == 0:
        return
    harmonic(n - 1)
    harmonic_sum += 1 / n



# Q1: Factorial
x_input = int(input("Q1 - Faktoriyel için bir sayı girin: "))
print("Faktoriyel:", factorial(x_input))

# Q2: sin(x)
x_deg_input = float(input("Q2 - sin(x) için x (derece cinsinden) girin: "))
n_terms = int(input("Q2 - sin(x) için terim sayısı (n) girin: "))
print("sin({}°) yaklaşık değeri ({} terim):".format(x_deg_input, n_terms), sine_x(x_deg_input, n_terms))

# Q3: Harmonik
harmonic_sum = 0
n_harmonic = int(input("Q3 - Harmonik sayı için n girin: "))
harmonic(n_harmonic)
print("H_{} harmonik değeri:".format(n_harmonic), harmonic_sum)
