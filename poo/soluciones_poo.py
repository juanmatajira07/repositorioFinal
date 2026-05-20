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
#Ejercicio del cajero
class Cajero():
    def __init__(self, n1, n2, n5):
        # n1: billetes de 10000, n2: billetes de 20000, n5: billetes de 50000
        self.billetes_10k = n1
        self.billetes_20k = n2
        self.billetes_50k = n5

    def retiro(self, x):
        # 1. Validar que sea múltiplo de 10000
        if x % 10000 != 0:
            return "Error: La cantidad solicitada debe ser múltiplo de 10000."

        # Variables temporales para hacer el cálculo sin afectar el inventario real aún
        cantidad_restante = x
        entregar_50k = 0
        entregar_20k = 0
        entregar_10k = 0

        # 2. Lógica para calcular billetes (de mayor a menor denominación)
        # Billetes de 50,000
        necesarios_50k = cantidad_restante // 50000
        entregar_50k = min(necesarios_50k, self.billetes_50k)
        cantidad_restante -= entregar_50k * 50000

        # Billetes de 20,000
        necesarios_20k = cantidad_restante // 20000
        entregar_20k = min(necesarios_20k, self.billetes_20k)
        cantidad_restante -= entregar_20k * 20000

        # Billetes de 10,000
        necesarios_10k = cantidad_restante // 10000
        entregar_10k = min(necesarios_10k, self.billetes_10k)
        cantidad_restante -= entregar_10k * 10000

        # 3. Verificación final y actualización
        if cantidad_restante == 0:
            # Si logramos cubrir el monto exacto, actualizamos los atributos reales
            self.billetes_50k -= entregar_50k
            self.billetes_20k -= entregar_20k
            self.billetes_10k -= entregar_10k
            return f"Retiro exitoso. Entregando: {entregar_50k}x50k, {entregar_20k}x20k, {entregar_10k}x10k."
        else:
            # Si sobra cantidad, el cajero no tiene cómo dar el cambio exacto
            return "Error: El cajero no dispone de la cantidad o denominación de billetes necesaria."

    def consignacion(self, n1, n2, n5):
        # Se suman los billetes ingresados al inventario actual
        self.billetes_10k += n1
        self.billetes_20k += n2
        self.billetes_50k += n5
        return "Consignación exitosa. Inventario actualizado."

    def verificar_estado(self):
        # Retorna el mensaje con el conteo actual de cada denominación
        return f"Billetes en cajero -> 10000: {self.billetes_10k} | 20000: {self.billetes_20k} | 50000: {self.billetes_50k}"