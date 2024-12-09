def inserir(tabela, cursor, conn):
    if tabela == "1":
        # nome, data_nascimento, cpf, email, telefone, endereco
        alunos = [
            ("Jorge", "2005-04-10", "12345678901", "jorge@example.com", "11999998888", "Rua A, 123"),
            ("Jorge", "2004-08-15", "12313432100", "jo@example.com", "12348887777", "Rua B, 456"),
            ("Julio Silva", "2004-08-15", "12313231100", "juju@example.com", "13458887777", "Rua B, 456"),
            ("Joaquim Silva", "2004-08-15", "12313123100", "joca@example.com", "15467887777", "Rua B, 456"),
            ("Joana Silva", "2004-08-15", "23423232100", "joana@example.com", "16788887777", "Rua B, 456")
        ]
        inserir_na_tabela_alunos(alunos, cursor, conn)

    elif tabela == "2":
        # nome, cpf, email, telefone, formacao
        professores = [
            ("Carlos", "11231314556", "caca@example.com", "12342342346", "Pedagogia"),
            ("Carlos", "61233131211", "carlos@example.com", "13456665555", "Engenharia"),
            ("Caio", "12333131211", "caio@example.com", "11236345555", "História"),
            ("Cesar", "61123131211", "cesar@example.com", "11346535555", "Matemática"),
            ("Cesar", "61123213311", "cece@example.com", "34536665555", "Geografia")
        ]
        inserir_na_tabela_professores(professores, cursor, conn)

    elif tabela == "3":
        # nome, descricao, duracao
        cursos = [
            ("Culinária", "Curso de culinária elementar", 100),
            ("Culinária", "Curso de culinária intermediária", 150),
            ("Informática", "Curso Técnico em Informática", 200),
            ("Mecânica", "Curso de Mecânica Indistrial", 600),
            ("Mecânica", "Curso de Mecânica Automotiva", 6)
        ]
        inserir_na_tabela_cursos(cursos, cursor, conn)

    elif tabela == "4":
        # id_curso, id_professor, nome, descricao
        disciplinas = [
            (1, 1, "Cortes Bovinos", "Introdução à arte do corte de carne bovina"),
            (2, 2, "Mecânica", "Estudo de mecânica clássica"),
            (2, 2, "Mecânica", "Estudo de mecânica clássica")
        ]
        inserir_na_tabela_disciplinas(disciplinas, cursor, conn)

    elif tabela == "5":
        # id_disciplina, id_professor, id_aluno, data_avaliacao, nota, descricao
        avaliacoes = [
            (1, 1, 1, "01-01-2024", 8.5, "Prova de Álgebra"),
            (1, 1, 2, "01-01-2024", 9.0, "Prova de Mecânica"),
            (1, 1, 3, "01-01-2024", 9.0, "Prova de Mecânica"),
            (1, 2, 1, "01-01-2024", 9.0, "Prova de Mecânica"),
            (1, 2, 2, "01-01-2024", 9.0, "Prova de Mecânica"),
            (1, 2, 3, "01-01-2024", 9.0, "Prova de Mecânica"),
            (1, 3, 1, "01-01-2024", 9.0, "Prova de Mecânica"),
            (1, 3, 2, "01-01-2024", 9.0, "Prova de Mecânica"),
            (1, 3, 3, "01-01-2024", 9.0, "Prova de Mecânica"),
            (2, 1, 1, "2024-05-01", 8.5, "Prova de Álgebra"),
            (2, 1, 2, "2024-05-10", 9.0, "Prova de Mecânica"),
            (2, 1, 3, "2024-05-10", 9.0, "Prova de Mecânica"),
            (2, 2, 1, "2024-05-10", 9.0, "Prova de Mecânica"),
            (2, 2, 2, "2024-05-10", 9.0, "Prova de Mecânica"),
            (2, 2, 3, "2024-05-10", 9.0, "Prova de Mecânica"),
            (2, 3, 1, "2024-05-10", 9.0, "Prova de Mecânica"),
            (2, 3, 2, "2024-05-10", 9.0, "Prova de Mecânica"),
            (2, 3, 3, "2024-05-10", 9.0, "Prova de Mecânica"),
            (3, 1, 1, "2024-05-01", 8.5, "Prova de Álgebra"),
            (3, 1, 2, "2024-05-10", 9.0, "Prova de Mecânica"),
            (3, 1, 3, "2024-05-10", 9.0, "Prova de Mecânica"),
            (3, 2, 1, "2024-05-10", 9.0, "Prova de Mecânica"),
            (3, 2, 2, "2024-05-10", 9.0, "Prova de Mecânica"),
            (3, 2, 3, "2024-05-10", 9.0, "Prova de Mecânica"),
            (3, 3, 1, "2024-05-10", 9.0, "Prova de Mecânica"),
            (3, 3, 2, "2024-05-10", 9.0, "Prova de Mecânica"),
            (3, 3, 3, "2024-05-10", 9.0, "Prova de Mecânica")
        ]
        inserir_na_tabela_avaliacoes(avaliacoes, cursor, conn)

    elif tabela == "6":
        # id_aluno, id_curso, data_matricula
        matriculas = [
            (1, 1, "2024-01-20"),
            (2, 2, "2024-01-21")
        ]
        inserir_na_tabela_matriculas(matriculas, cursor, conn)

    elif tabela == "7":
        # id_aluno, id_matricula, id_disciplina, data, presente (1 = Presente / 0 = Ausente)
        frequencias = [
            (1, 1, 1, "2024-05-01", 1),
            (2, 1, 1, "2024-05-01", 0)
        ]
        inserir_na_tabela_frequencias(frequencias, cursor, conn)


