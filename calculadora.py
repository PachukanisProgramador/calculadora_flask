import math

class calculadora:
    def __init__(self):
        pass

    def somar(self, num1, num2):
        return num1 + num2

    def subt(self, num1, num2):
        return  num1 - num2

    def dividir(self, num1, num2):
        return num1 / num2

    def multiplicar(self, num1, num2):
        if num2 == 0:
            return "Impossível dividir por 0s"
        else:
            return num1 * num2

    def potencia(self, base, expoente):
        if expoente == 0:
            return 1
        elif expoente == 1:
            return base
        else:
            return math.pow(base, expoente)

    def raiz(self, num):
        if num < 0:
            return "Impossível calcular"
        else:
            return math.sqrt(num)

    def tabuada(self, num1):
        for i in range(11):
            resultado = resultado + f"\n{i} x {num1} = {num1 * i}"

        return resultado