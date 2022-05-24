import math


class Calcular:

    def expoente(self,expoente, value):
        potencia = 1
        for _ in range(expoente):
            potencia *= value
        return potencia

    def logaritmo(self, value):
       return math.log(value)

    def raiz_quadrada(self, value):
        return math.pow(value, 1 / 2)

