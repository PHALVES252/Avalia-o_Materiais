def menu_avaliacoes(cursor):
    while True:
        print("\n" * 2)
        print("-" * 42)
        print("PESQUISAR EM AVALIACOES")
        print("-" * 42)
        print("1) Id avaliacao")
        print("2) Id disciplina")
        print("3) Id professor")
        print("4) Id aluno")
        print("-" * 42)
        print("0) Voltar")
        print("-" * 42)

        opcao = input("Selecione um campo (1/4) ou 0 para sair: ").strip()
        if opcao in "0":
            return

        elif opcao == "1":
            while True:
                id_avaliacao = pergunta_inteiro("PESQUISA PELO ID DA AVALIAÇÃO", "Insira o ID da avaliação: ")
                if not id_avaliacao:
                    break
                resposta = buscar_id_avaliacao_em_avaliacoes(id_avaliacao, cursor)
                print(f"Ao pesquisar pelo ID da avaliação {id_avaliacao} na tabela AVALIAÇÕES:")
                exibe_resposta_dicionario(resposta)

        elif opcao == "2":
            while True:
                id_disciplina = pergunta_inteiro("PESQUISA PELO ID DA DISCIPLINA", "Insira o ID da disciplina: ")
                if not id_disciplina:
                    break
                resposta = buscar_id_disciplina_em_avaliacoes(id_disciplina, cursor)
                print(f"Ao pesquisar pelo ID da disciplina {id_disciplina} na tabela AVALIAÇÕES:")
                exibe_resposta_lista(resposta)

        elif opcao == "3":
            while True:
                id_professor = pergunta_inteiro("PESQUISA PELO ID DO PROFESSOR", "Insira o ID do professor: ")
                if not id_professor:
                    break
                resposta = buscar_id_professor_em_avaliacoes(id_professor, cursor)
                print(f"Ao pesquisar pelo ID do professor {id_professor} na tabela AVALIAÇÕES:")
                exibe_resposta_lista(resposta)

        elif opcao == "4":
            while True:
                id_aluno = pergunta_inteiro("PESQUISA PELO ID DO ALUNO", "Insira o ID do aluno: ")
                if not id_aluno:
                    break
                resposta = buscar_id_aluno_em_avaliacoes(id_aluno, cursor)
                print(f"Ao pesquisar pelo ID do aluno {id_aluno} na tabela AVALIAÇÕES:")
                exibe_resposta_lista(resposta)


def buscar_id_avaliacao_em_avaliacoes(id_avaliacao, cursor):
    cursor.execute("SELECT * FROM avaliacoes WHERE id_avaliacao = ?", (id_avaliacao,))
    resultado = cursor.fetchone()
    if resultado:
        return {
            "id_disciplina": resultado[1],
            "id_professor": resultado[2],
            "id_aluno": resultado[3],
            "data_avaliacao": resultado[4],
            "nota": resultado[5],
            "descricao": resultado[6]
        }
    else:
        return None


def buscar_id_disciplina_em_avaliacoes(id_disciplina, cursor):
    cursor.execute("SELECT * FROM avaliacoes WHERE id_disciplina = ?", (id_disciplina,))
    resultado = cursor.fetchall()
    if resultado:
        registros = []
        for linha in resultado:
            registros.append({
                "id_avaliacao": linha[0],
                "id_professor": linha[2],
                "id_aluno": linha[3],
                "data_avaliacao": linha[4],
                "nota": linha[5],
                "descricao": linha[6]
            })
        return registros
    else:
        return None


def buscar_id_professor_em_avaliacoes(id_professor, cursor):
    cursor.execute("SELECT * FROM avaliacoes WHERE id_professor = ?", (id_professor,))
    resultado = cursor.fetchall()
    if resultado:
        registros = []
        for linha in resultado:
            registros.append({
                "id_avaliacao": linha[0],
                "id_disciplina": linha[1],
                "id_aluno": linha[3],
                "data_avaliacao": linha[4],
                "nota": linha[5],
                "descricao": linha[6]
            })
        return registros
    else:
        return None


def buscar_id_aluno_em_avaliacoes(id_aluno, cursor):
    cursor.execute("SELECT * FROM avaliacoes WHERE id_aluno = ?", (id_aluno,))
    resultado = cursor.fetchall()
    if resultado:
        registros = []
        for linha in resultado:
            registros.append({
                "id_avaliacao": linha[0],
                "id_disciplina": linha[1],
                "id_professor": linha[2],
                "data_avaliacao": linha[4],
                "nota": linha[5],
                "descricao": linha[6]
            })
        return registros
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


def pergunta_inteiro(cabecalho, mensagem):
    while True:
        print()
        print("-" * 45)
        print(cabecalho)
        print("-" * 45)
        resposta = input(mensagem).strip()
        if resposta == "":
            break
        try:
            resp = int(resposta)
            return resp
        except Exception as e:
            print("Insira um número válido para a pesquisa.")
            