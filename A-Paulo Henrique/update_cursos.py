from select_cursos import buscar_nome_em_cursos


def atualizar_cursos(cursor, conn):
    print("\n" * 2)
    while True:
        print("=" * 45)
        print("Alteração da Tabela CURSOS")
        print("-" * 45)

        nome_curso = input("Informe o nome do curso (deixe em branco para voltar): ").strip()
        if nome_curso == "":
            break

        cursos = buscar_nome_em_cursos(nome_curso, cursor)

        if cursos is None:
            print("\nEste nome de curso não foi encontrado.\n")
        else:
            opcao = identificar_curso(nome_curso, cursos)

            if opcao is not None:
                id_curso = cursos[opcao]["id_curso"]
                nome, descricao, duracao = obter_novos_dados()

                if input("\nConfirma os dados? (S/N): ").strip().upper() == "S":

                    sql = '''UPDATE cursos
                             SET nome = ?, descricao = ?, duracao = ?
                             WHERE id_curso = ?;
                          '''

                    cursor.execute(sql, (nome, descricao, duracao, id_curso))
                    conn.commit()


def identificar_curso(nome, cursos):
    while True:
        print("=" * 75)
        print("RELAÇÃO DE CURSOS ENCONTRADOS:")
        print("-" * 75)
        for i, curso in enumerate(cursos):
            print(f"{i+1}) {curso['id_curso']} | {nome} | {curso['descricao']} | {curso['duracao']}")

        if len(cursos) == 1:
            print()
            return 0

        print("-" * 55)
        print(f"0) Voltar")

        print("-" * 75)
        opcao = input("Identifique o aluno de interesse: ")
        if opcao == "0":
            break

        try:
            opcao = int(opcao)
            if opcao <= len(cursos):
                return opcao - 1
        except Exception as e:
            print("Opção inválida. Tente novamente.")
    return None


def obter_novos_dados():
    while True:
        print("\nSOBRE O CURSO, INFORME:")
        nome = input("Nome......: ")
        descricao = input("Descrição.: ")
        duracao = input("Duracao...: ")

        if nome != "":
            return nome, descricao, duracao
        print("Nome inválido.")