def inserir_na_tabela_alunos(alunos, cursor, conn):
    try:
        cursor.executemany('''
            INSERT INTO alunos (nome, data_nascimento, cpf, email, telefone, endereco)
            VALUES (?, ?, ?, ?, ?, ?);
        ''', alunos)
        conn.commit()
        print("Alunos inseridos com sucesso.")
    except Exception as e:
        print(f"Falha ao inserir alunos.\nErro: {e}")
        return False
    return True


def inserir_na_tabela_cursos(cursos, cursor, conn):
    try:
        cursor.executemany('''
            INSERT INTO cursos (nome, descricao, duracao)
            VALUES (?, ?, ?);
        ''', cursos)
        conn.commit()
        print("Cursos inseridos com sucesso.")
    except Exception as e:
        print(f"Falha ao inserir cursos.\nErro: {e}")
        return False
    return True


def inserir_na_tabela_disciplinas(disciplinas, cursor, conn):
    try:
        cursor.executemany('''
            INSERT INTO disciplinas (id_curso, id_professor, nome, descricao)
            VALUES (?, ?, ?, ?);
        ''', disciplinas)
        conn.commit()
        print("Disciplinas inseridas com sucesso.")
    except Exception as e:
        print(f"Falha ao inserir disciplinas.\nErro: {e}")
        return False
    return True


def inserir_na_tabela_professores(professores, cursor, conn):
    try:
        cursor.executemany('''
            INSERT INTO professores (nome, cpf, email, telefone, formacao)
            VALUES (?, ?, ?, ?, ?);
        ''', professores)
        conn.commit()
        print("Professores inseridos com sucesso.")
    except Exception as e:
        print(f"Falha ao inserir professores.\nErro: {e}")
        return False
    return True


def inserir_na_tabela_avaliacoes(avaliacoes, cursor, conn):
    try:
        cursor.executemany('''
            INSERT INTO avaliacoes (id_disciplina, id_professor, id_aluno, data_avaliacao, nota, descricao)
            VALUES (?, ?, ?, ?, ?, ?);
        ''', avaliacoes)
        conn.commit()
        print("Avaliações inseridas com sucesso.")
    except Exception as e:
        print(f"Falha ao inserir avaliações.\nErro: {e}")
        return False
    return True


def inserir_na_tabela_matriculas(matriculas, cursor, conn):
    try:
        cursor.executemany('''
            INSERT INTO matriculas (id_aluno, id_curso, data_matricula)
            VALUES (?, ?, ?);
        ''', matriculas)
        conn.commit()
        print("Matrículas inseridas com sucesso.")
    except Exception as e:
        print(f"Falha ao inserir matrículas.\nErro: {e}")
        return False
    return True


def inserir_na_tabela_frequencias(frequencias, cursor, conn):
    try:
        cursor.executemany('''
            INSERT INTO frequencias 
            (id_aluno, id_matricula, id_disciplina, data, presente)
            VALUES (?, ?, ?, ?, ?);
        ''', frequencias)
        conn.commit()
        print("Frequências inseridas com sucesso.")
    except Exception as e:
        print(f"Falha ao inserir frequências.\nErro: {e}")
        return False
    return True
