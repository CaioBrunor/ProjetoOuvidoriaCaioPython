from operacoesbd import *
from menu import *

manifestacoes = []

conn = criarConexao('127.0.0.1','root','12345','ouvidoriabd')

while True:
    print("\n👂 Ouvidoria de Caio")
    print("1)📋 Listagem das manifestações \n2)🔍 Listagem de manifestações por tipo \n3)✍️ Criar nova manifestação \n4)📊 Exibir quantidade total de manifestações \n5)🔢 Pesquisar manifestação pelo seu código \n6)❌ Excluir uma manifestação pelo seu código \n7)🚪 Sair do sistema")
    opcao = int(input("\nSelecione a opção desejada: "))

    if opcao == 1:
        manifestacoes = listarManifestacoes(conn)

    elif opcao == 2:
        listarTipo = int(input("1) Reclamação \n2) Elogio \n3) Sugestão\nDigite a opção desejada: "))
        if listarTipo == 1:
            tipo = "Reclamação"
        elif listarTipo == 2:
            tipo = "Elogio"
        elif listarTipo == 3:
            tipo = "Sugestão"
        else:
            print("Opção inválida!")
            tipo = ""
        if tipo != "":
            listarPorTipo(conn, tipo)

    elif opcao == 3:
        nome = input("Digite o seu nome: ")
        numeroManifest = int(input("1 - Reclamação \n2 - Elogio \n3 - Sugestão\n Digite o tipo de manifestação desejada: "))

        if numeroManifestacao == 1:
            tipo = "Reclamação"
            texto = input("Digite a sua reclamação: ")
            if len(texto) == 0:
                print("Inválido, opção não pode estar vazia.")
            else:
                print("Sua reclamação foi adicionada com sucesso!")

        elif numeroManifestacao == 2:
            tipo = "Elogio"
            texto = input("Digite o seu elogio: ")
            if len(texto) == 0:
                print("Inválido, opção não pode estar vazia.")
            else:
                print("Seu elogio foi adicionado com sucesso!")

        elif numeroManifestacao == 3:
            tipo = "Sugestão"
            texto = input("Digite a sua sugestão: ")
            if len(texto) == 0:
                print("Inválido, opção não pode estar vazia.")
            else:
                print("Sua sugestão foi adicionada com sucesso!")

        else:
            print("Opção inválida!")
            tipo = ""
            texto = ""

        if len(texto) != 0:
            criarManifestacao(conn, nome, texto, tipo)

    elif opcao == 4:
        contarManifestacoes(conn)

    elif opcao == 5:
        manifestacoes = buscarManifestacoes(conn)
        if len(manifestacoes) != 0:
            pesqManifestacao = int(input("\nDigite o código da manifestação desejada: "))
            if pesquisarManifestacao >= 1 and pesquisarManifestacao <= len(manifestacoes):
                manifestacaoPesquisada = manifestacoes[pesquisarManifestacao - 1]
                print("A manifestação pesquisada é", manifestacaoPesquisada)
            else:
                print("Opção inválida.")

    elif opcao == 6:
        print("Lista de manifestações:")
        for i in range(len(manifestacoes)):
            print(i + 1,"-",manifestacoes[i])
        codigoManifestacao = int(input("Digite o código da manifestação a ser removido: "))
        excluirPorCodigo(conn, codigoManifestacao)

    elif opcao == 7:
        print("Você escolheu sair do sistema, muito obrigado por utilizar nossa ouvidoria, volte sempre! =D")
        break

    else:
        print("Opção inválida.")

encerrarConexao(conn)
