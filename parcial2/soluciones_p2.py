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

#Ejercicio 2
def f2(func):
    errores   = [0]
    bloqueado = [False]

    def wrapper(*args):
        if bloqueado[0]:
            print('Leer la documentacion')
            return None

        try:
            return func(*args)         
        except Exception as e:
            errores[0] += 1
            print(f'Ha cometido {errores[0]} error(es): {type(e).__name__}')
            if errores[0] >= 3:         
                bloqueado[0] = True
            return None                 
    return wrapper

@f2
def division(a, b):
    return a / b

# --- RECURSIÓN ---
def f3i(n):
    """Versión iterativa para obtener el primer dígito."""
    while n >= 10:
        n = n // 10
    return n

def f3r(n):
    """Versión recursiva para obtener el primer dígito."""
    if n < 10:          
        return n
    return f3r(n // 10)