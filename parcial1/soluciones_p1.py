#Ejercicio_1

def f1(f, a, b):
    suma_total = 0
    for i in range(a, b + 1):
        suma_total += f(i) * i
    return suma_total

#Ejercicio_2

def f2(L):
    def polinomio(x):
        resultado = 0
        for i, coef in enumerate(L):
            resultado += coef * (x ** i)
        return resultado
    return polinomio

#Ejercicio_3
def f3(x0, y0):
    def recta(x):
        return 2 * (x - x0) + y0  
    def paralela(x):
        return 2 * (x - 1) + 1 
    return recta, paralela
#Ejercicio_4
def f4(L):
    L = [x for x in L if x > 10 and (int(str(x)[0]) + int(str(x)[-1])) % 2 == 0]
    return sum(L)
