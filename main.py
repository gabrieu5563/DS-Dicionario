import os
from subalgoritmos import *
os.system("cls")

alunos = {
    'Pedro': 14,
    'João': 23,
    'Augusto': 1,
    'Patrício': 8.9
}

rep = 1
while rep == 1:
    os.system("cls")
    print("0 - Sair")
    print("1 - Adicionar novo aluno | nota (limite de 10 alunos)")
    print("2 - Editar aluno | nota")
    print("3 - Listar os alunos")
    print("4 - Excluir um aluno")
    print("5 - Calcular a média da turma")
    print("6 - Consultar um aluno")
    print("7 - Apagar todos os alunos")
    ex = input("Escolha uma opção: ")

    if not ex.isnumeric():
        input("Opção inválida.\nPressione qualquer tecla para continuar...")
        continue

    match int(ex):

        case 0:
            rep = 0

        case 1:
            adicionar(alunos)

        case 2:
            editar(alunos)

        case 3:
            exibir(alunos)

        case 4:
            os.system("cls")
            nome = input("Nome do aluno que será excluído: ")
            if nome not in alunos:
                print(f"Aluno {nome} não encontrado.")
                input("Pressione qualquer tecla para continuar...")
            else:
                conf = input(f"Você tem certeza que quer apagar {nome} \n1 - Sim     2 - Não\n")
                if verif_conf(conf):
                    excluir(alunos, nome, conf)
                else:
                    input("Opção inválida.\nPressione qualquer tecla para continuar...")

        case 5:
            media(alunos)

        case 6:
            consulta(alunos)

        case 7:
            conf = input("Você tem certeza que quer apagar todos os alunos da sala?\n1 - Sim     2 - Não\n")
            if verif_conf(conf):
                excluir_sala(alunos, conf)
            else:
                input("Opção inválida.\nPressione qualquer tecla para continuar...")
            
        case _:
            input("Opção inválida.\nPressione qualquer tecla para continuar...")
            os.system("cls")