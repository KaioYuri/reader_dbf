from dbfread import DBF
import pandas as pd

# Solicitar os dados do usuário
arq_dbf = input('Nome do arquivo DBF: ')
encoding = input('Qual o tipo do encoding \n(Opções: latin1, cp1252, \nutf-8, ascii, \niso-8859-15, cp850, \ncp437, utf-16, \nmacroman): ')
arq_output = input('Qual o nome do arquivo de saída: ')
num_linhas = input('Quantas linhas você quer exportar? (Digite "todas" para exportar tudo): ')

# Carregar o arquivo DBF com o encoding especificado
table = DBF(arq_dbf, encoding=encoding)

# Converter a tabela DBF em um DataFrame do pandas
df = pd.DataFrame(iter(table))

# Exportar para o CSV com base no número de linhas solicitado
if num_linhas.lower() == 'todas':
    df.to_csv(arq_output, index=False, encoding='utf-8')
else:
    try:
        num_linhas = int(num_linhas)
        df.head(num_linhas).to_csv(arq_output, index=False, encoding='utf-8')
    except ValueError:
        print('Entrada inválida para o número de linhas. Exportando todas as linhas.')
        df.to_csv(arq_output, index=False, encoding='utf-8')

print(f'Arquivo CSV {arq_output} foi criado com sucesso.')
