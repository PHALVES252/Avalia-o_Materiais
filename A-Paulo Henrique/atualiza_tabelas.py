from update_alunos import atualizar_alunos
from update_professores import atualizar_professores
from update_cursos import atualizar_cursos
from update_disciplinas import atualizar_disciplinas
from update_avaliacoes import atualizar_avaliacoes
from update_matriculas import atualizar_matriculas
from update_frequencias import atualizar_frequencias

def atualizar(tabela, cursor, conn):
    if tabela == "1":  # ALUNOS
        atualizar_alunos(cursor, conn)
    elif tabela == "2":  # PROFESSORES
        atualizar_professores(cursor, conn)
    elif tabela == "3":  # CURSOS
        atualizar_cursos(cursor, conn)
    elif tabela == "4":  # DISCIPLINA
        atualizar_disciplinas(cursor, conn)
    elif tabela == "5":  # AVALIAÇÕES
        atualizar_avaliacoes(cursor, conn)
    elif tabela == "6":  # MATRÍCULAS
        atualizar_matriculas(cursor, conn)
    elif tabela == "7":  # FREQUÊNCIAS
        atualizar_frequencias(cursor, conn)