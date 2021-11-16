import unittest
from exe1102_city_functions import nome_cidade_pais


class CitiesTestCase(unittest.TestCase):
    """[Testes para 'exe1101_city_functions']
    """

    def test_city_country(self):
        """[Cidades como 'Santiago, Chile' funcionam?]
        """
        cidade_pais = nome_cidade_pais('santiago', 'chile')
        self.assertEqual(cidade_pais, 'Santiago, Chile')

    def test_city_country_pop(self):
        """[Cidade como 'Santiago, Chile - população 5,614 mi funcionam?]
        """
        cidade_pais = nome_cidade_pais('santiago', 'chile', '5,614 mi')
        self.assertEqual(cidade_pais, 'Santiago, Chile - população 5,614 mi')


unittest.main()
