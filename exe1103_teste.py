import unittest
from exe1103_employee import Employee

class TestEmployee(unittest.TestCase):
    """[Testes para a classe Employee]
    """

    def setUp(self):
        """[Cria dois testes para Employee.]
        """
        self.junior = Employee('junior', 'pedroso', 10000)

    def test_give_default_raise(self):
        """[Testa se a função com aumento default]
        """
        self.junior.give_raise()
        self.assertEqual(self.junior.salario, 15000)

    def test_give_custom_raise(self):
        """[Testa a função com outro valor de aumento]
        """
        self.junior.give_raise(8000)
        self.assertEqual(self.junior.salario, 18000)


unittest.main()