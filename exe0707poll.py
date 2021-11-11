responses = {}
# Define uma flag para indicar que a enquete está ativa
polling_active = True

while polling_active:
    # Pede o nome da pessoa e a resposta
    name = input('\nQual seu nome? ')
    response = input('Qual montanha você gostaria de escalar algun dia? ')
    # Armazena a reposta no dicionário
    responses[name] = response
    # Descobre se outra pessoa vai responder a enquete
    repeat = input('Você gostaria de deixar outra pessoa responder?' +
                   '(s/n)')
    if repeat == 'n':
        polling_active = False

# A enquete foi concluída. Mostra os resultados
print('\n--- Resultado da enquete ---')
for name, response in responses.items():
    print(name + ' gostaria de escalar ' + response + '.')
    
print(responses)
