import os


try:
    with open('dados/frutas.txt', 'r') as arquivo:
        conteudo = arquivo.read().split(', ')

    with open('dados/resultado1.txt', 'w') as resultado:
        for item in conteudo:
            texto = f'Novo conteudo {item.strip()}\n'
            print('--> ', item)
            resultado.write(texto)

    print('****** conteúdo ******')
    entradas =  os.scandir('./dados')

    for obj in entradas:
         print('Nome: ==>', obj.name)

except OSError as erro:
        print('ocorreu um erro ===> ', erro)


#os.remove('dados/frutas_copy.txt')
#os.rename('dados/frutas_copy.txt', 'dados/frutas2.txt')
