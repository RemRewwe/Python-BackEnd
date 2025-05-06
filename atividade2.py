def gerenciador_tarefas():
    tarefas = []

    while True:
        print("Gerenciador de tarefas. \n1. Adicionar\n2. Listar\n3. Concluir\n4. Remover\n5. Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            t = input("Tarefa: ").strip()
            if t: tarefas.append({"tarefa": t, "concluida": False})
        elif opcao == '2':
            [print(f"{i+1}. [{'✓' if t['concluida'] else ' '}] {t['tarefa']}") for i, t in enumerate(tarefas)] or print("Sem tarefas.")
        elif opcao == '3':
            try:
                i = int(input("Número: ")) - 1
                if 0 <= i < len(tarefas): tarefas[i]["concluida"] = True
            except: print("Entrada inválida.")
        elif opcao == '4':
            try:
                i = int(input("Número: ")) - 1
                if 0 <= i < len(tarefas): tarefas.pop(i)
            except: print("Entrada inválida.")
        elif opcao == '5':
            break
        else:
            print("Inválido.")

gerenciador_tarefas()
