
import sqlite3 as conector

try:

    conexao = conector.connect('./dbpessoas.db')
    cursor = conexao.cursor()

    comando = '''
            ALTER TABLE Veiculo ADD motor REAL
    '''

    cursor.execute(comando)

    conexao.commit()

except conector.DatabaseError as err:
    print('Erro de banco de dados', err)

finally:
    # if conexao:
    if conexao:
        cursor.close()
        conexao.close()
