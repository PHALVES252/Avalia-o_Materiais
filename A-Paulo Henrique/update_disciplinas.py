from select_disciplinas import buscar_nome_em_disciplinas


def atualizar_disciplinas(cursor, conn):
    while True:
        print("-" * 75)
        nome_disciplina = input("Informe o nome do disciplina: ").strip()
        if nome_disciplina == "":
            return

        dados_disciplinas = buscar_nome_em_disciplinas(nome_disciplina, cursor)
        if dados_disciplinas is None:
            print(f"\nNenhum disciplina chamada '{nome_disciplina}' foi encontrada.\n")
        else:
            indice_lista_disciplinas = identificar_disciplina(nome_disciplina, dados_disciplinas)
            if indice_lista_disciplinas is not None:
                dados_disciplina = dados_disciplinas[indice_lista_disciplinas]
                print("Disciplina selecionada:")
                print(f"{dados_disciplina['id_disciplina']} | {nome_disciplina} | {dados_disciplina['descricao']} | {dados_disciplina['id_curso']} | {dados_disciplina['id_professor']}")
                id_disciplina = dados_disciplina["id_disciplina"]

                # Uma vez obtido o id da disciplina, podemos...
                obter_salvar_novos_dados(id_disciplina, cursor, conn)


def identificar_disciplina(nome, disciplinas):
    while True:
        print("=" * 75)
        print("RELAÇÃO DE DISCIPLINAS ENCONTRADOS:")
        print("-" * 75)

        for i, disciplina in enumerate(disciplinas):
            print(f"{i + 1}) {disciplina['id_disciplina']} | {nome} | {disciplina['descricao']} | {disciplina['id_curso']} | {disciplina['id_professor']}")

        if len(disciplinas) == 1:
            print()
            return 0

        print("-" * 55)
        print(f"0) Voltar")

        print("-" * 75)
        opcao = input("Identifique a disciplina de interesse: ")
        if opcao == "0":
            break
        try:
            opcao = int(opcao)
            if opcao <= len(disciplinas):
                return opcao - 1
        except Exception as e:
            print("Opção inválida. Tente novamente.")
    return None


def obter_salvar_novos_dados(id_disciplina, cursor, conn):
    while True:
        print("=" * 75)
        print("SOBRE A DISCIPLINA, INFORME:")

        nome = input("Nome......: ").strip()

        if nome == "":
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")
            break

        descricao = input("Descrição.: ")
        id_curso = input("Id. Curso.: ")
        id_professor = input("Id. Profe.: ")

        print("-" * 75)
        if input("Confirma os dados? (S/N): ").strip().upper() == "S":
            sql = '''UPDATE disciplinas SET 
                            nome = ?, 
                            descricao = ?,
                            id_curso = ?, 
                            id_professor = ? 
                         WHERE id_disciplina = ?;
                      '''
            cursor.execute(sql, (nome, descricao, id_curso, id_professor, id_disciplina))
            conn.commit()
            print("Dados salvos com sucesso!")
            return
        else:
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")
