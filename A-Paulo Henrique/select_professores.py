
def menu_professores(cursor):
    while True:
        print("\n" * 2)
        print("-" * 42)
        print("PESQUISAR EM PROFESSORES")
        print("-" * 42)
        print("1) Id professor")
        print("2) Nome")
        print("3) CPF")
        print("4) E-Mail")
        print("5) Telefone")
        print("-" * 42)
        print("0) Voltar")
        print("-" * 42)
        
        opcao = input("Escolha uma opção (1/5) ou 0 para voltar: ").strip()
        
        if opcao == '0':
            return
        
        elif opcao == '1':
            while True:
                id_professor = pergunta_inteiro("PESQUISA PELO ID DO PROFESSOR", "Insira o ID do professor: ")
                if not id_professor:
                    break
                resposta = buscar_id_professor_em_professores(id_professor, cursor)
                print(f"\nAo pesquisar pelo ID '{id_professor}' na tabela professorS:")
                exibe_resposta_dicionario(resposta)

        elif opcao == '2':
            while True:
                nome = pergunta_string("PESQUISA PELO NOME DO PROFESSOR", "Insira o nome do professor: ")
                if not nome:
                    break
                resposta = buscar_nome_em_professores(nome, cursor)
                print(f"\nAo pesquisar pelo nome '{nome}' na tabela PROFESSOR:")
                exibe_resposta_lista(resposta)

        elif opcao == '3':
            while True:
                email = pergunta_string("PESQUISA PELO EMAIL DO PROFESSOR", "Insira o email do professor: ")
                if not email:
                    break
                resposta = (email, cursor)
                print(f"\nAo pesquisar pelo e-mail '{email}' na tabela professores:")
                exibe_resposta_lista(resposta)


def exibe_resposta_lista(lista):
    if lista is None:
        print("  Ops! :-|  Nenhum registro foi encontrado.")
    else:
        for linha in lista:
            exibe_resposta_dicionario(linha)


def exibe_resposta_dicionario(dicionario):
    if not dicionario:
        print("  Vixe! :-(  Nenhum registro foi encontrado.")
    else:
        for chave, valor in dicionario.items():
            print(f"  O campo: '{chave}' contém o valor: '{valor}'.")


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


def buscar_id_professor_em_professores(id_professor, cursor):
    cursor.execute('''SELECT * FROM professores WHERE id_professor=?''', (id_professor,))
    resposta = cursor.fetchone()
    if resposta:
        return {
            "nome": resposta[1],
            "cpf": resposta[2],
            "email": resposta[3],
            "telefone": resposta[4],
            "formacao": resposta[5]
        }
    else:
        return None


def buscar_nome_em_professores(nome, cursor):
    cursor.execute('''SELECT * FROM professores WHERE nome = ?''', (nome,))
    respostas = cursor.fetchall()
    if respostas:
        registros = []
        for resposta in respostas:
            registros.append({'id_professor': resposta[0],
                              'cpf': resposta[2],
                              'email': resposta[3],
                              'telefone': resposta[4]})
        return registros
    return None


def buscar_email_em_professores(email, cursor):
    cursor.execute('''SELECT * FROM PROFESSORES WHERE email=?''', (email,))
    resposta = cursor.fetchone()
    if resposta:
        return {
            'id_professor': resposta[0],
            'nome': resposta[1],
            'cpf': resposta[2],
            'telefone': resposta[4]}


def buscar_cpf_em_professores(cpf, cursor):
    cursor.execute('''SELECT * FROM PROFESSORES WHERE cpf=?''', (cpf,))
    resposta = cursor.fetchone()
    if resposta:
        return{
            'id_professor': resposta[0],
            'nome': resposta[1],
            'email': resposta[3],
            'telefone': resposta[4]
        }
