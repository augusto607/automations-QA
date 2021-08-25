# Importamos UnitTest
import unittest

# Creamos la clase operations poniendo el objeto TestCase de unittest como parametro
class Operations(unittest.TestCase):

    # Definimos nuestros metodos
    def test_sum(self):
        sum = 1 + 1
        # Utilizamos los assertions
        self.assertEqual(sum, 2) # Con assertEqual validamos que estamos obteniendo el resultado esperado

    def test_sub(self):
        sub = 1 - 1
        self.assertNotEqual(sub, 2) # assertNotEqual evalua que el resultado no sea por eg 2

    def test_isupper(self):
        self.assertTrue('ALLAN'.isupper()) # Evaluamos booleanos tru or false
        self.assertFalse('augusto'.isupper())

# Colocamos esta validacion
if __name__ == '__main__':
    unittest.main()