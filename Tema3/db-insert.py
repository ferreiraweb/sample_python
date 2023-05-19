import sqlite3 as conector
from modelo import Pessoa, Marca, Veiculo


conexao = conector.connect('dbpessoas.db')
# conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

# comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (12345678, 'Joao', '2000-01-31', 1)'''
# comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (987654321, 'Pedro', '1998-02-14', 0)'''


# pessoa = Pessoa(122588, 'Josefa', '1994-05-05', False)
# comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?)'''
# cursor.execute(comando, (pessoa.cpf, pessoa.nome,
#              pessoa.data_nascimento, pessoa.usa_oculos))

# Argumento nomeados - a ordem pode ser alterada
# pessoa = Pessoa(7775588, 'Emanuel', '1996-04-25', True)
# comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (:p1, :p2, :p3, :p4)'''
# cursor.execute(comando, {'p2': pessoa.cpf, 'p1': pessoa.nome,
#               'p4': pessoa.usa_oculos, 'p3': pessoa.data_nascimento, })

# Inserção de dados na tabela Marca
comando1 = '''INSERT INTO Marca (id, nome, sigla) VALUES (:id, :nome, :sigla);'''

marca1 = Marca("Marca A", "MA")
cursor.execute(comando1, {'id': 1, 'nome': marca1.nome, 'sigla': marca1.sigla})
marca1.id = cursor.lastrowid

marca2 = Marca("Marca B", "MB")
# cursor.execute(comando1, vars(marca2))
cursor.execute(comando1, {'id': 2, 'nome': marca2.nome, 'sigla': marca2.sigla})
marca2.id = cursor.lastrowid

# Inserção de dados na tabela Veiculo
comando2 = '''INSERT INTO Veiculo
                VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''
veiculo1 = Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, marca1.id)
veiculo2 = Veiculo("BAA0002", 2002, "Preto", 1.4, 10000000099, marca1.id)
veiculo3 = Veiculo("CAA0003", 2003, "Branco", 2.0, 20000000099, marca2.id)
veiculo4 = Veiculo("DAA0004", 2004, "Azul", 2.2, 30000000099, marca2.id)
cursor.execute(comando2, vars(veiculo1))
cursor.execute(comando2, vars(veiculo2))
cursor.execute(comando2, vars(veiculo3))
cursor.execute(comando2, vars(veiculo4))


conexao.commit()

cursor.close()
conexao.close()
