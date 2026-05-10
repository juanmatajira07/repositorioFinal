# Ejercicio 1
class Polinomio:
    def __init__(self, L):
        self.L = L 
            
    def __str__(self):
        terminos = []
        for i, coef in enumerate(self.L):
            if i == 0: terminos.append(str(coef))
            elif i == 1: terminos.append(f"{coef}x")
            else: terminos.append(f"{coef}x^{i}")
        return " + ".join(terminos).replace("+ -", "- ")

    def __add__(self, other):
        maxi = max(len(self.L), len(other.L))
        l1 = self.L + [0] * (maxi - len(self.L))
        l2 = other.L + [0] * (maxi - len(other.L))
        return Polinomio([l1[i] + l2[i] for i in range(maxi)])

    def __sub__(self, other):
        maxi = max(len(self.L), len(other.L))
        l1 = self.L + [0] * (maxi - len(self.L))
        l2 = other.L + [0] * (maxi - len(other.L))
        return Polinomio([l1[i] - l2[i] for i in range(maxi)])

    def __mul__(self, other):
        res = [0] * (len(self.L) + len(other.L) - 1)
        for i in range(len(self.L)):
            for j in range(len(other.L)):
                res[i+j] += self.L[i] * other.L[j]
        return Polinomio(res)

    def evaluar(self, x):
        total = 0
        for i in range(len(self.L)):
            total += self.L[i] * (x**i)
        return total

# Ejercicio 2
class PolinomiosDerivables(Polinomio):
    def grado(self):
        return len(self.L) - 1

    def derivada(self):
        nueva_L = [self.L[i] * i for i in range(1, len(self.L))]
        return PolinomiosDerivables(nueva_L)
    
    def recta_tangente(self, x0):
        m = self.derivada().evaluar(x0)
        y0 = self.evaluar(x0)
        b = y0 - (m * x0)
        return PolinomiosDerivables([b, m])
# falta ejercicio del cajero