import unittest
from calculate import Calcular


class TestStringMethods(unittest.TestCase):

    def test_raiz_quadrada(self):
        calcular = Calcular()
        print("test_raiz_quadrada")
        self.assertEqual(calcular.raiz_quadrada(9), 3)
        self.assertEqual(calcular.raiz_quadrada(4), 2)

    def test_logaritmo(self):
        calcular = Calcular()
        print("test_logaritmo")
        self.assertEqual(calcular.logaritmo(100.12), 4.6063694665635735)
        self.assertEqual(calcular.logaritmo(100.72), 4.612344389736092)

    def test_split(self):
        calcular = Calcular()
        print("test_logaritmo")
        self.assertEqual(calcular.expoente(5, 3), 243)
        self.assertEqual(calcular.expoente(2, 3), 9)
        self.assertEqual(calcular.expoente(3, 5), 125)


if __name__ == '__main__':
    unittest.main()
