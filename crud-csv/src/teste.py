import csv

caminho_arquivo = '.\dados.csv'

def ler_dados():
    with open(caminho_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        dados = [dict(linha) for linha in leitor_csv]
    return dados


def salvar_dados(dados):
    with open(caminho_arquivo, 'w') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for linha in dados:
            escritor_csv.writerow(linha.values())


def criar_dados():
    novo_dado = {
        'id': input('Insira o ID: '),
        'nome': input('Insira o nome: '),
        'idade': input('Insira a idade: ')
    }
    dados = ler_dados()
    dados.append(novo_dado)
    salvar_dados(dados)


def ler_todos_os_dados():
    dados = ler_dados()
    for dado in dados:
        print(dado)


def atualizar_dados():
    dados = ler_dados()
    id = input('Insira o ID do registro que deseja atualizar: ')
    for dado in dados:
        if dado['id'] == id:
            dado['nome'] = input('Insira o novo nome: ')
            dado['idade'] = input('Insira a nova idade: ')
            break
    salvar_dados(dados)


def deletar_dados():
    dados = ler_dados()

    id_deletar = input("Digite o ID do registro a ser deletado: ")

    registro_deletar = None
    for registro in dados:
        if registro['id'] == id_deletar:
            registro_deletar = registro
            break
    if registro_deletar:
        dados.remove(registro_deletar)
        print("Registro deletado com sucesso!")
    else:
        print("Registro não encontrado.")

    salvar_dados(dados)


if __name__ == '__main__':
    novo_registro = {'id': '1', 'nome': 'Maria', 'idade': '28'}
    criar_dados(novo_registro)

