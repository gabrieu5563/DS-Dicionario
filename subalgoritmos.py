import os

def adicionar(d : dict) -> dict:
    while True:
        os.system("cls")
        nome = input("Nome do aluno: ")

        while True:
            nota = input(f"Nota de {nome}: ")
            if verif_nota(nota):
                break
            else:
                print("Nota inválida.")

        if nome in d:
            print(f"Aluno de nome '{nome}' já cadastrado.")
            input("Pressione qualquer tecla para continuar...")
        elif len(d) >= 10:
            print("Limite de 10 alunos atingido. Apague algum aluno antes de adicionar um novo.")
            break
        else:
            d[nome] = nota
            print(f"Aluno {nome} cadastrado com sucesso!")
            input("Pressione qualquer tecla para continuar...")
            return d
            break


def verif_nota(n) -> bool:
    try:
        m = float(n)
        if 0 <= m <= 10:
            return True
        else:
            return False
    except ValueError:
        return False


def exibir(d: dict) -> None:
    os.system("cls")
    print(f"{'Aluno':<30} | {'Nota:>20'}")
    print("-" * 55)
    for k, v in d.items():
        print(f"{k:<30} | {v:>20}")

    input("Pressione qualquer tecla para continuar...")


def editar(d: dict) -> dict:
    rep = 1
    while rep == 1:
        os.system("cls")
        nome = input("Nome do aluno que será editado: ")
        if nome in d:
            while True:
                nota = input(f"Nova nota de {nome}: ")
                if verif_nota(nota):
                    input("Alteração feita com sucesso.\nPressione qualquer tecla para continuar...")
                    d[nome] = float(nota)
                    rep = 0
                    break
                else:
                    print("Nota inváida.")

        else:
            print(f"Aluno {nome} não encontrado.")
            input("Pressione qualquer tecla para continuar...")

def excluir(d: dict, nome: str, conf: str) -> dict:
    if int(conf) == 1:
        print(f"Aluno {nome} excluído com sucesso.")
        input("Pressione qualquer tecla para continuar...")
        del d[nome]
    else:
        input("Operação cancelada. Pressione qualquer tecla para continuar...")

def media(d: dict) -> None:
    temp = 0
    for v in d.values():
        temp += v
    res = temp / len(d)
    os.system("cls")
    print(f"A média da sala é {str(res)}.")
    input("Pressione qualquer tecla para continuar...")

def consulta(d: dict) -> None:
    while True:
        os.system("cls")
        nome = input("Nome do aluno que deseja consultar: ")
        if nome not in d:
            print(f"Aluno {nome} não encontrado.")
            input("Pressione qualquer tecla para continuar...")
        else:
            print(f"{'Aluno':<30} | {'Nota':>20}")
            print("-" * 55)
            print(f"{nome:<30} | {d[nome]:>20}")
            input("Pressione qualquer tecla para continuar...")
            break

def excluir_sala(d: dict, conf: str) -> dict:
    os.system("cls")
    match int(conf):
        case 1:
            d.clear()
            input("Alunos apagados.\nPressione qualquer tecla para continuar...")

        case 2:
            input("Operação cancelada. Pressione qualquer tecla para continuar...")

def verif_conf(conf: str) -> bool:
    if conf.isnumeric() and (conf == "1" or conf == "2"):
        r = True
    else:
        r = False
    return r