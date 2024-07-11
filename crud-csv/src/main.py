import teste

novo_registro = {'id': '1', 'nome': 'Maria', 'idade': '28'}
teste.criar_registro(novo_registro)

registros = teste.ler_registros()
print(registros)

registro_atualizado = {'id': '1', 'nome': 'Maria Silva', 'idade': '29'}
teste.atualizar_registro(registro_atualizado)

teste.deletar_registro('1')
