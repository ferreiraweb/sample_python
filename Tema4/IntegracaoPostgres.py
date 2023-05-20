import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres",
                        password="caetel23", host="127.0.0.1", port="5432")

print("Conexão com o Banco de Dados aberta com sucesso!")

cur = conn.cursor()

# --- -------------------------- CREATE TABLE
# cur.execute(
#    '''CREATE TABLE Agenda(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));''')
# print("Tabela criada com sucesso!")


# ---- ------------------------- INSERT

# cur.execute(
#    """INSERT INTO Agenda ("id", "nome" , "telefone" ) VALUES (1, 'Paulo' , '02199999999' )""")
# cur.execute(
#    """INSERT INTO Agenda ("id", "nome" , "telefone" ) VALUES (2, 'Pedro' , '0215558-5568' )""")
# cur.execute(
#    """INSERT INTO Agenda ("id", "nome" , "telefone" ) VALUES (3, 'Sergio' , '0214526-5639' )""")

# --- ------------------------ SELECT

cur.execute("""select * from Agenda where "id"=1""")
registro = cur.fetchone()
print(registro)
print("Seleção realizada com sucesso!")


# -- ------------------------ UPDATE


cur.execute("""Update Agenda set "telefone"='02188888888' where "id"=1""")
conn.commit()
print("Registro Atualizado com sucesso! ")
cur = conn.cursor()
print(" Consulta depois da atualização")
cur.execute("""select * from Agenda where "id"=1""")
registro = cur.fetchone()
print(registro)


# --- ----------------------- DELETE


cur.execute("""Delete from Agenda where "id"=3""")
conn.commit()
cont = cur.rowcount
print(cont, "Registro excluído com sucesso!")
print("Exclusão realizada com sucesso!")

cur.execute("""select nome from Agenda""")
registro = cur.fetchall()
print(registro)


conn.commit()

conn.close()
