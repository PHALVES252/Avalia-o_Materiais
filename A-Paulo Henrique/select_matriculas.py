def menu_matriculas(cursor):
    while True:
        print("\n" * 2)
        print("-" * 42)
        print("PESQUISAR EM MATRICULAS")
        print("-" * 42)
        print("1) Id matricula")
        print("2) Id aluno")
        print("3) Id curso")
        print("-" * 42)
        print("0) Voltar")
        print("-" * 42)

        opcao = input("Selecione uma opção (1/3) ou 0 para sair: ").strip()

        if opcao == "0":
            print("Voltando ao menu anterior...")
            return

        elif opcao == "1":
            id_matricula = input("Digite o id_matricula: ").strip()
            resposta = busca_id_matricula_em_matriculas(id_matricula, cursor)
            if resposta:
                print(f"Resposta para id_matricula {id_matricula}: {resposta}")
            else:
                print("Matrícula não encontrada.")

        elif opcao == "2":
            id_aluno = input("Digite o id_aluno: ").strip()
            resposta = busca_id_aluno_em_matriculas(id_aluno, cursor)
            if resposta:
                print(f"Respostas encontradas para id_aluno {id_aluno}:")
                for registro in resposta:
                    print(f" > Matrícula {registro['id_matricula']}, Curso: {registro['id_curso']}, Data: {registro['data_matricula']}")
            else:
                print("Aluno não encontrado.")

        elif opcao == "3":
            id_curso = input("Digite o id_curso: ").strip()
            resposta = busca_id_curso_em_matriculas(id_curso, cursor)
            if resposta:
                print(f"\nPara o id_curso igual a {id_curso} os dados encontrados foram:")
                for chave, valor in resposta.items():
                    print(f" > O campo {chave} contém o valor: {valor}")
            else:
                print("Curso não encontrado.")

        else:
            print("Alternativa inválida. Tente novamente.")


def busca_id_matricula_em_matriculas(id_matricula, cursor):
    try:
        cursor.execute("""SELECT * FROM matriculas 
                          WHERE id_matricula = ?""", (id_matricula,))
        resposta = cursor.fetchone()
        if resposta:
            return {
                "id_aluno": resposta[1],
                "id_curso": resposta[2],
                "data_matricula": resposta[3]
            }
        else:
            return None
    except Exception as e:
        print(f"Erro ao buscar matrícula: {e}")
        return None


def busca_id_aluno_em_matriculas(id_aluno, cursor):
    try:
        cursor.execute("""SELECT * FROM matriculas 
                          WHERE id_aluno = ?""", (id_aluno,))
        resposta = cursor.fetchall()
        if resposta:
            registros = []
            for linha in resposta:
                registros.append({
                    "id_matricula": linha[0],
                    "id_curso": linha[2],
                    "data_matricula": linha[3]
                })
            return registros
        else:
            return None
    except Exception as e:
        print(f"Erro ao buscar aluno: {e}")
        return None


def busca_id_curso_em_matriculas(id_curso, cursor):
    try:
        cursor.execute("SELECT * FROM matriculas WHERE id_curso = ?", (id_curso,))
        resposta = cursor.fetchone()
        if resposta:
            return {
                "id_matricula": resposta[0],
                "id_aluno": resposta[1],
                "data_matricula": resposta[3]
            }
        else:
            return None
    except Exception as e:
        print(f"Erro ao buscar curso: {e}")
        return None
