tarefas = []
id_atual = 1

def adicionar_lista():
    global id_atual
    titulo = input("Informe o título da tarefa: ")
    nova_tarefa = {
        "id": id_atual,
        "titulo": titulo,
        "concluido": False
    }
    tarefas.append(nova_tarefa)
    id_atual += 1

def mostrar_tarefa():
    print(f"\n📋 LISTA DE TAREFAS")
    for tarefa in tarefas:
        status = "[X]" if tarefa["concluido"] else "[ ]"
        print(f"{status} - {tarefa['titulo']}")

def completar_tarefa():
    id_tarefa = int(input("Informe o número da tarefa concluída: "))
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["concluido"] = True
            break

def atualizar_tarefa():
    id_tarefa = int(input("Informe o número da tarefa para atualizar: "))
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            novo_nome = input("Informe o novo nome da tarefa: ")
            tarefa["titulo"] = novo_nome
            break

def deletar_completas():
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if not tarefa["concluido"]]
    print("Todas as tarefas concluídas foram removidas.")

def inicio():
    while True:
        try:
            iniciar = int(input(
                "\nEscolha uma opção:\n"
                "[1] - Adicionar nova tarefa\n"
                "[2] - Mostrar tarefas\n"
                "[3] - Completar uma tarefa\n"
                "[4] - Atualizar tarefa\n"
                "[5] - Deletar tarefas concluídas\n"
                "[6] - Sair\n> "
            ))

            if iniciar == 1:
                adicionar_lista()
            elif iniciar == 2:
                mostrar_tarefa()
            elif iniciar == 3:
                completar_tarefa()
            elif iniciar == 4:
                atualizar_tarefa()
            elif iniciar == 5:
                deletar_completas()
            elif iniciar == 6:
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")

inicio()