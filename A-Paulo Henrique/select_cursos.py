def menu_cursos(cursor):
    while True:
        print("\n" * 2)
        print("-" * 42)
        print("PESQUISAR EM CURSOS")
        print("-" * 42)
        print("1) Id curso")
        print("2) Nome")
        print("-" * 42)
        print("0) voltar")
        print("-" * 42)

        opcao = input("selecione um campo (1/4) ou 0 para sair: ").strip()
        if opcao in "0":
            return

        if opcao == "1":
            id_curso = "1"
            resposta = buscar_id_curso_em_cursos(id_curso, cursor)
            print(f"\nAo pesquisar pelo id {id_curso} na tabela CURSOS:")
            exibe_resposta_dicionario(resposta)

        elif opcao == "2":
            while True:
                nome = pergunta_string("PESQUISA PELO NOME DO CURSO", "Insira o nome do curso: ")
                if not nome:
                    break
                resposta = buscar_nome_em_cursos(nome, cursor)
                print(f"\nAo pesquisar por {nome} na tabela CURSOS:")
                exibe_resposta_lista(resposta)


def buscar_nome_em_cursos(nome, cursor):
    cursor.execute("SELECT * FROM cursos WHERE nome = ?", (nome,))
    resultado = cursor.fetchall()
    if resultado:
        registros = []
        for linha in resultado:
            registros.append({
                    "id_curso": linha[0],
                    "descricao": linha[2],
                    "duracao": linha[3]
                    })
        return registros
    else:
        return None


def buscar_id_curso_em_cursos(id_curso, cursor):
    cursor.execute("SELECT * FROM cursos WHERE id_curso = ?", (id_curso,))
    resposta = cursor.fetchone()
    if resposta:
        return {
            "nome": resposta[1],
            "descricao": resposta[2],
            "duracao": resposta[3]
        }
    else:
        return None

def exibe_resposta_lista(lista):
    if lista is None:
        print("  Ops! :-|  Nenhum registro foi encontrado.")
    else:
        for linha in lista:
            exibe_resposta_dicionario(linha)

def exibe_resposta_dicionario(dicionario):
    if dicionario is None:
        print("  Vixe! :-(  Nenhum registro foi encontrado.")
    else:
        for chave, valor in dicionario.items():
            print(f"  O campo: '{chave}' contém o valor: '{valor}'.")

def pergunta_string(cabecalho, mensagem):
    while True:
        print()
        print("_" * 45)
        print(cabecalho)
        print("_" * 45)
        resposta = input(mensagem).strip()
        if resposta == "":
                break
        return resposta