# Exercício do capítulo 03 - Alterando, acrescentando e removendo elementos 
# da lista de convidados - Funções para cada coisa 


def linha():
    print('-' * 30) # Esta função cria uma linha


def mensagem(msg): # Esta função cria uma mensagem personalizada com linhas antes e depois
    linha()
    print(msg.center(30))
    linha()


def menu(lista):
    mensagem('MENU PRINCIPAL') # Esta função cria um menu e espera uma opção
    for i in range(len(lista)):
        print(f'{i + 1} - {lista[i]}')
    linha()
    opc = int(input('Digite sua opção: '))
    return opc 

def incConvidado():
    conv = input('Nome do convidado: ')
    convidados.append(conv)


def excConvidado():
    consConvidado('orig')
    mensagem('EXCLUSÃO DE CONVIDADO')
    convExc = (int(input('Digite o número para excluir: ')) - 1)
    print(f'O convidado {convidados.pop(convExc)} foi excluído!')


def consConvidado(modo):
    listaTemp = []
    if modo == 'orig':
        mensagem('LISTA EM ORDEM ORIGINAL')
        listaTemp = convidados
    elif modo == 'ordem':
        mensagem('LISTA EM ORDEM ALFABÉTICA')
        listaTemp = sorted(convidados)
    elif modo == 'reverso':
        mensagem('LISTA EM ORDEM INVERSA')
        listaTemp = sorted(convidados, reverse=True)

    for i in range(len(listaTemp)):
        print(f'{i + 1} - {listaTemp[i]}')


# Programa Principal
convidados=[]
itensMenu = ['Incluir Convidado', 'Excluir Convidado', 'Consulta Convidado', 
             'Consulta em ordem', 'Consulta em ordem inversa', 'Sair']

while True:
    opc = menu(itensMenu)
    if opc == 1:
        incConvidado()
    elif opc == 2:
        excConvidado()
    elif opc == 3:
        consConvidado('orig')
    elif opc == 4:
        consConvidado('ordem')
    elif opc == 5:
        consConvidado('reverso')
    elif opc == 6:
        break

print('Saindo do sistema... Até logo!')
