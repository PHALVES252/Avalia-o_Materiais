def menu_disciplina(cursor):
    while True:
        print("\n" * 2)
        print("-" * 42)
        print("PESQUISAR EM DISCIPLINAS")
        print("-" * 42)
        print("1) Id disciplina")
        print("2) Id curso")
        print("3) Id professor")
        print("4) Nome")
        print("-" * 42)
        print("0) Voltar")
        print("-" * 42)

        opcao = input("Selecione um campo (1/4) ou 0 para sair: ").strip()
        if opcao in "0":
            return

        if opcao == "1":
            while True:
                id_disciplina = pergunta_inteiro("PESQUISA PELO ID DA DISCIPLINA", "Digite o ID da disciplina: ")
                if not id_disciplina:
                    break
                resposta = buscar_id_disciplina_em_disciplinas(id_disciplina, cursor)
                print(f"Ao pesquisar pelo id '{id_disciplina}' na tabela DISCIPLINAS encontramos:")
                exibe_resposta_dicionario(resposta)

        elif opcao == "2":
            while True:
                id_curso = pergunta_inteiro("PESQUISA PELO ID DO CURSO", "Digite o ID do curso: ")
                if not id_curso:
                    break
                resposta = buscar_id_curso_em_disciplinas(id_curso, cursor)
                print(f"Ao pesquisar pelo id curso '{id_curso}' na tabela DISCIPLINAS encontramos:")
                exibe_resposta_lista(resposta)

        elif opcao == "3":
            while True:
                id_professor = pergunta_inteiro("PESQUISA PELO ID DO PROFESSOR", "Digite o ID do professor: ")
                if not id_professor:
                    break
                resposta = buscar_id_professor_em_disciplinas(id_professor, cursor)
                print(f"Ao pesquisar pelo id professor '{id_professor}' na tabela DISCIPLINAS encontramos:")
                exibe_resposta_lista(resposta)

        elif opcao == "4":
            while True:
                nome = pergunta_string("PESQUISA PELO NOME DA DISCIPLINA", "Digite o NOME da disciplina: ")
                if not nome:
                    break
                resposta = buscar_nome_em_disciplinas(nome, cursor)
                print(f"Ao pesquisar pelo nome '{nome}' na tabela DISCIPLINAS encontramos:")
                exibe_resposta_dicionario(resposta)

        else:
            print("Alternativa inválida. Tente novamente.")


def buscar_id_disciplina_em_disciplinas(id_disciplina, cursor):
    cursor.execute("SELECT * FROM disciplinas WHERE id_disciplina = ?", (id_disciplina,))
    resposta = cursor.fetchone()
    if resposta:
        return {
            "id_curso": resposta[1],
            "id_professor": resposta[2],
            "nome": resposta[3],
            "descricao": resposta[4]
        }
    else:
        return None


def buscar_id_curso_em_disciplinas(id_curso, cursor):
    cursor.execute("SELECT * FROM disciplinas WHERE id_curso = ?", (id_curso,))
    resposta = cursor.fetchall()
    if resposta:
        registros = []
        for linha in resposta:
            registros.append({
                    "id_disciplina": linha[0],
                    "id_professor": linha[2],
                    "nome": linha[3],
                    "descricao": linha[4]
                    })
        return registros
    else:
        return None


def buscar_id_professor_em_disciplinas(id_professor, cursor):
    cursor.execute("SELECT * FROM disciplinas WHERE id_professor = ?", (id_professor,))
    resposta = cursor.fetchall()
    if resposta:
        registros = []
        for linha in resposta:
            registros.append({
                "id_disciplina": linha[0],
                "id_curso": linha[1],
                "nome": linha[3],
                "descricao": linha[4]
                })
        return registros
    else:
        return None


def buscar_nome_em_disciplinas(nome, cursor):
    cursor.execute("SELECT * FROM disciplinas WHERE nome = ?", (nome,))
    resposta = cursor.fetchall()
    if resposta:
        registros = []
        for linha in resposta:
            registros.append({
                "id_disciplina": linha[0],
                "id_curso": linha[1],
                "id_professor": linha[2],
                "descricao": linha[4]
                })
        return registros
    else:
        return None


def pergunta_inteiro(cabecalho, mensagem):
    while True:
        print()
        print("_" * 45)
        print(cabecalho)
        print("_" * 45)
        resposta = input(mensagem).strip()
        if resposta == "":
            break
        try:
            resp = int(resposta)
            return resp
        except Exception as e:
            print("Insira dados válidos!!")


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
