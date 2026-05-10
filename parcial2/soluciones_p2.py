#Ejercicio 1.1.
def G1():
    a, b, c = 1, 1, 1
    while True:
        yield a
        a, b, c = b, c, a + b + c

#Ejercicio 1.2.
def tresfibonacci(n):
    a, b, c = 1, 1, 1
    for _ in range(n):
        yield a
        a, b, c = b, c, a + b + c

# faltan ejercicio 2 y 3