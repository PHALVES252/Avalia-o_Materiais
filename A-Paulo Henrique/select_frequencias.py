def menu_frequencias(cursor):
    while True:
        print("\n" * 2)
        print("-" * 42)
        print("PESQUISAR EM DISCIPLINAS")
        print("-" * 42)
        print("1) Id frequencia")
        print("2) Id aluno")
        print("3) Id disciplina")
        print("4) Id matricula")
        print("-" * 42)
        print("0) Voltar")
        print("-" * 42)

        opcao = input("Selecione um campo (1/4) ou 0 para sair: ").strip()
        if opcao in "0":
            return

        if opcao == "1":
            id_frequencias = "2"
            resposta = busca_id_frequencias_em_frequencias(id_frequencias, cursor)
            print(f"Ao pesquisar pelo ID da frequência {id_frequencias} na tabela FREQUÊNCIAS:")
            exibe_resposta_dicionario(resposta)

        elif opcao == "2":
            id_aluno = "1"
            resposta = busca_id_aluno_em_frequencias(id_aluno, cursor)
            exibe_resposta_lista(resposta)

        elif opcao == "3":
            id_disciplina = "3"
            resposta = busca_id_disciplina_em_frequencias(id_disciplina, cursor)
            exibe_resposta_lista(resposta)

        elif opcao == "4":
            id_matricula = "4"
            resposta = busca_id_matricula_em_frequencias(id_matricula, cursor)
            exibe_resposta_lista(resposta)
        else:
            print("Alternativa inválida. Tente novamente.")


def busca_id_frequencias_em_frequencias(id, cursor):
    cursor.execute('SELECT * FROM frequencias WHERE id_frequencia = ?', (id,))
    resposta = cursor.fetchone()
    if resposta:
       return {
           "id_aluno": resposta[1],
           "id_matricula": resposta[2],
           "id_diciplina": resposta[3],
           "data": resposta[4],
           "presente": resposta[5]
       }
    else:
        return None


def busca_id_aluno_em_frequencias(id, cursor):
    cursor.execute('SELECT * FROM frequencias WHERE id_aluno = ?', (id,))
    resposta = cursor.fetchall()
    if resposta:
        registros = []
        for linha in resposta:
            registros.append({
                "id_frequencia": linha[0],
                "id_matricula": linha[2],
                "id_diciplina": linha[3],
                "data": linha[4],
                "presente": linha[5]
            })
        return registros
    else:
        return None


def busca_id_matricula_em_frequencias(id, cursor):
    cursor.execute('SELECT * FROM frequencias WHERE id_matricula = ?', (id,))
    resposta = cursor.fetchall()
    if resposta:
        registros = []
        for linha in resposta:
            registros.append({
                "id_frequencia": linha[0],
                "id_aluno": linha[1],
                "id_disciplina": linha[3],
                "data": linha[4],
                "presente": linha[5]
            })
        return registros
    else:
        return None


def busca_id_disciplina_em_frequencias(id, cursor):
    cursor.execute('SELECT * FROM frequencias WHERE id_disciplina = ?', (id,))
    resposta = cursor.fetchall()
    if resposta:
        registros = []
        for linha in resposta:
            registros.append({
                "id_frequencia": linha[0],
                "id_aluno": linha[1],
                "id_matricula": linha[2],
                "data": linha[4],
                "presente": linha[5]
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