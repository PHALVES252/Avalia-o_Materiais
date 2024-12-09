from select_alunos import menu_alunos
from select_professores import menu_professores
from select_cursos import menu_cursos
from select_disciplinas import menu_disciplina
from select_avaliacoes import menu_avaliacoes
from select_matriculas import menu_matriculas
from select_frequencias import menu_frequencias

def pesquisar(tabela, cursor):
    if tabela == "1":  # ALUNOS
        menu_alunos(cursor)
    elif tabela == "2":  # PROFESSORES
        menu_professores(cursor)
    elif tabela == "3":  # CURSOS
        menu_cursos(cursor)
    elif tabela == "4":  # DISCIPLINA
        menu_disciplina(cursor)
    elif tabela == "5":  # AVALIAÇÕES
        menu_avaliacoes(cursor)
    elif tabela == "6":  # MATRÍCULAS
        menu_matriculas(cursor)
    elif tabela == "7":  # FREQUÊNCIAS
        menu_frequencias(cursor)