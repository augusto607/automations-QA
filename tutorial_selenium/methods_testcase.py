import unittest

class MethodsTestCase(unittest.TestCase):

    # El metodo setUpClass se ejecuta previamente que todo el conjunto de pruebas
    # y se le debe agregar siempre la funcion decoradora @classmethod
    @classmethod
    def setUpClass(cls):
        print("(setupclass->) Open Application")

    # Creamos el metodo setUp que ejecuta pre-condiciones antes de los casos de pruebas
    def setUp(self):
        print("(setup->) - Login on Application")

    # Creamos los casos de pruebas
    def test_create(self):
        print("Test create")

    def test_update(self):
        print("Test update")

    def test_search(self):
        print("Test search")

    def test_delete(self):
        print("Test delete")

    # Lo que se encuentra dentro del metodo tearDown se ejecuta despues que se ejecuta un caso de prueba
    # se ejecuta aun cuando las pruebas den error
    def tearDown(self):
        print("(teardown->) - Logout Application")

    # El metodo tearDownClass se ejecuta al final de todo el conjunto de pruebas
    # y se le debe agregar siempre la funcion decoradora @classmethod
    @classmethod
    def tearDownClass(cls):
        print("(teardownclass->) Close Application")

if __name__ == '__main__':
    unittest.main()