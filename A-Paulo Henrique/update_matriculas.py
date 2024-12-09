from select_alunos import buscar_nome_em_alunos
from update_alunos import identificar_aluno
from select_cursos import buscar_nome_em_cursos
from update_cursos import identificar_curso


def atualizar_matriculas(cursor, conn):
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

        # IDENTIFICANDO O CURSO
        while True:
            print("-" * 75)
            nome_curso = input("\nInforme nome do curso.: ").strip()
            if nome_curso == "":
                break
            dados_cursos = buscar_nome_em_cursos(nome_curso, cursor)
            if dados_cursos is None:
                print(f"\nNenhum curso chamada '{nome_curso}' foi encontrada.\n")
                continue
            else:
                indice_lista_cursos = identificar_curso(nome_curso, dados_cursos)
                if indice_lista_cursos is None:
                    continue
                # OBTENDO O ID DO CURSO
                dados_curso = dados_cursos[indice_lista_cursos]
                print("\nAluno selecionado:")
                print(f"{dados_aluno['id_aluno']} | {nome_aluno} | {dados_aluno['cpf']} | {dados_aluno['email']} | {dados_aluno['telefone']}")
                print("Curso selecionada:")
                print(f"{dados_curso['id_curso']} | {nome_curso} | {dados_curso['descricao']}")
                id_curso = dados_curso["id_curso"]

            # OBTENDO A DATA DA AVALIAÇÃO
            while True:
                print("-" * 75)
                data_matricula = input("Informe a data da matricula: ").strip()
                if data_matricula == "":
                    break

                # OBTENDO O ID DA AVALIAÇÃO
                id_matricula = buscar_id_da_matriculas(id_curso, id_aluno, data_matricula, cursor)
                if id_matricula:
                    obter_salvar_novos_dados(id_matricula, cursor, conn)
                    break
                else:
                    print(f"\nNENHUMA MATRÍCULA DO ALUNO '{nome_aluno}' NA DISCIPLIMA '{nome_curso}' NO DIA '{data_matricula}'.")


def obter_salvar_novos_dados(id_matricula, cursor, conn):
    while True:
        print("=" * 75)
        print("SOBRE A MATRICULA, INFORME:")
        data = input("Data......: ").strip()
        if data == "":
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")
            break

        print("-" * 75)
        if input("Confirma os dados? (S/N): ").strip().upper() == "S":
            sql = '''UPDATE matriculas SET 
                            data_matricula = ? 
                         WHERE id_matricula = ?;
                      '''
            cursor.execute(sql, (data, id_matricula))
            conn.commit()
            print("Dados salvos com sucesso!")
            return
        else:
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")


def buscar_id_da_matriculas(id_curso, id_aluno, data_matricula, cursor):
    cursor.execute("""SELECT id_matricula FROM matriculas 
                        WHERE id_aluno == ? AND
                              id_curso = ? AND
                              data_matricula == ?""", (id_aluno, id_curso, data_matricula))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    return None
