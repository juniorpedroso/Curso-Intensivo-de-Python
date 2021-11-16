from exe1100_survey import AnonymousSurvey

# Define uma pergunta e cria uma pesquisa
question = 'Qual idioma você aprendeu a falar primeiro?'
my_survey = AnonymousSurvey(question)

#Mostra a pergunta e armazena as resposatas à pergunta
my_survey.show_question()
print("Tecle 's' para sair.\n")
while True:
    response = input('Idioma: ')
    if response == 's':
        break
    my_survey.store_response(response)

# Exibe os resultados da pesquisa
print("\nObrigado a todos que participaram da pesquisa!")
my_survey.show_results()
