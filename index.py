"""
1 - adicionar, ver, atualizar, completar, deletar completadas, sair
"""

def list():
    lista = []
    indice = 1
    check = "✅"
    while True:
        valor = input(f"{'='*30} \nLISTA DE TAREFAS \n {'='*30} Escolha uma opção abaixo: \n [ 1 ] - Adicionar tarefa \n [ 2 ] - Visualizar tarefas \n [ 3 ] - Atualizar tarefa \n [ 4 ] - Deletar tarefas concluídas \n [ 5 ] Sair")

        if valor == "5":
            break
        elif valor == "1":
            resposta = input("Informe o nome da tarefa a ser adicinada: ")
            tarefa = f"{indice} - [ ]"
            tarefa += resposta
            indice += 1
            lista.append(tarefa)
        elif valor == "2":
            print(f"{'='*30}\nTarefas adicionadas: \n{lista} \n")
        elif valor == "3":
            print(f"{'='*30}\nTarefas adicionadas: \n{lista} \n\n")
            atualizacao = int(input("Indique o número da tarefa que você quer modificar: "))
            
            for n in lista:
                if n == atualizacao:
                    
