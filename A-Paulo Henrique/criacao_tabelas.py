
def criar(tabela, cursor, conn):
    resultado = False
    if tabela == "1":
        resultado = criar_tabela_alunos(cursor, conn)
    elif tabela == "2":
        resultado = criar_tabela_professores(cursor, conn)
    elif tabela == "3":
        resultado = criar_tabela_cursos(cursor, conn)
    elif tabela == "4":
        resultado = criar_tabela_disciplinas(cursor, conn)
    elif tabela == "5":
        resultado = criar_tabela_avaliacoes(cursor, conn)
    elif tabela == "6":
        resultado = criar_tabela_matriculas(cursor, conn)
    elif tabela == "7":
        resultado = criar_tabela_frequencias(cursor, conn)

    # Exibir mensagem de sucesso se a tabela foi criada
    if resultado:
        print(f"\nTabela {resultado.upper()} criada com sucesso.\n")


def criar_tabela(nome_tabela, query, cursor, conn):
    try:
        cursor.execute(query)
        conn.commit()
        return nome_tabela
    except Exception as e:
        print(f"Falha ao criar a tabela {nome_tabela.upper()}.\nErro: {e}")
        return False


def criar_tabela_alunos(cursor, conn):
    query = '''CREATE TABLE IF NOT EXISTS alunos (
                    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    data_nascimento DATE NOT NULL,
                    cpf TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE,
                    telefone TEXT,
                    endereco TEXT); '''
    return criar_tabela("alunos", query, cursor, conn)


def criar_tabela_cursos(cursor, conn):
    return criar_tabela("cursos", '''
                    CREATE TABLE IF NOT EXISTS cursos (
                        id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        descricao TEXT,
                        duracao INTEGER CHECK(duracao > 0) NOT NULL
                    ); ''', cursor, conn)


def criar_tabela_disciplinas(cursor, conn):
    return criar_tabela("disciplinas", '''
                    CREATE TABLE IF NOT EXISTS disciplinas (
                        id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_curso INTEGER NOT NULL,
                        id_professor INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        descricao TEXT,
                        FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
                        FOREIGN KEY (id_professor) REFERENCES professores(id_professor)
                    ); ''', cursor, conn)


def criar_tabela_professores(cursor, conn):
    return criar_tabela("professores", '''
                    CREATE TABLE IF NOT EXISTS professores (
                    
                        id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
                        
                        nome TEXT NOT NULL,
                        cpf TEXT UNIQUE NOT NULL,
                        email TEXT UNIQUE,
                        telefone TEXT,
                        
                        formacao TEXT
                    ); ''', cursor, conn)


def criar_tabela_avaliacoes(cursor, conn):
    return criar_tabela("avaliacoes", '''
                    CREATE TABLE IF NOT EXISTS avaliacoes (
                        
                        id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
                        
                        id_disciplina INTEGER NOT NULL,
                        id_professor INTEGER NOT NULL,
                        id_aluno INTEGER NOT NULL,
                        data_avaliacao DATE NOT NULL,
                        
                        nota REAL CHECK(nota >= 0 AND nota <= 10),
                        descricao TEXT,
                        
                        FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id_disciplina),
                        FOREIGN KEY (id_professor) REFERENCES professores(id_professor),
                        FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno)
                    ); ''', cursor, conn)


def criar_tabela_matriculas(cursor, conn):
    return criar_tabela("matriculas", '''
                    CREATE TABLE IF NOT EXISTS matriculas (
                        
                        id_matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                        
                        id_aluno INTEGER NOT NULL,
                        id_curso INTEGER NOT NULL,
                        data_matricula DATE NOT NULL,
                        
                        FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
                        FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
                    );''', cursor, conn)


def criar_tabela_frequencias(cursor, conn):
    return criar_tabela("frequencias", '''
                CREATE TABLE IF NOT EXISTS frequencias (
                
                    id_frequencia INTEGER PRIMARY KEY AUTOINCREMENT,
                    
                    id_aluno INTEGER NOT NULL,
                    id_disciplina INTEGER NOT NULL,
                    id_matricula INTEGER NOT NULL,
                    data DATE NOT NULL,
                    
                    presente INTEGER CHECK(presente IN (0, 1)),
                    
                    
                    
                    FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
                    FOREIGN KEY (id_matricula) REFERENCES matriculas(id_matricula),
                    FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id_disciplina)
                ); ''', cursor, conn)
