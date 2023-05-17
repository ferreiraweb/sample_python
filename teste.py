import os
import xlrd

arquivo = open ('C:/files/Tarefas.txt', 'r')

conteudo = arquivo.readlines()

#
print("Tipo do conteudo", type(conteudo))

print('Nomde do Arquivo: ', arquivo.name);
print('Modo do arquivo: ', arquivo.mode);
print('Arquivo fechado:  ', arquivo.closed);

print("conteúdo retornado pelo read: ");
print(repr(conteudo));

#

for linha in arquivo:
    print(repr(linha))



arquivo.close()

print('Arquivo fechado:  ', arquivo.closed);

arquivo = open('C:/files/Tarefas.txt', 'w')

arquivo

arquivo.close();

