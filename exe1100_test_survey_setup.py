import unittest
from exe1100_survey import AnonymousSurvey


class TestAnonnynousSurvey(unittest.TestCase):
    """[Testes para a classe AnonnymousSurvey]
    """

    def setUp(self):
        """[Cria uma pesquisa e um conjunto de respostas que poderão ser
        usados em todos os métodos de teste.]
        """
        question = 'Qual idioma você aprendeu a falar primeiro? '
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Inglês', 'Espanhol', 'Português']

    def test_store_single_response(self):
        """[Testa se uma única resposta é armazenada de forma apropriada]
        """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """[Testa se três resposatas individuais são armazenadas de forma
        apropriada]
        """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()