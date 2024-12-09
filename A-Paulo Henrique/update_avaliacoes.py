from select_disciplinas import buscar_nome_em_disciplinas
from update_disciplinas import identificar_disciplina

from select_alunos import buscar_nome_em_alunos
from update_alunos import identificar_aluno


def atualizar_avaliacoes(cursor, conn):
    while True:
        print("-" * 75)
        nome_aluno = input("Informe o nome do aluno....: ").strip()
        if nome_aluno == "":
            return

        # IDENTIFICANDO O ALUNO
        dados_alunos = buscar_nome_em_alunos(nome_aluno, cursor)
        if dados_alunos is None:
            print(f"\nNenhum aluno chamado '{nome_aluno}' foi encontrado.\n")
            continue
        else:
            indice_lista_alunos = identificar_aluno(nome_aluno, dados_alunos)
            if indice_lista_alunos is None:
                continue
            # OBTENDO O ID DO ALUNO
            dados_aluno = dados_alunos[indice_lista_alunos]
            print("\nAluno selecionado:")
            print(f"{dados_aluno['id_aluno']} | {nome_aluno} | {dados_aluno['cpf']} | {dados_aluno['email']} | {dados_aluno['telefone']}")
            id_aluno = dados_aluno["id_aluno"]

        # IDENTIFICANDO A DISCIPLINA
        while True:
            print("-" * 75)
            nome_disciplina = input("\nInforme nome da disciplina.: ").strip()
            if nome_disciplina == "":
                break
            dados_disciplinas = buscar_nome_em_disciplinas(nome_disciplina, cursor)
            if dados_disciplinas is None:
                print(f"\nNenhum disciplina chamada '{nome_disciplina}' foi encontrada.\n")
                continue
            else:
                indice_lista_disciplinas = identificar_disciplina(nome_disciplina, dados_disciplinas)
                if indice_lista_disciplinas is None:
                    continue
                # OBTENDO O ID DA DISCIPLINA
                dados_disciplina = dados_disciplinas[indice_lista_disciplinas]
                print("\nAluno selecionado:")
                print(f"{dados_aluno['id_aluno']} | {nome_aluno} | {dados_aluno['cpf']} | {dados_aluno['email']} | {dados_aluno['telefone']}")
                print("Disciplina selecionada:")
                print(f"{dados_disciplina['id_disciplina']} | {nome_disciplina} | {dados_disciplina['descricao']} | {dados_disciplina['id_curso']} | {dados_disciplina['id_professor']}")
                id_disciplina = dados_disciplina["id_disciplina"]

            # OBTENDO A DATA DA AVALIAÇÃO
            while True:
                print("-" * 75)
                data_avaliacao = input("Informe a data da avaliacao: ").strip()
                if data_avaliacao == "":
                    break

                # OBTENDO O ID DA AVALIAÇÃO
                id_avaliacao = buscar_id_da_avaliacoes(id_disciplina, id_aluno, data_avaliacao, cursor)
                if id_avaliacao:
                    obter_salvar_novos_dados(id_avaliacao, cursor, conn)
                else:
                    print(f"\nNENHUMA AVALIAÇÃO DO ALUNO '{nome_aluno}' NA DISCIPLIMA '{nome_disciplina}' NO DIA '{data_avaliacao}'.")


def obter_salvar_novos_dados(id_avaliacao, cursor, conn):
    while True:
        print("=" * 75)
        print("SOBRE A AVALIACAO, INFORME:")

        nota = input("Nota......: ").strip()
        descricao = input("Descrição.: ")

        if nota == "":
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")
            break

        print("-" * 75)
        if input("Confirma os dados? (S/N): ").strip().upper() == "S":
            sql = '''UPDATE avaliacoes SET 
                            nota = ?, 
                            descricao = ?,
                         WHERE id_avaliacao = ?;
                      '''
            cursor.execute(sql, (nota, descricao, id_avaliacao))
            conn.commit()
            print("Dados salvos com sucesso!")
            return
        else:
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")


def buscar_id_da_avaliacoes(id_disciplina, id_aluno, data_avaliacao, cursor):
    cursor.execute("""SELECT id_avaliacao FROM avaliacoes 
                        WHERE id_aluno == ? AND
                              id_disciplina = ? AND
                              data_avaliacao == ?""", (id_aluno, id_disciplina, data_avaliacao))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    return None
