"""Este script en python resuelve ecuaciones cuadráticas de la forma ax^2 + bx + c = 0.
by: Alvaro Manzo"""

import cmath

def resolver_ecuacion_cuadratica(a, b, c):
    # Calculamos el discriminante
    d = (b**2) - (4*a*c)
    # Encontramos las dos soluciones
    sol1 = (-b + cmath.sqrt(d)) / (2*a)
    sol2 = (-b - cmath.sqrt(d)) / (2*a)
    return sol1, sol2

if __name__ == "__main__":
    print("Resuelve la ecuación cuadrática de la forma ax^2 + bx + c = 0")
    a = float(input("Ingresa el valor de a (no puede ser 0): "))
    b = float(input("Ingresa el valor de b: "))
    c = float(input("Ingresa el valor de c: "))

    if a == 0:
        print("El valor de 'a' no puede ser 0 en una ecuación cuadrática.")
    else:
        soluciones = resolver_ecuacion_cuadratica(a, b, c)
        print(f"""Las soluciones son: {soluciones[0]} y {soluciones[1]}
               by: Alvaro Manzo""")

