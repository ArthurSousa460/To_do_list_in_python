from os import system
from time import sleep

lista = []
tarefa = dict()

def listar_nomes():
    i = 1
    for t in lista:
        print(f"Tarefa {i}: {t['tarefa']}")
        i+=1

def menu_principal():
    print('''
                  To Do
-------------------------------------------
1 - Cadastrar um tarefa
2 - Marcar tarefa como concluida
3 - Listar todas as tarefas
4 - pesquisar_tarefar uma tarefa
5 - Editar uma tarefa
6 - Excluir uma tarefa
7 - Sair
-------------------------------------------''')
    escolha = int(input("Opção: "))
    system('clear')
    return escolha

def menu_editar():
    print('''             MENU DE ESCOLHA
-------------------------------------------
1 - Alterar nome
2 - Alterar data
3 - Alterar local  
4 - Alterar TUDO        
-------------------------------------------''')
    escolha = int(input("Opção: "))
    return escolha

def data_dividida(data: str):
    date = list()
    try:
        dia, mes, ano = data.split("/")
        date.append(int(dia))
        date.append(int(mes))
        date.append(int(ano))
        return date
    except:
        return

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
    try:
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
    except:
        return 

def cadastrar():
    tarefa_input = str(input("Tarefa: "))
    data = str(input("Data da tarefa: "))
    local = str(input("local: "))
    if validar_data(data) == True:
        tarefa["tarefa"] = tarefa_input
        tarefa["data"] = data
        tarefa["local"] = local
        tarefa["status"] = "pendente"
        lista.append(tarefa.copy())
        tarefa.clear()
        system("clear")
        print("Adcionado com sucesso!")
        sleep(0.8)
    else:
        system("clear")
        print("Dados inválidos, tarefa não adcionada.")
        sleep(2)

def concluir_tarefa():
    listar_nomes()
    print("")
    alterar = str(input("Qual tarefa deseja concluir?: "))
    o = 1
    for i in lista:
        if i['tarefa'] == alterar:
            o += 1
            i['status'] = 'concluido'
            system('clear')
            print("Tarefa concluida")
        if o == 1:
            print("Tarefa não encontrada!!!")
            o = 0

def listar_tarefas():
    for i in lista:
        print(f'''Tarefa: {i['tarefa']}
Data: {i['data']}
Local: {i['local']}
Status: {i['status']}
-------------------------------------------''')
    input("precione ENTER para sair:")

def pesquisar_tarefa():
    listar_nomes()
    print("")
    Escolha = str(input('Qual tarefa você deseja pesquisar? '))
    system('clear')
    for c in lista:
        if c ['tarefa'] == Escolha:
            print(f"Tarefa: {c['tarefa']}")
            print(f"Data: {c['data']}")
            print(f"Local: {c['local']}")
            print(f"Status: {c['status']}")
            print("-------------------------------------------")

def editar_tarefa():
    listar_nomes()
    print("")
    editar = input("Qual tarefa deseja editar?: ")
    system('clear')
    for i in lista:
        if i['tarefa'] == editar:
            print(f'''-------------------------------------------
Tarefa: {i['tarefa']}
Data: {i['data']}
Local: {i['local']}
Status: {i['status']}
-------------------------------------------''')
            opc = menu_editar()
            match opc:
                case 1:
                    system('clear')
                    nova_descricao = str(input("Nova descrição: "))
                    i['tarefa'] = nova_descricao
                    system('clear')
                    print("Alterado com sucesso!!!")
                case 2:
                    system('clear')
                    nova_data = str(input("Nova data: "))
                    i['data'] = nova_data
                    system('clear')
                    print("Alterado com sucesso!!!")
                case 3:
                    system('clear')
                    novo_local = str(input("Novo local: "))
                    i['local'] = novo_local
                    system('clear')
                    print("Alterado com sucesso!!!")
                case 4:
                    system('clear')
                    nova_descricao = str(input("Nova descrição: "))
                    nova_data = str(input("Nova data: "))
                    novo_local = str(input("Novo local: "))
                    local = lista.index(i)
                    lista[local] = {
                        'tarefa': nova_descricao,
                        'data': nova_data,
                        'local': novo_local,
                        'status': 'Pendente'
                    }
                    system('clear')
                    print("Alterado com sucesso!!!")

def excluir_tarefa():
    listar_nomes()
    tarefa = str(input("Qual tarefa deseja excluir: "))
    for i in lista:
        if i['tarefa'] == tarefa:
            local = lista.index(i)
            lista.pop(local)
            system('clear')
            print("excluido com sucesso!!!")       

def programa():
    while True:
        opção = menu_principal()
        match opção:
            case 1:
                cadastrar()
            case 2:
                if len(lista) == 0:
                    print('Você não possui nenhuma tarefa!!')
                else:
                    concluir_tarefa()
                    sleep(1)
            case 3:
                if len(lista) == 0:
                    print('Você não possui nenhuma tarefa!!')
                else:
                    system('clear')
                    listar_tarefas()
            case 4:
                if len(lista) == 0:
                    print('Você não possui nenhuma tarefa!!')
                else:
                    pesquisar_tarefa()
                    sleep(1)
            case 5:
                if len(lista) == 0:
                    print('Você não possui nenhuma tarefa!!')
                else:
                    editar_tarefa()
                    sleep(1)
            case 6:
                if len(lista) == 0:
                    print('Você não possui nenhuma tarefa!!')
                else:
                    excluir_tarefa()
                    sleep(1)
            case 7:
                print("Saindo...")
                sleep(1)
                break
            case _:
                print("Invalido...\nTente novamente")

programa()