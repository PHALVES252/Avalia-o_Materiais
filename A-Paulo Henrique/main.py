import sqlite3

from time import sleep
from criacao_tabelas import criar
from insersao_tabelas import inserir
from pesquisa_tabelas import pesquisar
from atualiza_tabelas import atualizar

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

def selecionar_tabela():
    while True:
        print("\n" * 2)
        print("-" * 44)
        print("MENU DE TABELAS")
        print("-" * 44)
        print("1) Tabela Alunos")
        print("2) Tabela Professores")
        print("3) Tabela Cursos")
        print("4) Tabela Disciplinas")
        print("5) Tabela Avaliações")
        print("6) Tabela Matrículas")
        print("7) Tabela Frequências")
        print("-" * 44)
        print("0) Voltar")
        print("-" * 44)

        opcao = input("Selecione uma tabela (1/7) ou 0 para sair: ").strip()
        if opcao in "01234567":
            return opcao
        print("Alternativa inválida. Tente novamente.")
        sleep(1)


while True:
    print("\n"*2)
    print("*" * 45)
    print(">> MENU PRINCIPAL")
    print("*" * 45)
    print("1) Criar tabelas")
    print("2) Inserir")
    print("3) Pesquisar/Ler")
    print("4) Editar")
    print("5) Excluir Dados")
    print("6) Excluir Tabelas")
    print("-"*45)
    print("0) Sair do programa")
    print("-"*45)

    opcao = input("Escolha uma atividade (1/6) ou 0 para sair: ").strip()
    if opcao == "0":
        break
    elif opcao not in "123456":
        print("\nOpção inválida. Tente novamente.")
        continue

    while True:
        # BUSCAR A TABELA DESEJADA PARA A ATIVIDADE
        tabela = selecionar_tabela()

        if tabela == "0":
            break

        if opcao == "1":  # CRIAÇÃO DE TABELAS
            criar(tabela, cursor, conn)
        elif opcao == "2":  # INSERIR EM TABELAS
            inserir(tabela, cursor, conn)
        elif opcao == "3":  # PESQUISAR/LER TABELAS
            pesquisar(tabela, cursor)
        elif opcao == "4":  # EDITAR DADOS DE TABELAS
            atualizar(tabela, cursor, conn)
        elif opcao == "5":  # EXCLUIR DADOS DE TABELAS
            pass
        elif opcao == "6":  # EXCLUIR TABELAS
            pass

        sleep(0.5)

conn.close()
print("\nFIM DO PROGRAMA")
