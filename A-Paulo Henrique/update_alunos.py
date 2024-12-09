from select_alunos import buscar_nome_em_alunos
from select_alunos import buscar_cpf_em_alunos
from select_alunos import buscar_email_em_alunos
from select_alunos import buscar_telefone_em_alunos

def atualizar_alunos(cursor, conn):
    while True:
        id_aluno = None
        print("")
        print("=" * 45)
        print("Alteração da Tabela ALUNOS")
        print("-" * 45)
        print("Localizar aluno por...")
        print("1) Nome")
        print("2) CPF")
        print("3) e-mail")
        print("4) Telefone")
        print("-" * 45)
        print("0) Retornar")

        print("-" * 75)
        opcao_pesquisa = input("Informe a forma de pesquisa desejada: ").strip()
        if opcao_pesquisa == "" or opcao_pesquisa == "0":
            break
            
        if opcao_pesquisa == '1':
            id_aluno = obter_id_por_nome(cursor)
        elif opcao_pesquisa == '2':
            id_aluno = obter_id_por_cpf(cursor)
        elif opcao_pesquisa == '3':
            id_aluno = obter_id_por_email(cursor)
        elif opcao_pesquisa == '4':
            id_aluno = obter_id_por_telefone(cursor)

        if id_aluno != None:
            # Uma vez obtido o id do aluno, podemos...
            obter_salvar_novos_dados(id_aluno, cursor, conn)


def obter_id_por_nome(cursor):
    while True:
        print("-" * 75)
        nome_aluno = input("Informe o nome do aluno: ").strip()
        if nome_aluno == "":
            break

        dados_alunos = buscar_nome_em_alunos(nome_aluno, cursor)
        if dados_alunos is None:
            print(f"\nNenhum aluno chamado '{nome_aluno}' foi encontrado.\n")
        else:
            indice_lista_alunos = identificar_aluno(nome_aluno, dados_alunos)
            if indice_lista_alunos is not None:
                dados_aluno = dados_alunos[indice_lista_alunos]
                print("Aluno selecionado:")
                print(f"{dados_aluno['id_aluno']} | {nome_aluno} | {dados_aluno['cpf']} | {dados_aluno['email']} | {dados_aluno['telefone']}")
                id_aluno = dados_aluno["id_aluno"]
                return id_aluno
    
    return None


def identificar_aluno(nome, alunos):
    while True:
        print("=" * 75)
        print("RELAÇÃO DE ALUNOS ENCONTRADOS:")
        print("-" * 75)
        for i, aluno in enumerate(alunos):
            print(f"{i+1}) {aluno['id_aluno']} | {nome} | {aluno['cpf']} | {aluno['email']} | {aluno['telefone']}")

        if len(alunos) == 1:
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
            if opcao <= len(alunos):
                return opcao - 1
        except Exception as e:
            print("Opção inválida. Tente novamente.")
    return None


def obter_id_por_cpf(cursor):
    while True:
        print("-" * 75)
        cpf_aluno = input("Informe o CPF do aluno: ").strip()
        if cpf_aluno == "":
            break

        dados_aluno = buscar_cpf_em_alunos(cpf_aluno, cursor)
        if dados_aluno is None:
            print(f"\nNenhum aluno com CPF '{cpf_aluno}' foi encontrado.\n")
        else:
            print("Aluno encontrado:")
            print(f"{dados_aluno['id_aluno']} | {dados_aluno['nome']} | {cpf_aluno} | {dados_aluno['email']} | {dados_aluno['telefone']}")
            id_aluno = dados_aluno["id_aluno"]
            return id_aluno

    return None


def obter_id_por_email(cursor):
    cursor.execute("SELECT * FROM alunos")
    t = cursor.fetchall()
    print(t)

    while True:
        print("-" * 75)
        email_aluno = input("Informe o EMAIL do aluno: ").strip()
        if email_aluno == "":
            break

        dados_aluno = buscar_email_em_alunos(email_aluno, cursor)
        if dados_aluno is None:
            print(f"\nNenhum aluno com e-mail '{email_aluno}' foi encontrado.\n")
        else:
            print("Aluno encontrado:")
            print(f"{dados_aluno['id_aluno']} | {dados_aluno['nome']} | {dados_aluno['cpf']} | {email_aluno}")
            id_aluno = dados_aluno["id_aluno"]
            return id_aluno

    return None

def obter_id_por_telefone(cursor):
    while True:
        print("-" * 75)
        telefone_aluno = input("Informe o TELEFONE do aluno: ").strip()
        if telefone_aluno == "":
            break

        dados_aluno = buscar_telefone_em_alunos(telefone_aluno, cursor)
        if dados_aluno is None:
            print(f"\nNenhum aluno com telefone '{telefone_aluno}' foi encontrado.\n")
        else:
            print("Aluno encontrado:")
            print(f"{dados_aluno['id_aluno']} | {dados_aluno['nome']} | {dados_aluno['cpf']} | {dados_aluno['email']} | {telefone_aluno}")
            id_aluno = dados_aluno["id_aluno"]
            return id_aluno

    return None

def obter_salvar_novos_dados(id_aluno, cursor, conn):
    while True:
        print("=" * 75)
        print("SOBRE O ALUNO, INFORME:")

        nome = input("Nome......: ").strip()

        if nome == "":
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")
            break

        cpf = input("CPF.......: ")
        email = input("e-Mail....: ")
        data_nascimento = input("DT. Nasc..: ")
        telefone = input("Telefone..: ")
        endereco = input("Endereço..: ")

        print("-" * 75)
        if input("Confirma os dados? (S/N): ").strip().upper() == "S":
            sql = '''UPDATE alunos SET 
                            nome = ?, 
                            data_nascimento = ?,
                            cpf = ?, 
                            email = ?, 
                            telefone = ?, 
                            endereco = ?
                         WHERE id_aluno = ?;
                      '''
            cursor.execute(sql, (nome, data_nascimento, cpf, email, telefone, endereco, id_aluno))
            conn.commit()
            print("Dados salvos com sucesso!")
            return
        else:
            print("NENHUMA ALTERAÇÃO FOI REALIZADA.\n")
