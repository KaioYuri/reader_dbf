# Conversor de DBF para CSV

Este projeto contém um script Python para converter arquivos DBF para CSV. O usuário pode especificar o encoding do arquivo DBF e o número de linhas a serem exportadas.

## Requisitos

- Python 3.6 ou superior
- pip

## Instalação

### Clonar o Repositório

Se você ainda não fez isso, clone este repositório para o seu ambiente local:

```sh
git clone https://github.com/KaioYuri/reader_dbf.git
cd reader_dbf
```

## Criar um Ambiente Virtual

Recomenda-se criar um ambiente virtual para instalar as dependências do projeto:

```sh
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

## Instalar Dependências

Use o arquivo requirements.txt para instalar as dependências necessárias:

```sh
pip install -r requirements.txt
```

## Uso

Execute o script app.py para converter um arquivo DBF para CSV:

```sh
python app.py
```

Você será solicitado a fornecer as seguintes informações:

- Nome do arquivo DBF (por exemplo, ARQUIVO.dbf)
- Tipo de encoding (por exemplo, latin1, cp1252, utf-8, etc.)
- Nome do arquivo de saída (por exemplo, NOME_SAIDA.csv)
- Quantas linhas você quer exportar (digite "todas" para exportar todas as linhas)
