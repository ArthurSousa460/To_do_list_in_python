from os import system
from time import sleep

todo_list= []
tarefa = dict()



def data_dividida(data: str):
    date = list()
    dia, mes, ano = data.split("/")
    date.append(int(dia))
    date.append(int(mes))
    date.append(int(ano))
    return date


def validar_dia(dia):
    if dia > 0 and dia <= 31:
        return True
    return False


def validar_mes(mes):
    if mes > 0 and mes <= 12:
        return True
    return False


def validar_ano(ano):
    if ano > 0 and (ano / 1000) >= 1:
        return True
    return False 



def validar_data(data: str):
    #função que valida a data por inteiro, exigindo uma data em forma de srting
    #Retorna valores verdadeiro(True) e falso (False) 
    data_split = data_dividida(data)
    dia_valido = validar_dia(data_split[0])
    mes_valido = validar_mes(data_split[1])
    ano_valido = validar_ano(data_split[2])
    if dia_valido == True and mes_valido == True and ano_valido == True:
        if data_split[2] % 4 == 0:
            if data_split[1] == 2:
                if data_split[0] > 0 and data_split[0] <= 29:
                    return True
        if data_split[2] % 4 != 0:
            if data_split[1] == 2:
                if data_split[0] > 0 and data_split[0] <= 28:
                    return True 
        if data_split[1] == 1 or data_split[1] == 3 or data_split[1] == 5 or data_split[1] == 7 or data_split[1] == 8 or data_split[1] == 10 or data_split[1] == 12:
            if data_split[0] > 0 and data_split[0] <= 31:
                return True
        if data_split[1] == 4 or data_split[1] == 6 or data_split[1] == 9 or data_split[1] == 11:
            if data_split[0] > 0 and data_split[0] <= 30:
                return True
    return False



def menu_principal():
    print('''
                  To Do
-------------------------------------------
1 - Cadastrar um tarefa
2 - Marcar tarefa como concluida
3 - Listar todas as tarefas
4 - Pesquisar uma tarefa
5 - Editar uma tarefa
6 - Excluir uma tarefa
7 - Sair
-------------------------------------------''')
    escolha = int(input("Opção: "))
    system('cls')
    return escolha

def cadastrar():
    tarefa_input = str(input("Tarefa: "))
    data_conclusao = str(input("Data da tarefa: "))
    local = str(input("local: "))
    if validar_data(data_conclusao) == True:
        tarefa["tarefa"] = tarefa_input
        tarefa["data_de_conclusao"] = data_conclusao
        tarefa["local"] = local
        tarefa["status"] = "pendente"
        todo_list.append(tarefa.copy())
        tarefa.clear()
        system("cls")
        print("Adcionado com sucesso!")
        sleep(0.8)
    else:
        system("cls")
        print("Dados inválidos, tarefa não adcionada.")
        sleep(0.8)

        

def listar_tarefas():
    for c in todo_list:
        print(c["tarefa"])
        print(c["local"])
        print(c["status"])

def programa():
    while True:
        opção = menu_principal()
        match opção:
            case 1:
                cadastrar()
            case 2:
                system('cls')
                listar_tarefas()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("Saindo...")
                break
            case _:
                print("Invalido...\nTente novamente")

programa()
