#Ejercicio_1

def f1_intermedia(f, a, b):
    suma_total = 0
    for i in range(a, b + 1):
        suma_total += f(i) * i
    return suma_total

#Ejercicio_2

def f2_intermedia(L):
    def polinomio(x):
        resultado = 0
        for i, coef in enumerate(L):
            resultado += coef * (x ** i)
        return resultado
    return polinomio

#faltan ejercicio 3 y 4