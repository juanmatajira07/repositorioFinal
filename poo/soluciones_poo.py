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
class Cajero:
    def __init__(self, billetes_100k, billetes_50k, billetes_20k, billetes_10k, billetes_5k, saldo_ahorros, saldo_corriente, saldo_cod):
        # 1. Inventario de billetes en el cajero
        self.billetes = {
            100000: billetes_100k,
            50000: billetes_50k,
            20000: billetes_20k,
            10000: billetes_10k,
            5000: billetes_5k
        }
        
        # 2. Cuentas y saldos del cliente
        self.cuentas = {
            "ahorros": saldo_ahorros,
            "corriente": saldo_corriente,
            "COD": saldo_cod
        }

    def retirar(self, tipo_cuenta, cantidad):
        # Validar que la cuenta exista
        if tipo_cuenta not in self.cuentas:
            return "Error: Tipo de cuenta no válido. Use 'ahorros', 'corriente' o 'COD'."

        # Validar el múltiplo mínimo (ahora el billete más pequeño es de 5000)
        if cantidad % 5000 != 0:
            return "Error: Solo se pueden retirar múltiplos de $5000."

        # Validar que la cuenta tenga saldo suficiente
        if cantidad > self.cuentas[tipo_cuenta]:
            return f"Error: Saldo insuficiente en su cuenta '{tipo_cuenta}'. Saldo actual: ${self.cuentas[tipo_cuenta]}"

        # Lógica para calcular billetes a entregar
        cantidad_restante = cantidad
        billetes_a_entregar = {}
        
        # Hacemos una copia temporal del inventario del cajero por si no logramos completar la suma
        inventario_temp = self.billetes.copy()

        # Recorremos las denominaciones de mayor a menor (100k -> 5k)
        for denominacion in sorted(self.billetes.keys(), reverse=True):
            if cantidad_restante == 0:
                break # Ya completamos el monto
            
            # Cuántos billetes de esta denominación idealmente necesitamos
            necesarios = cantidad_restante // denominacion
            
            # Cuántos podemos dar realmente (el mínimo entre lo que necesitamos y lo que hay en el cajero)
            a_dar = min(necesarios, inventario_temp[denominacion])

            if a_dar > 0:
                billetes_a_entregar[denominacion] = a_dar
                cantidad_restante -= (a_dar * denominacion)
                inventario_temp[denominacion] -= a_dar # Restamos del inventario temporal

        # Si después de revisar todos los billetes la cantidad restante no es 0, el cajero no tiene el cambio exacto
        if cantidad_restante > 0:
            return "Error: El cajero no dispone de la denominación de billetes necesaria para este retiro."

        # === TRANSACCIÓN EXITOSA ===
        # 1. Actualizamos el inventario real del cajero
        self.billetes = inventario_temp
        
        # 2. Descontamos el dinero del saldo de la cuenta
        self.cuentas[tipo_cuenta] -= cantidad

        # Imprimir el recibo
        print(f"\n--- RETIRO EXITOSO ---")
        print(f"Cuenta: {tipo_cuenta.capitalize()}")
        print(f"Monto retirado: ${cantidad}")
        print("Billetes entregados:")
        for denom, cant in billetes_a_entregar.items():
            print(f" - {cant} billete(s) de ${denom}")
        print(f"Nuevo saldo en cuenta: ${self.cuentas[tipo_cuenta]}")
        print("----------------------\n")
        
        return "Transacción completada."

    def mostrar_estado_cajero(self):
        print("\n--- INVENTARIO DEL CAJERO ---")
        for denom, cant in self.billetes.items():
            print(f"${denom}: {cant} billetes")
        print("-----------------------------\n")
