from operacoesbd import *

def listarManifestacoes(conn):
    consulta = 'select * from manifestacoes'
    manifestacoes = listarBancoDados(conn, consulta)

    if len(manifestacoes) == 0:
        print("Não existem manifestações a serem listadas.")
    else:
        print("Lista de Manifestações")
        for i in manifestacoes:
            print("-", i)
    return manifestacoes  

def listarPorTipo(conn, tipo):
    comando = "select nome,manifestacao,tipo from manifestacoes where tipo = %s"
    dados = [tipo]
    manifestacoes = listarBancoDados(conn, comando, dados)

    if len(manifestacoes) == 0:
        print("Não há manifestações deste tipo a serem exibidas.")
    else:
        print("Lista de", tipo)
        for i in range(len(manifestacoes)):
            print(i + 1, "-", manifestacoes[i])

def criarManifestacao(conn, nome, texto, tipo):
    comando = "insert into manifestacoes (nome, manifestacao, tipo) values (%s, %s, %s)"
    dados = (nome, texto, tipo)
    insertNoBancoDados(conn, comando, dados)

def contarManifestacoes(conn):
    consulta = 'select count(*) from manifestacoes'
    resultado = listarBancoDados(conn, consulta)
    quantidade = resultado[0][0]
    print("Temos", quantidade, "manifestações no nosso sistema.")

def buscarManifestacoes(conn):
    consulta = 'select * from manifestacoes'
    manifestacoes = listarBancoDados(conn, consulta)

    if len(manifestacoes) == 0:
        print("Não existem manifestações a serem exibidas.")
    else:
        print("As manifestações a serem exibidas são: \n")
        for i in range(len(manifestacoes)):
            print(i + 1, "-", manifestacoes[i])
    return manifestacoes  # Para uso na busca e exclusão

def excluirPorCodigo(conn, codigo):
    comando = "delete from manifestacoes where codigo = %s"
    dados = [codigo]
    linhas = excluirBancoDados(conn, comando, dados)

    if linhas == 0:
        print("Não existe nenhuma manifestação para o código informado.")
    else:
        print("Manifestação removida com sucesso!")
