
import xlrd

planilha = xlrd.open_workbook("dados/dicionario_pessoas.xls")
primeira_aba = planilha.sheet_by_index(0)
print('Nome: ', primeira_aba.name)
print('Num linhas: ', primeira_aba.nrows)
print('Num colunas: ', primeira_aba.ncols)

for idx, linha in enumerate(primeira_aba.get_rows()):
    print(linha)
    if idx > 20:
        break


