import sqlite3 as conector

try:

    conexao = conector.connect("./dbpessoas.db")
    cursor = conexao.cursor()

    comandoPessoa = '''
                CREATE TABLE Pessoa (
                    cpf INTERGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY(cpf)
                )
    '''

    comandoMarca = '''
                CREATE TABLE Marca (
                id INTERGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY(id)
                )
    '''

    comandoVeiculo = '''
                CREATE TABLE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano INTERGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTERGER NOT NULL,
                marca INTERGER NOT NULL,
                PRIMARY KEY (placa),
                FOREIGN KEY (proprietario) REFERENCES Pessoa (cpf),
                FOREIGN KEY (marca) REFERENCES Marca (id)


                )
    
    '''

    cursor.execute(comandoPessoa)
    cursor.execute(comandoMarca)
    cursor.execute(comandoVeiculo)
    # cursor.fetchall()

    conexao.commit()

except conector.DatabaseError as err:
    print('Erro de banco de dados', err)

finally:
    # if conexao:
    if conexao:
        cursor.close()
        conexao.close()
