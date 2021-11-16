import unittest
from exe1100_survey import AnonymousSurvey


class TestAnonnynousSurvey(unittest.TestCase):
    """[Testes para a classe AnonnymousSurvey]
    """

    def test_store_single_response(self):
        """[Testa se uma única resposta é armazenada de forma apropriada]
        """
        question = 'Qual idioma você aprendeu a falar primeiro? '
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('Português')

        self.assertIn('Português', my_survey.responses)

    def test_store_three_responses(self):
        """[Testa se três resposatas individuais são armazenadas de forma
        apropriada]
        """
        question = 'Qual idioma você aprendeu a falar primeiro? '
        my_survey = AnonymousSurvey(question)
        responses = ['Inglês', 'Espanhol', 'Português']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()
