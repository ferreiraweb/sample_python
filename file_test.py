
def show_linha(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        print('Total de linha no arquivo')
        contador = 0
        for linha in arquivo:
            if linha.strip():
                contador += 1
        print('Total de linhas: ', contador)


frase = 'Eu amo comer amoras no café da manhã'
print('Contagem direta', frase.count('amo'))

contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'amo':
        contador += 1
print('Contagem correta: ', contador)

contagem = lista_termos.count('amo')
print(contagem)


lista = ['Arroz', 'Feijao', 'Macarrao']
print(' | '.join(lista))


# arquivo = open('exercicio_1.txt', 'w')
# arquivo.write('Novo Teste 3')
# arquivo.write('\nTeste 4')
# arquivo.close()

# arquivo = open('exercicio_1.txt', 'r')
# arquivo.write('Novo Teste 5')
# arquivo.write('\nTeste 6')
# arquivo.write('\nTeste 8')
# arquivo.write('\nTeste 7')

# linhas = arquivo.readlines()
# for linha in linhas:
#   print('>', linha)

# arquivo.close()


# show_linha('dados/Tarefas.txt')
