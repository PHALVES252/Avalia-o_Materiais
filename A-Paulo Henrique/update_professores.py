from select_professores import buscar_nome_em_professores
from select_professores import buscar_cpf_em_professores
from select_professores import buscar_email_em_professores

def atualizar_professores(cursor, conn):
    while True:
        id_professor = None
        print("")
        print("=" * 45)
        print("Alteração da Tabela professores")
        print("-" * 45)
        print("Localizar professor por...")
        print("1) Nome")
        print("2) CPF")
        print("3) e-mail")
        print("-" * 45)
        print("0) Retornar")

        # cursor.execute("SELECT * FROM professores")
        # prof = cursor.fetchall()
        # print(prof)


        print("-" * 75)
        opcao_pesquisa = input("Informe a forma de pesquisa desejada: ").strip()
        if opcao_pesquisa == "" or opcao_pesquisa == "0":
            break
            
        if opcao_pesquisa == '1':
            id_professor = obter_id_por_nome(cursor)
        elif opcao_pesquisa == '2':
            id_professor = obter_id_por_cpf(cursor)
        elif opcao_pesquisa == '3':
            id_professor = obter_id_por_email(cursor)

        if id_professor != None:
            # Uma vez obtido o id do professor, podemos...
            obter_salvar_novos_dados(id_professor, cursor, conn)


def obter_id_por_nome(cursor):
    while True:
        print("-" * 75)
        nome_professor = input("Informe o nome do professor: ").strip()
        if nome_professor == "":
            break

        dados_professores = buscar_nome_em_professores(nome_professor, cursor)
        if dados_professores is None:
            print(f"\nNenhum professor chamado '{nome_professor}' foi encontrado.\n")
        else:
            indice_lista_professores = identificar_professor(nome_professor, dados_professores)
            if indice_lista_professores is not None:
                dados_professor = dados_professores[indice_lista_professores]
                print("Professor selecionado:")
                print(f"{dados_professor['id_professor']} | {nome_professor} | {dados_professor['cpf']} | {dados_professor['email']}")
                id_professor = dados_professor["id_professor"]
                return id_professor
    
    return None


def identificar_professor(nome, professores):
    while True:
        print("=" * 75)
        print("RELAÇÃO DE PROFESSORES ENCONTRADOS:")
        print("-" * 75)
        for i, professor in enumerate(professores):
            print(f"{i+1}) {professor['id_professor']} | {nome} | {professor['cpf']} | {professor['email']}")

        if len(professores) == 1:
            print()
            return 0

        print("-" * 55)
        print(f"0) Voltar")

        print("-" * 75)
        opcao = input("Identifique o professor de interesse: ")
        if opcao == "0":
            break

        try:
            opcao = int(opcao)
            if opcao <= len(professores):
                return opcao - 1
        except Exception as e:
            print("Opção inválida. Tente novamente.")
    return None


def obter_id_por_cpf(cursor):
    while True:
        print("-" * 75)
        cpf_professor = input("Informe o CPF do professor: ").strip()
        if cpf_professor == "":
            break

        dados_professor = buscar_cpf_em_professores(cpf_professor, cursor)
        if dados_professor is None:
            print(f"\nNenhum professor com CPF '{cpf_professor}' foi encontrado.\n")
        else:
            print("professor encontrado:")
            print(f"{dados_professor['id_professor']} | {dados_professor['nome']} | {cpf_professor} | {dados_professor['email']}")
            id_professor = dados_professor["id_professor"]
            return id_professor

    return None


def obter_id_por_email(cursor):
    cursor.execute("SELECT * FROM professores")
    t = cursor.fetchall()
    print(t)

    while True:
        print("-" * 75)
        email_professor = input("Informe o EMAIL do professor: ").strip()
        if email_professor == "":
            break

        dados_professor = buscar_email_em_professores(email_professor, cursor)
        if dados_professor is None:
            print(f"\nNenhum professor com e-mail '{email_professor}' foi encontrado.\n")
        else:
            print("professor encontrado:")
            print(f"{dados_professor['id_professor']} | {dados_professor['nome']} | {dados_professor['cpf']} | {email_professor}")
            id_professor = dados_professor["id_professor"]
            return id_professor

    return None

def obter_salvar_novos_dados(id_professor, cursor, conn):
    while True:
        print("=" * 75)
        print("SOBRE O PROFESSOR, INFORME:")

        nome = input("Nome......: ").strip()

        if nome == "":
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")
            break

        cpf = input("CPF.......: ")
        email = input("e-Mail....: ")
        telefone = input("Telefone..: ")
        formacao = input("Formação..: ")

        print("-" * 75)
        if input("Confirma os dados? (S/N): ").strip().upper() == "S":
            sql = '''UPDATE professores SET 
                            nome = ?, 
                            cpf = ?, 
                            email = ?, 
                            telefone = ?, 
                            formacao = ?
                         WHERE id_professor = ?;
                      '''
            cursor.execute(sql, (nome, cpf, email, telefone, formacao, id_professor))
            conn.commit()
            print("Dados salvos com sucesso!")
            return
        else:
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")
