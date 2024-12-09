def menu_alunos(cursor):
    while True:
        print("\n" * 2)
        print("-" * 42)
        print("PESQUISAR EM ALUNOS")
        print("-" * 42)
        print("1) Id aluno")
        print("2) Nome")
        print("3) CPF")
        print("4) E-Mail")
        print("5) Telefone")
        print("-" * 42)
        print("0) Voltar")
        print("-" * 42)

        opcao = input("Selecione um campo (1/5) ou 0 para voltar: ").strip()
        if opcao in "0":
            return

        if opcao == "1":  # id_aluno
            while True:
                id_aluno = pergunta_inteiro("PESQUISA PELO ID DO ALUNO", "Insira o ID do Aluno: ")
                if not id_aluno:
                    break
                resposta = buscar_id_aluno_em_alunos(id_aluno, cursor)
                print(f"\nAo pesquisar pelo ID {id_aluno} na tabela ALUNOS:")
                exibe_resposta_dicionario(resposta)

        elif opcao == "2":  # nome
            while True:
                nome = pergunta_string("PESQUISA PELO NOME DO ALUNO", "Insira o nome do aluno: ")
                if not nome:
                    break
                resposta = buscar_nome_em_alunos(nome, cursor)
                print(f"\nAo pesquisar pelo nome {nome} na tabela ALUNOS:")
                exibe_resposta_lista(resposta)

        elif opcao == "3":
            while True:
                cpf = pergunta_string("PESQUISA PELO CPF DO ALUNO", "Insira o CPF do aluno: ")
                if not cpf:
                    break
                resposta = buscar_cpf_em_alunos(cpf, cursor)
                print(f"\nAo pesquisar pelo CPF {cpf} na tabela ALUNOS:")
                exibe_resposta_dicionario(resposta)

        elif opcao == "4":
            while True:
                email = pergunta_string("PESQUISA PELO EMAIL DO ALUNO", "Insira o email do aluno: ")
                if not email:
                    break
                resposta = buscar_email_em_alunos(email, cursor)
                print(f"\nAo pesquisar pelo email {email} na tabela ALUNOS:")
                exibe_resposta_dicionario(resposta)

        elif opcao == "5":
            while True:
                telefone = pergunta_string("PESQUISA PELO TELEFONE DO ALUNO", "insira o telefone do aluno: ")
                if not telefone:
                    break
                resposta = buscar_telefone_em_alunos(telefone, cursor)
                print(f"\nAo pesquisar pelo telefone {telefone} na tabela ALUNOS:")
                exibe_resposta_dicionario(resposta)

        else:
            print("Alternativa inválida. Tente novamente.")


def buscar_id_aluno_em_alunos(id_aluno, cursor):
    cursor.execute('SELECT * FROM alunos WHERE id_alunos = ?', (id_aluno,))
    resultado = cursor.fetchone()
    if resultado:
        return {
            "nome": resultado[1],
            "data_nascimento": resultado[2],
            "cpf": resultado[3],
            "email": resultado[4],
            "telefone": resultado[5],
            "endereco": resultado[6]
        }
    return None


def buscar_nome_em_alunos(nome, cursor):
    cursor.execute('SELECT * FROM alunos WHERE nome = ?', (nome,))
    resultado = cursor.fetchall()
    if resultado:
        registros = []
        for linha in resultado:
            registros.append({
                "id_aluno": linha[0],
                "data_nascimento": linha[2],
                "cpf": linha[3],
                "email": linha[4],
                "telefone": linha[5],
                "endereco": linha[6]
            })
        return registros
    return None


def buscar_cpf_em_alunos(cpf, cursor):
    cursor.execute('SELECT * FROM alunos WHERE cpf = ?', (cpf,))
    resultado = cursor.fetchone()
    if resultado:
        return {
            "id_aluno": resultado[0],
            "nome": resultado[1],
            "data_nascimento": resultado[2],
            "email": resultado[4],
            "telefone": resultado[5],
            "endereco": resultado[6]
        }
    return None


def buscar_email_em_alunos(email, cursor):
    cursor.execute('SELECT * FROM alunos WHERE email = ?', (email,))
    resultado = cursor.fetchone()
    if resultado:
        return {
            "id_aluno": resultado[0],
            "nome": resultado[1],
            "data_nascimento": resultado[2],
            "cpf": resultado[3],
            "telefone": resultado[5],
            "endereco": resultado[6]
        }
    return None


def buscar_telefone_em_alunos(telefone, cursor):
    cursor.execute('SELECT * FROM alunos WHERE telefone = ?', (telefone,))
    resultado = cursor.fetchone()
    if resultado:
        return {
            "id_aluno": resultado[0],
            "nome": resultado[1],
            "data_nascimento": resultado[2],
            "cpf": resultado[3],
            "email": resultado[4],
            "endereco": resultado[6]
        }
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